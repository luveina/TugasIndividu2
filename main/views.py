from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'app_name': 'Luveina\'s Store',
        'author' : 'Luvenia Feodora Saragih',
        'class' : 'PBP F',
        'name' : 'lampu',
        'price': 25000,
        'description': 'lampu 5 watt'
    }

    return render(request, "main.html", context)