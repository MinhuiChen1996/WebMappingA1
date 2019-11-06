from django.shortcuts import render
from django.views import generic
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from .models import Shop

# Create your views here.
# def index(request):
#   return render(request,"index.html")
longitude = -53.350403
latitude = 6.264477

user_location = Point(longitude, latitude, srid=4326)


class Home(generic.ListView):
    model = Shop
    context_object_name = 'WebMap'
    queryset = Shop.objects.annotate(distance=Distance('shopLocation', user_location)
                                     ).order_by('distance')[0:6]
    template_name = 'WebMap/index.html'
