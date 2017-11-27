import random
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

# # Create your views here.
# def home_old(request):

# 	html_var = 'Django'
# 	html_ = f"""
# 		<!doctype html>
# 		<html lang="en">
# 		  	<head>
# 				<title>My Django App</title>
# 			</head>
# 			<body>
# 				<h1><p>My {html_var} App</p></h1>
# 		  	</body>
# 		</html>
# 	"""
# 	#f strings
# 	return HttpResponse(html_)
# 	#return render (request, "home.html", {}) #response

# def home(request):
# 	html_var = 'Django'
# 	num=None
	
# 	some_list = [random.randint(0,10000000), random.randint(0,10000000), random.randint(0,10000000)]
# 	condition_bool_item  = True

# 	if condition_bool_item:
# 		num = random.randint(0,10000000)
# 	context = {
# 				"html_var":html_var, 
# 				"num":num,
# 				"some_list":some_list
# 				}
# 	return render (request, "home.html", context)  #response

# def about(request):
# 	html_var = 'Django'
# 	context = {
# 				"html_var":html_var
# 				}
# 	return render (request, "about.html", context)  #response

# def contact(request):
# 	html_var = 'Django'
# 	context = {
# 				"html_var":html_var
# 				}
# 	return render (request, "contact.html", context)  #response


# class ContactView(View):
# 	def get(self, request, *args, **kwargs):
# 		html_var = 'Django'
# 		context = {
# 				"html_var":html_var
# 				}
# 		return render (request, "contact.html", context)  #response

# class AboutView(View):
# 	def get(self, request, *args, **kwargs):
# 		html_var = 'Django'
# 		# print(kwargs)
# 		context = {
# 				"html_var":html_var
# 				}
# 		return render (request, "about.html", context)  #response

	# def post(self, request, *args, **kwargs):
	# 	html_var = 'Django'
	# 	# print(kwargs)
	# 	context = {
	# 			"html_var":html_var
	# 			}
	# 	return render (request, "about.html", context)  #response

	# def put(self, request, *args, **kwargs):
	# 	html_var = 'Django'
	# 	# print(kwargs)
	# 	context = {
	# 			"html_var":html_var
	# 			}
	# 	return render (request, "about.html", context)  #response

class HomeView(TemplateView):
	template_name = 'home.html'

	def get_context_data(self, *args, **kwargs):
		context = super(HomeView, self).get_context_data(*args, **kwargs)
		html_var = 'Django'
		num=None
		
		some_list = [random.randint(0,10000000), random.randint(0,10000000), random.randint(0,10000000)]
		condition_bool_item  = True

		if condition_bool_item:
			num = random.randint(0,10000000)
		context = {
					"html_var":html_var, 
					"num":num,
					"some_list":some_list
					}
		return context

class AboutView(TemplateView):
	template_name = 'about.html'
	def get_context_data(self, *args, **kwargs):

		context = super(AboutView, self).get_context_data(*args, **kwargs)
		html_var = 'Django'
		context = {"html_var":html_var}
		return context

class ContactView(TemplateView):
	template_name = 'contact.html'
	def get_context_data(self, *args, **kwargs):

		context = super(ContactView, self).get_context_data(*args, **kwargs)
		html_var = 'Django'
		context = {"html_var":html_var}
		return context