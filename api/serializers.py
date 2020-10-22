from rest_framework import serializers
from .models import Book, Request

class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'available')

class RequestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Request
        fields = ('id', 'book_id', 'email', 'created_at')