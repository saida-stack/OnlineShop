from django.shortcuts import render


def home(request):
    context = {
        'page_title': 'Home Page'
    }
    return render(request, 'pages/home.html', context)


def about(request):
    context = {
        'page_title': 'About Us'
    }
    return render(request, 'pages/about.html', context)


def contact(request):
    context = {
        'page_title': 'Contact Us'
    }
    return render(request, 'pages/contact.html', context)
