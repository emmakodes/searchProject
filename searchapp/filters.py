import django_filters
from .models import Pet
from django_filters import CharFilter


class PetFilter(django_filters.FilterSet):
    pet_name = CharFilter(field_name='pet_name',
                          lookup_expr='icontains')

    class Meta:
        model = Pet
        fields = ['pet_name']
