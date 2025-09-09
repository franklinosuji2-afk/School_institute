from django.shortcuts import render

def welcome_page(request):
    return render(request, 'welcome.html')

def bye_page(request):
    return render(request, 'bye.html')