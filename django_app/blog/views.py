from rest_framework import generics

from blog.models import Blog
from blog.serializers import BlogSerializer

class ListBlog(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class =  BlogSerializer

class DetailBlog(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    
