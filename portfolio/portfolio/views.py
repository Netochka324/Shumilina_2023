from django.http import HttpResponse
from django.shortcuts import render


# def home(request):
#     return render(request, 'home.html', {'hello': 'привет!', 'bye': 'пока!'})
#
#
# def reverse(request):
#     old_text = request.GET["usertext"]
#     new_text = old_text[::-1]
#     return render(request,
#                   'reverse.html',
#                   {'old_text': old_text, 'new_text': new_text, 'words': len(old_text.split())})