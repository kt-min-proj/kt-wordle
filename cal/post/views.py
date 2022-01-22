from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view


@csrf_exempt
def calendar_view(request):
    # output = Calendar.objects.all()
    # output_json = serializers.serialize("json", output)
    # print(output_json)
    return JsonResponse(
        """
    {"date":"123"}
        """
    )
