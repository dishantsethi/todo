from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

# Create your views here.
# @csrf_exempt
# @api_view(["GET"])
def list(request):
    return render(request, 'frontend/list.html')