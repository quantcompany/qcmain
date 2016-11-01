from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.sites.shortcuts import get_current_site

from emails import send_contact_email


def home(request):
    return render(request, 'index/home.html')


def contact(request):
    data = {
        'name': request.POST.get('name', ''),
        'email': request.POST.get('email', ''),
        'subject': request.POST.get('subject', ''),
        'message': request.POST.get('message', ''),
        'phone': request.POST.get('phone', '')
    }

    send_contact_email(data, site=get_current_site(request))
    return JsonResponse({'message': 'Your message has been received. Thank You!'})
