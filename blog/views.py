from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, permissions
from rest_framework.permissions import AllowAny
from django.db.models import Q

from .models import Blog
from .serializer import BlogSerializer


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [AllowAny]

def blog_list_view(request):
    query = request.GET.get('q')
    if query:
        posts = Blog.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query),
            is_published=True
        ).order_by('-created_date')
    else:
        posts = Blog.objects.filter(is_published=True).order_by('-created_date')

    return render(request, 'blog_list.html', {'posts': posts, 'query': query})


def post_detail_view(request, pk):
    post = get_object_or_404(Blog, pk=pk, is_published=True)
    return render(request, 'post_detail.html', {'post': post})
