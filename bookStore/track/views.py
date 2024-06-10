from django.shortcuts import render

from django.http import HttpResponse



def track_landing(request):
    return HttpResponse('Track landing page ')


def tracks_index(request):
    return render(request, 'landing.html')