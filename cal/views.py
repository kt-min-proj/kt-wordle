from django.shortcuts import render

# Create your views here.
def index(request):
    print(request.POST.get("my_date_field"))
    return render(
        request=request,
        template_name="calendar.html",
        context={},
    )
