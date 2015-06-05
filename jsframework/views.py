from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'jsframework/index.html')

def base(request):
	return render(request, 'jsframework/base.html')