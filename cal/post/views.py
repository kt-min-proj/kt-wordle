import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view


@csrf_exempt
@api_view(["POST"])
def calendar_view(request):
    json_data = json.loads(request.body)
    return JsonResponse(json_data)
