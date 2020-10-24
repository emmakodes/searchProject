from django.shortcuts import render
from .models import Pet
from .filters import PetFilter


# Create your views here.
def index(request):
    myFilter = PetFilter(request.GET, queryset=Pet.objects.all())
    pets = myFilter.qs

    context = {
        'pets': pets,
    }
    return render(request, 'projx.html', context)

