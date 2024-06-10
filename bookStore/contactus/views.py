from django.shortcuts import render
from django.http import HttpResponse

import json

# Create your views here.
def contact(request):
    # return template ?
    return render(request, "contact.html")