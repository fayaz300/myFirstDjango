from django.http.response import Http404
from django.shortcuts import render
from django.http import HttpResponse
import requests
import socket

def ip(request):
    if request.method == 'POST':
        try:
            website = str(request.POST.get('website'))
            ipaddr = socket.gethostbyname(website)

            res = requests.get('http://ip-api.com/json/' + ipaddr)

            if res.status_code == 200:
                data = res.json()
                return render(request, 'ipdata.html', {'data':data, 'website' : website})
            else:
                error = 'api_error'
                return render(request, 'error.html', {'error':error})
        except:
            error = 'website_error'
            return render(request, 'error.html', {'error':error})
    else:
        return render(request, 'index.html')
