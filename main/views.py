from django.shortcuts import render

def show_main(request):
    context = {
        
        'app': 'EGO Gear',
        'name': 'Muhammad Rafi Sugianto',
        'class': 'PBP B',
    }

    return render(request, "main.html", context)

# Create your views here.
