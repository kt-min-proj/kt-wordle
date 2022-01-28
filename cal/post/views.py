import json
from datetime import datetime

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

from master_user.models import WordleAnswers, WordleRanks
from member.models import WordleUser

json_false_data = {
    "data": None,
    "answer": "Today's answer",
}

WA = WordleAnswers.objects
WDR = WordleRanks.objects
WU = WordleUser.objects


@csrf_exempt
@api_view(["POST"])
def calendar_view(request):
    json_data = json.loads(request.body)
    _date = datetime.today().strftime("%Y-%m-%d")

    for i in WA.filter(date=json_data["date"]).values("answer"):
        json_data["answer"] = i["answer"]
        json_data["rank"] = calendar_rank(
            json_data["rank"],
        )
    if json_data["date"] == str(_date):
        return JsonResponse(json_false_data)

    return JsonResponse(json_data)


def calendar_rank(data: dict):
    for i in range(10):
        """
        :return username, user_id, account_id
        """
        data[f"{i}"] = []

        # TODO fix using comprehension
        for ia in WDR.filter(user_rank=i).values(
            "user_id",
            "user",
        ):
            for ib in WU.filter(id=ia["user"]).values(
                "user_name",
                "user_id",
            ):
                data[f"{i}"].append(ib["user_name"])
                # data[f"{i}"].append(ia["user_id"]) # NOTE Think don't need
                data[f"{i}"].append(ib["user_id"])
    return data
  
# def timeconvert(date):
#     result = datetime.strptime(date, "%Y-%m-%d").strftime("%Y-%m-%d 00:00:00")
#
#     return result
