from django.contrib import admin

from .models import Book, Request

# added this for my own dev purposes, not explicitly part of the spec
admin.site.register(Book)
admin.site.register(Request)