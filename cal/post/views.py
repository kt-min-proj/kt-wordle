from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view


@csrf_exempt
def calendar_view(request):
    if request.method == "POST":
        print("This is Post")
    # TODO 요청값 dict로 뽑아내기
    json = {"hello": "123"}
    return JsonResponse(json)
