import json
import threading
from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
# from django.http.request import  HttpRequest
from rest_framework.parsers import JSONParser
from rest_framework import status

from .gifting import login, subscribe


@api_view(['GET'])
def browser_login(request):
    login(number="08165383806")
    return JsonResponse({'message': 'successfully!'})


@api_view(['post'])
def cooperate_data(request):
    json_body = json.loads(request.body)
    x = threading.Thread(target=subscribe,
                         args=(json_body["name"], json_body["number"], json_body["bundle"], json_body["reference"]))
    x.start()

    return JsonResponse({'message': 'successfully!'})


def hello(test):
    print(test)
