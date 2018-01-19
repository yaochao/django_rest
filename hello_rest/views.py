from django.shortcuts import render
from hello_rest.models import Book
from hello_rest.serializers import BookSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status

# Create your views here.
class BookList(APIView):
    def get(self, request, format=None):
        books = Book.objects.all()
        ser = BookSerializer(books, many=True)
        return Response(ser.data)

    def post(self, request, format=None):
        ser = BookSerializer(data=request.data)
        if ser.is_valid():
            ser.create(ser.validated_data).save()
            return Response(ser.data, status.HTTP_201_CREATED)
        return Response(ser.errors)

class BookDetail(APIView):
    def get(self, request, book_id, format=None):
        book = Book.objects.get(id=book_id)
        ser = BookSerializer(book)
        print ser
        return Response(ser.data)

class GenericBookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    def post(self, request, *args, **kwargs):
        ser = BookSerializer(data=request.data)
        if ser.is_valid():
            ser.create(ser.validated_data).save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors)

