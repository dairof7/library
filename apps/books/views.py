from django.shortcuts import render
from rest_framework.views import APIView
from django.db.models import F

from rest_framework import viewsets
from apps.users import serializers
from apps.users.views import GeneralApiView
from .models import Author, Book
from django.http import Http404
from .serializers import AuthorSerializer, BookSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
# from books import serializers

class AuthorsList(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]
    """View a complete Author list

    * Requires: token authentication
    * Any user can access
    """
    def get(self, request, format=None):
        authors = Author.objects.all()
        authors_serialized = AuthorSerializer(authors, many=True)
        return Response(authors_serialized.data)

    def post(self, request, format=None):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AuthorDetailView(APIView):
    """View a Author detail

    * Requires: token authentication
    * Any user can access
    """
    def get(self, request, pk=None, format=None):
        
        author = Author.objects.get(id=pk)
        author_serialized = AuthorSerializer(author, many=False)
        return Response(author_serialized.data)

    def put(self, request, pk=None):

        try:
            author = Author.objects.get(id=pk)
        except Author.DoesNotExist:
            author = None
            # raise Http404("Poll does not exist")
            return Response({'message':'Id do no exist'}, status=status.HTTP_404_NOT_FOUND)
        author_serializer = AuthorSerializer(author, data=request.data)
        if author_serializer.is_valid():
            author_serializer.save()
            return Response(author_serializer.data)
        return Response(author_serializer.errors)


    def delete(self, request, pk=None):

        try:
            author = Author.objects.get(id=pk)
            author.delete()
            return Response({'message':'deleted'}, status=status.HTTP_404_NOT_FOUND)
        except Author.DoesNotExist:
            author = None
            return Response({'message':'Id do no exist'}, status=status.HTTP_404_NOT_FOUND)
 

class BooksListView(GeneralApiView):
    serializer_class = BookSerializer

# this view can be used to list and create
class BooksCreateView(generics.ListCreateAPIView):
    serializer_class = BookSerializer 
    queryset = BookSerializer.Meta.model.objects.all()
    # intercept the post before response
    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'done'})
        return Response(serializer.errors)

class BooksRetrieveApiView(generics.RetrieveAPIView):
    serializer_class = BookSerializer 
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()

    # using manual get overwriting get method, its just alternative
    # def get(self, request, pk):
    #     resp = self.get_queryset().get(id=pk)
    #     resp = self.serializer_class(resp).data
    #     return Response(resp)

class BooksDeleteApiView(generics.DestroyAPIView):
    serializer_class = BookSerializer 
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()
    
    # in this case only deactivate a book this could be mean book desapear for user but not from DB
    def delete(self, request, pk=None):    
        book = self.get_queryset().filter(id=pk).first()
        if book:
            book.is_available = False
            book.save()
            return Response({'message': 'Deactivated'}, status=status.HTTP_200_OK)
        return Response({'message': 'Product not found'}, status=status.HTTP_400_BAD_REQUEST)


class BookUpdateApiView(generics.UpdateAPIView):
    serializer_class = BookSerializer 
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()
# class BooksListView(APIView):
    
#     def get(self, request):
#         books = Book.objects.all()
#         books = books.values(
#             'id',
#             'author__full_name',
#             author_name=F('author__full_name')
#         )
#         return Response(books)

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = BookSerializer.Meta.model.objects.all()