from django.shortcuts import render


def index(request):
    return render(request, 'website/website.html', {})