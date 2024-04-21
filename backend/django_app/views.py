from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser, MultiPartParser
from django_app.serializers import *
from django_app.models import *


