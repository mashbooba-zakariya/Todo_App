from django.contrib import admin

from todoapp import models

# Register your models here.
# class todoAdmin(admin.ModelAdmin):
    # list_display = ('title','date')

admin.site.register(models.todo)
