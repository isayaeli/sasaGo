from django.shortcuts import render
from .models import Vehicle


def home(request):
	queryset = Vehicle.objects.filter()
	context = {
		'vehicles': queryset
	}
	return render(request, 'home/home.html', context=context)
