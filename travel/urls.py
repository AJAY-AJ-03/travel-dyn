from django.urls import path
from . import views
from django.conf.urls.static import static
from django.urls import include, path
from django.contrib import admin



urlpatterns = [
    path('', views.index, name='index'),  # Maps the home page to index view
    path('about.html', views.about, name='about'),  # Maps the home page to index view
    path('deals.html', views.deals, name='deals'),  # Maps the home page to index view
    # path('travels/', views.travels, name='travels'),  # Maps the home page to index view
    path('travels/', views.travel_list, name='travels'),
    path('reservation.html', views.reservation, name='reservation'),  # Maps the home page to index view
    path('admin/', admin.site.urls),
]
