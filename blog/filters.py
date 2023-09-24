import django_filters
from django_filters import CharFilter
from .models import Blog


class BlogFilter(django_filters.FilterSet):
    class Meta:
        model = Blog
        fields = ['category',]

    title = CharFilter(field_name='title', lookup_expr='icontains')
    content = CharFilter(field_name='content', lookup_expr='icontains')

