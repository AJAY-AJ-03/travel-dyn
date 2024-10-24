from django.contrib import admin
from .models import Travels

@admin.register(Travels)
class TravelsAdmin(admin.ModelAdmin):
    list_display = ('place', 'country', 'people', 'distance', 'price')  # Display these fields in the list view
    search_fields = ('place', 'country')  # Add search functionality by place and country
    list_filter = ('country', 'price')  # Filter options for country and price
