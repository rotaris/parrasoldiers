from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Soldier
from django.shortcuts import render
from django.conf import settings

def all_soldiers(request):
    s = Soldier.objects.exclude(unique_id__in=settings.LIST_OF_MISSING_SOLDIER_PHOTOS).order_by("unique_id")[:18]
    soldiers = [(s_, s_.get_photo_url()) for s_ in s]
    #soldiers = s
    context = {'soldiers': soldiers}
    #print(s)
    return render(request, 'all_soldiers.html', context)

def soldier_detail(request, unique_id):
    s = get_object_or_404(Soldier, unique_id=unique_id)
    return render(request, 'soldier_detail.html', {'soldier': s, 'photo_url': s.get_photo_url()})

def soldier_records(request, unique_id):
    s = get_object_or_404(Soldier, unique_id=unique_id)
    return render(request, 'soldier_records.html', {'soldier': s, 'photo_url': s.get_photo_url()})
