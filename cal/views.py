from re import template
from django.shortcuts import render

# Create your views here.
def index(request):
    print(request.body)
    a = request.POST.get("date")
    return render(
        request=request,
        template_name="calendar.html",
        context={"data": a},
    )


def cal(request):
    return render(
        request=request,
        template_name="cal.html",
        context={},
    )
