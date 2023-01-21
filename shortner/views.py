from django.shortcuts import render, redirect
import uuid
from .models import Url
from django.http import HttpResponse

def index(request):
  return render(request, 'index.html')

def create(request):
  if request.method == 'POST':
    link = request.POST['link']
    uid = str(uuid.uuid4())[:5]
    new_url = Url(link=link, uuid=uid)
    new_url.save()
    return HttpResponse(uid)
  
def go(request, pk):
  url_datails = Url.objects.get(uuid=pk)
  print(url_datails.link)
  return redirect(url_datails.link)
