import django_filters
from .models import Sermon
from django_filters import FilterSet
from django.db.models import Q

class SermonFilter(FilterSet):
    search = django_filters.CharFilter(method='filter_by_all')

    def filter_by_all(self, queryset, name, value):
        term = value.strip().split()
        for terms in term:
            return queryset.filter(
                Q(title__icontains=terms)|
                Q(preacher__icontains=terms)|
                Q(scripture_references__icontains=terms)
            )
    
    tags = django_filters.CharFilter(lookup_expr='iexact',field_name='tags')
    class Meta:
        model = Sermon
        fields = ['search','tags']