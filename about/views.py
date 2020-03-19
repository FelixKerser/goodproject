from django.shortcuts import render
from .models import Info

def info_site(request):
	infos = Info.objects.all()
	return render(request, 'about/info_site.html', {'infos': infos})