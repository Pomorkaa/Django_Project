from django.shortcuts import render
from.models import Main

def main(request):
    main = Main.objects.get()
    return render(request, 'mains/list.html', {'main': main})



