import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def calendar_view(request):
    json_data = json.loads(request.body)
    return JsonResponse(json_data)
