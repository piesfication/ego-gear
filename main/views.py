import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.http import HttpResponse
from django.core import serializers

from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product

from django.http import HttpResponseRedirect, JsonResponse

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from django.utils.html import strip_tags

import json

import requests

from django.views.decorators.csrf import csrf_exempt
from django.utils.html import strip_tags
import json
from django.http import JsonResponse

@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")  # default 'all'

    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)

    context = {
        'app': 'EGO Gear',
        'npm': '240123456',
        'name': request.user.username,
        'class': 'PBP A',
        'product_list': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }
    return render(request, "main.html",context)


def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        product_entry = form.save(commit = False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "create_product.html", context)

@csrf_exempt
@require_POST
def create_product_ajax(request):
    if request.method != "POST":
        return JsonResponse({"success": False, "message": "Invalid request method"}, status=400)

    if not request.user.is_authenticated:
        return JsonResponse({"success": False, "message": "User not authenticated"}, status=401)

    try:
        # Use Django form for validation
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return JsonResponse({"success": True}, status=201)
        else:
            # Return form errors as JSON
            return JsonResponse({"success": False, "message": json.loads(form.errors.as_json())}, status=400)
    except Exception as e:
        return JsonResponse({"success": False, "message": str(e)}, status=500)


# def create_car(request):
#     form = CarForm(request.POST or None)

#     if form.is_valid() and request.method == 'POST':
#         product_entry = form.save(commit = False)
#         product_entry.user = request.user
#         product_entry.save()
#         return redirect('main:show_main')
    
#     context = {
#         'form': form
#     }

#     return render(request, "create_car.html", context)
    
    

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.increment_hype()

    context = {
        'product': product
    }

    return render(request, "product_detail.html", context)

def show_xml(request):
     product_list = Product.objects.all()
     xml_data = serializers.serialize("xml", product_list)
     return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    product_list = Product.objects.all()
    data = [
        {
            'id': str(product.id),
            'name': product.name,
            'stock':product.stock,
            'price':product.price,
            'brand':product.brand,
            'description': product.description,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'hype': product.hype,
            'created_at': product.created_at.isoformat() if product.created_at else None,
            'is_featured': product.is_featured,
            'user_id': product.user_id,
        }
        for product in product_list
    ]

    return JsonResponse(data, safe=False)

def show_xml_by_id(request, product_id):
   try:
       product_item = Product.objects.filter(pk=product_id)
       xml_data = serializers.serialize("xml", product_item)
       return HttpResponse(xml_data, content_type="application/xml")
   except Product.DoesNotExist:
       return HttpResponse(status=404)

# def show_json_by_id(request, product_id):
#    try:
#        product_item = Product.objects.get(pk=product_id)
#        json_data = serializers.serialize("json", [product_item])
#        return HttpResponse(json_data, content_type="application/json")
#    except Product.DoesNotExist:
#        return HttpResponse(status=404)

def show_json_by_id(request, product_id):
    try:
        product = Product.objects.select_related('user').get(pk=product_id)
        data = {
            'id': str(product.id),
            'name': product.name,
            'description': product.description,
            'price': product.price,
            'stock': product.stock,
            'brand':product.brand,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'hype': product.hype,
            'created_at': product.created_at.isoformat() if product.created_at else None,
            'is_featured': product.is_featured,
            'user_id': product.user_id,
            'user_username': product.user.username if product.user_id else None,
        }
        return JsonResponse(data)
    except product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)
   
# Create your views here.

# def add_employee(request) :

#     employee = Employee.objects.create(name="Rafi",age="19",persona="Jahat")

#     context = {

#         'nama': employee.name,
#         'age':employee.age,
#         'persona':employee.persona

#     }

#     return render(request, "main.html", context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    response.set_cookie('toast', 'You have successfully logged out!', max_age=5)
    return response

def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_product.html", context)

@csrf_exempt
def edit_product_ajax(request, id):
    if request.method == 'POST':
        try:
            product = Product.objects.get(pk=id, user=request.user)
        except Product.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Product not found'}, status=404)

        product.name = request.POST.get('name', product.name)
        product.description = request.POST.get('description', product.description)
        product.category = request.POST.get('category', product.category)
        product.thumbnail = request.POST.get('thumbnail', product.thumbnail)
        product.is_featured = 'is_featured' in request.POST
        product.save()

        return JsonResponse({'success': True, 'message': 'Product updated successfully'})
    
    return JsonResponse({'success': False, 'message': 'Invalid request method'})


def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
def delete_product_ajax(request, id):
    if request.method == "DELETE":
        product = get_object_or_404(Product, id=id)
        
        # Optional: pastikan user yang hapus adalah pemilik produk
        if request.user != product.user:
            return JsonResponse({"success": False, "error": "Unauthorized"}, status=403)
        
        product.delete()
        return JsonResponse({"success": True, "message": "Product deleted successfully!"})
    
    return JsonResponse({"success": False, "error": "Invalid request method"}, status=400)
# /////////////////////////

def register_ajax(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # login(request, user)  # login otomatis setelah register
            return JsonResponse({
                "success": True,
                "message": "Your account has been successfully created!",
                "redirect_url": reverse("main:login")  # atau halaman lain setelah register
            })
        else:
            # Ambil error pertama
            error = next(iter(form.errors.values()))[0]
            return JsonResponse({
                "success": False,
                "message": f"Register failed: {error}"
            })
    return JsonResponse({"success": False, "message": "Method harus POST"})

def register(request):
    form = UserCreationForm()

    # if request.method == "POST":
    #     form = UserCreationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request, 'Your account has been successfully created!')
    #         return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_ajax(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = JsonResponse({
                "success": True,
                "message": "Login successful!",
                "redirect_url": reverse("main:show_main")
            })
            # simpan cookie last_login
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            return JsonResponse({
                "success": False,
                "message": "Username atau password salah."
            })
    return JsonResponse({"success": False, "message": "Method harus POST"})

def login_user(request):
#    if request.method == 'POST':
#       form = AuthenticationForm(data=request.POST)

#       if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             response = HttpResponseRedirect(reverse("main:show_main"))
#             response.set_cookie('last_login', str(datetime.datetime.now()))
#             return response  

#    else:
    form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)

def proxy_image(request):
    image_url = request.GET.get('url')
    if not image_url:
        return HttpResponse('No URL provided', status=400)
    
    try:
        # Fetch image from external source
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()
        
        # Return the image with proper content type
        return HttpResponse(
            response.content,
            content_type=response.headers.get('Content-Type', 'image/jpeg')
        )
    except requests.RequestException as e:
        return HttpResponse(f'Error fetching image: {str(e)}', status=500)

@csrf_exempt
def increase_hype(request, id):
    if request.method == "POST":
        try:
            product = Product.objects.get(id=id)
            product.hype += 1
            product.save()
            return JsonResponse({"status": "success", "hype": product.hype})
        except Product.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Product not found"}, status=404)

    return JsonResponse({"status": "error", "message": "Only POST allowed"}, status=400)

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        
        name = strip_tags(data.get("name", ""))
        description = strip_tags(data.get("description", ""))
        brand = data.get("brand", "")
        category = data.get("category", "")
        thumbnail = data.get("thumbnail", "")
        stock = data.get("stock", 0)
        price = data.get("price", 0)
        hype = data.get("hype", 0)
        is_featured = data.get("is_featured", False)

        # Jika kamu ingin created_at dari Flutter
        created_at = data.get("created_at", None)

        product = Product(
            name=name,
            description=description,
            brand=brand,
            category=category,
            thumbnail=thumbnail,
            stock=stock,
            price=price,
            hype=hype,
            is_featured=is_featured,
            user=request.user,
        )
        
    
        if created_at:
                try:
                    product.created_at = created_at
                except:
                    pass

        product.save()
        
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)