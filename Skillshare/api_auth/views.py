from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.
def index(req):
    """
    Render the index page.

    
    """
   
    return HttpResponse(
                         """<h1>Hello, world! This is the index page. </h1>"""
                         )
