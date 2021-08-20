from django.contrib import admin

# Register your models here.
from . models import Action, ActionName, CategoryName


admin.site.register(Action)
admin.site.register(ActionName)
admin.site.register(CategoryName)
