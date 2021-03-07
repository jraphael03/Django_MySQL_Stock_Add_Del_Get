from django.contrib import admin
from .models import Stock       # import from models (the name of the model you want to import)

# THIS IS USED TO DISPLAY YOUR MODELS IN THE DJANGO ADMIN PANEL
admin.site.register(Stock)
