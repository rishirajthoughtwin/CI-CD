from django.http import HttpResponse


def ping(request):
    data = "data"
    return HttpResponse(data)