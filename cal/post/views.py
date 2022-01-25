import json
from datetime import datetime

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import *

json_false_data = {"data": None, "answer": "Today's answer"}


@csrf_exempt
def calendar_view(request):
    json_data = json.loads(request.body)
    _date = datetime.today().strftime("%Y-%m-%d")
    values = Calendar.objects.filter(date=json_data["date"])
    for i in values:
        json_data["answer"] = i.answer
    if json_data["date"] == str(_date):
        return JsonResponse(json_false_data)
    return JsonResponse(json_data)
