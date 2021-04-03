from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def index(request):
    if request.method == 'GET':
        return JsonResponse({"req_method":"get"}, status=200)
    elif request.method == 'POST':
        return JsonResponse({"req_method":"post"}, status=200)
    else:
        return JsonResponse({"error": "request method not allowed"}, status=405)
    #return HttpResponse("aaaa")