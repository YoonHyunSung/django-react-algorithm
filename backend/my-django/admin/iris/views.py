from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from admin.iris.models import Iris

@api_view(['GET'])
@parser_classes([JSONParser])
def base(request):
    Iris().base()
    return JsonResponse({'base':'sucess'})

@api_view(['GET'])
@parser_classes([JSONParser])
def advance(request):
    Iris().advanced()
    return JsonResponse({'advance':'sucess'})

@api_view(['GET'])
@parser_classes([JSONParser])
def advance(request):
    Iris().iris_by_tf()
    return JsonResponse({'tf':'sucess'})
