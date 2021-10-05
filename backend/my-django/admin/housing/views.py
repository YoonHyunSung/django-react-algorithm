from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from admin.housing.models import HousingService
from icecream import ic
import matplotlib.pyplot as plt


@api_view(['GET'])
@parser_classes([JSONParser])
def housing_info(request):
    HousingService().housing_info()
    return JsonResponse({'result': 'Housing Success'})
