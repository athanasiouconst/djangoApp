from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from .forms import RestaurantCreateForm, RestaurantLocationCreateForm
from .models import RestaurantLocation


def restaurant_createview(request):
    form = RestaurantLocationCreateForm(request.POST or None)
    errors = None
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/restaurants/")
    if form.errors:
        errors = form.errors
           
    template_name = 'restaurants/form.html'
    context = {"form": form, "errors": errors}
    return render(request, template_name, context)


def restaurant_listview(request, ):
    template_name = 'restaurants/restaurants_list.html'
    queryset = RestaurantLocation.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, template_name, context)


def restaurant_detailview(request, slug):
    template_name = 'restaurants/restaurantlocation_detail.html'
    obj = RestaurantLocation.objects.get(slug=slug)
    context = {
        "object": obj
    }
    return render(request, template_name, context)


class RestaurantListView(ListView):
    def get_queryset(self):
        slug = self.kwargs.get("slug")
        if slug:
            queryset = RestaurantLocation.objects.filter(
                Q(category__iexact=slug) |
                Q(category__icontains=slug)
            )
        else:
            queryset = RestaurantLocation.objects.all()
        return queryset


class RestaurantDetailView(DetailView):
    queryset = RestaurantLocation.objects.all() #.filter(category_iexact = 'asian') #filter by user

    # def get_object(self, *args, **kwargs):
    #     rest_id = self.kwargs.get('rest_id')
    #     obj = get_object_or_404(RestaurantLocation, id=rest_id) # pk = rest_id
    #     return obj


class RestaurantCreateView(CreateView):
	form_class    = RestaurantLocationCreateForm
	template_name = 'restaurants/form.html'
	success_url = "/restaurants/"




    # class SearchRestaurantListView(ListView):
    # 	template_name='restaurants/restaurants_list.html'

    # 	def get_queryset(self):
    # 		print(self.kwargs)
    # 		slug = self.kwargs.get("slug")
    # 		if slug:
    # 			queryset = RestaurantLocation.objects.filter(
    # 					Q(category__iexact=slug) |
    # 					Q(category__icontains=slug)
    # 				)
    # 		else:
    # 			queryset = RestaurantLocation.objects.none
    # 		return queryset

    # class MexicanRestaurantListView(ListView):
    # 	queryset = RestaurantLocation.objects.filter(category__iexact='Mexican')
    # 	template_name='restaurants/restaurants_list.html'

    # class AsianFusionRestaurantListView(ListView):
    # 	queryset = RestaurantLocation.objects.filter(category__iexact='Asian Fusion')
    # 	template_name='restaurants/restaurants_list.html'


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

    # class HomeView(TemplateView):
    # 	template_name = 'home.html'

    # 	def get_context_data(self, *args, **kwargs):
    # 		context = super(HomeView, self).get_context_data(*args, **kwargs)
    # 		html_var = 'Django'
    # 		num=None

    # 		some_list = [random.randint(0,10000000), random.randint(0,10000000), random.randint(0,10000000)]
    # 		condition_bool_item  = True

    # 		if condition_bool_item:
    # 			num = random.randint(0,10000000)
    # 		context = {
    # 					"html_var":html_var,
    # 					"num":num,
    # 					"some_list":some_list
    # 					}
    # 		return context

    # class AboutView(TemplateView):
    # 	template_name = 'about.html'
    # 	def get_context_data(self, *args, **kwargs):

    # 		context = super(AboutView, self).get_context_data(*args, **kwargs)
    # 		html_var = 'Django'
    # 		context = {"html_var":html_var}
    # 		return context

    # class ContactView(TemplateView):
    # 	template_name = 'contact.html'
    # 	def get_context_data(self, *args, **kwargs):

    # 		context = super(ContactView, self).get_context_data(*args, **kwargs)
    # 		html_var = 'Django'
    # 		context = {"html_var":html_var}
    # 		return context
