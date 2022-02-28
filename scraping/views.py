# from django.shortcuts import render
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder

from scraping.models import Proxy
from scraping.scraping import get_proxies

# Create your views here.


def index(request):

    proxies_list = get_proxies()
    for proxy in proxies_list:
        Proxy.objects.create(
            ip=proxy["ip"],
            port=proxy["port"],
            protocol=proxy["protocol"],
            anonymity=proxy["anonymity"],
            country=proxy["country"],
            region=proxy["region"],
            city=proxy["city"],
            uptime=proxy["uptime"],
            response=proxy["response"],
        )

    return HttpResponse(
        DjangoJSONEncoder().encode(proxies_list), content_type="application/json"
    )
