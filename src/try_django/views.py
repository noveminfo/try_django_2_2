from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

def home_page(request):
	my_title = "Hello there...."
	return render(request, "hello_world.html", {"title": my_title})


def about_page(request):
	# my_title = "Hello there...."
	return render(request, "about.html", {"title": "About Us"})

def contact_page(request):
	return render(request, "hello_world.html", {"title": "Contact Us"})

def example_page(request):
	context = {"title": "Example"}
	template_name = "hello_world.html"
	template_obj = get_template(template_name)
	rendered_string = template_obj.render(context)
	print(rendered_string)
	return HttpResponse(rendered_string)
	