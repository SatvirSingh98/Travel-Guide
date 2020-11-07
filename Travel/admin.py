from django.contrib import admin
from .models import Destination, DestDescription


# Register your models here.
class DestDescriptionAdmin(admin.StackedInline):
    model = DestDescription


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    inlines = [DestDescriptionAdmin]

    class Meta:
       model = Destination


@admin.register(DestDescription)
class DestDescriptionAdmin(admin.ModelAdmin):
    pass