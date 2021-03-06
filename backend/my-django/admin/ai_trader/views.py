from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from admin.ai_trader.models import AiTrader
from admin.tensor.models import Calculator, FashionClassification, TensorFunction


@api_view(['GET'])
@parser_classes([JSONParser])
def model_builder(request):
    AiTrader().model_builder()
    return JsonResponse({'AI Trader model_builder': 'SUCCESS'})

@api_view(['GET'])
@parser_classes([JSONParser])
def process(request):
    AiTrader().process()
    return JsonResponse({'process': 'SUCCESS'})