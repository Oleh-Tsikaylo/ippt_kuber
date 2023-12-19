from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Jeweller)
admin.site.register(Order)
admin.site.register(CompletedProduct)
admin.site.register(UsedMaterials)
