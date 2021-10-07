from django.http import JsonResponse
from django.shortcuts import render

from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from admin.crime.models import CrimeCctvModel

@api_view(['GET'])
@parser_classes([JSONParser])
def Crime_view(request):
    CrimeCctvModel().create_crime_model()
    return JsonResponse({'result':'Crime Success'})

# Create your views here.
@api_view(['GET'])
@parser_classes([JSONParser])
def create_police_position(request):
    CrimeCctvModel().create_police_position()
    return JsonResponse({'result': 'Create Police Position Success'})
