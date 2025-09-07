from django.shortcuts import render

def show_main(request):
    context = {
        
        'app_name': 'EGO Gear',
        'student_name': 'Muhammad Rafi Sugianto',
        'student_class': 'PBP B',
    }

    return render(request, "main.html", context)

# Create your views here.
