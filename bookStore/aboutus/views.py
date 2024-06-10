from django.shortcuts import render
from django.http import HttpResponse

import json

# Create your views here.
def aboutus(request):
    # return template ?
    return render(request, "index.html")