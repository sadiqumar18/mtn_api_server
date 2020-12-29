from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status


from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from .gifting import login

@api_view(['GET'])
def buy_data(request):
     login(number="08165383806")
     return JsonResponse({'message': 'Tutorials were deleted successfully!'})

