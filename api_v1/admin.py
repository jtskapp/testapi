from django.contrib import admin
from .models import Customer

class CreatedDate(admin.ModelAdmin):
    readonly_fields = ('created',)

# Register your models here.
admin.site.register(Customer, CreatedDate)