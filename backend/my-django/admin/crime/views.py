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

@api_view(['GET'])
@parser_classes([JSONParser])
def create_cctv_model(request):
    CrimeCctvModel().create_cctv_model()
    return JsonResponse({'result' :'create cctv model'})

@api_view(['GET'])
@parser_classes([JSONParser])
def create_population_model(request):
    CrimeCctvModel().create_population_model()
    return JsonResponse({'result' :'create population model'})

@api_view(['GET'])
@parser_classes([JSONParser])
def merge_cctv_pop(request):
    CrimeCctvModel().merge_cctv_pop()
    return JsonResponse({'result' :'create cctv pop merge'})


@api_view(['GET'])
@parser_classes([JSONParser])
def crime_sum(request):
    CrimeCctvModel().crime_sum()
    return JsonResponse({'result' :'sum crime'})


