import random
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_old(request):

	html_var = 'Django'
	html_ = f"""
		<!doctype html>
		<html lang="en">
		  	<head>
				<title>My Django App</title>
			</head>
			<body>
				<h1><p>My {html_var} App</p></h1>
		  	</body>
		</html>
	"""
	#f strings
	return HttpResponse(html_)
	#return render (request, "home.html", {}) #response

def home(request):
	num = random.randint(0,10000000)
	return render (request, "base.html", {"html_var":"Django", "num":num}) #response