from django.shortcuts import render
from .models import Image

# Create your views here.
def home(request):
	image_queryset = Image.objects.all()
	context = {
		"images": image_queryset,
	}
	return render(request, "index.html", context)