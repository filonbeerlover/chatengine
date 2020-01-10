from django.shortcuts import render

def themes_list(request):
	return render(request,'themes/themes.html')