from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from .serializers import BookSerializer, RequestSerializer
from .models import Book, Request


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('id')
    serializer_class = BookSerializer


class RequestViewSet(viewsets.ModelViewSet):

    queryset = Request.objects.all().order_by('id')
    serializer_class = RequestSerializer

    def create(self, request):

        try:
            book_title = request.data['title']
            email = request.data['email']

            book = Book.objects.get(title=book_title)

            request = Request.objects.create(book=book, email=email)
            return Response({"id": book.id, "title": book.title, "available": book.available, "timestamp": request.created_at})

        except:
            return Response(status=status.HTTP_204_NO_CONTENT)
