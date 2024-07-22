import django_filters
from .models import ApartmentModel
from django.utils.timezone import now

class RoomFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name='price_per_night', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price_per_night', lookup_expr='lte')
    min_capacity = django_filters.NumberFilter(field_name='capacity', lookup_expr='gte')
    max_capacity = django_filters.NumberFilter(field_name='capacity', lookup_expr='lte')
    start_date = django_filters.DateFilter(field_name='bookings__rent_start', lookup_expr='gte')
    end_date = django_filters.DateFilter(field_name='bookings__rent_end', lookup_expr='lte')

    class Meta:
        model = ApartmentModel
        fields = ['min_price', 'max_price', 'min_capacity', 'max_capacity', 'start_date', 'end_date']

    def filter_by_date(self, queryset, name, value):
        if name == 'start_date':
            return queryset.exclude(bookings__rent_start__lte=value, bookings__rent_end__gte=value)
        if name == 'end_date':
            return queryset.exclude(bookings__rent_start__lte=value, bookings__rent_end__gte=value)
        return queryset
