import json
import os
import sys
from datetime import datetime

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

from master_user.models import WordleAnswers, WordleDayRanks, WordleUser

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

json_false_data = {
    "data": None,
    "answer": "Today's answer",
}


@csrf_exempt
@api_view(["POST"])
def calendar_view(request):
    json_data = json.loads(request.body)
    _date = datetime.today().strftime("%Y-%m-%d")

    values = WordleAnswers.objects.filter(date=json_data["date"])

    for i in values:
        json_data["answer"] = i.answer
        json_data["rank"] = calendar_rank(json_data["rank"])
    if json_data["date"] == str(_date):
        return JsonResponse(json_false_data)

    return JsonResponse(json_data)


def calendar_rank(data: dict):
    for i in range(10):
        d = WordleDayRanks.objects.filter(user_rank=i)
        # NOTE WordleUser 모델을 불러 와야 할것 같음
        data[f"{i}"] = []
        for ii in d:
            data[f"{i}"].append(ii.user_rank)
            data[f"{i}"].append(ii.user_id)
            a = WordleUser.objects.select_related('user_id')
            print(a)
            # for iii in a: print(iii)
            # data[f"{i}"].append()

    return data
