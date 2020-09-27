from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

class BookView(GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def post(self, request, *args, **kwargs):
        cover = request.data['cover']
        title = request.data['title']
        Book.objects.create(title=title, cover=cover)
        return Response({'message':'created'}, status=201)

    def get(self, request, *args, **kwargs):
        book = Book.objects.all()
        serializer = BookSerializer(book, many = True)
        return Response({'data':serializer.data, 'status':200})