from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name' : 'lampu',
        'price': 25000,
        'description': 'lampu 5 watt'
    }

    return render(request, "main.html", context)