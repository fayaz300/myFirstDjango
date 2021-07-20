from django.http.response import Http404
from django.shortcuts import render
from django.http import HttpResponse
import requests
import socket
# Create your views here.
def ip(request):
    if request.method == 'POST':
        # try:
            website = str(request.POST.get('website'))
            print(website)
            ipaddr = socket.gethostbyname(website)
            print(ipaddr)
            # ipaddr = str(request.POST.get('ipaddr'))
            res = requests.get('http://ip-api.com/json/' +ipaddr)
            print(ipaddr)
            print(res.status_code)
            if res.status_code == 200:
                data = res.json()
                print("error 1")
                return render(request, 'ipdata.html', {'data':data, 'website' : website})
            else:
                print("error 2")
                return render(request, 'error.html')
        # except:
        #     print("error here")
        #     return render(request, 'error.html')
    else:
        return render(request, 'index.html')
