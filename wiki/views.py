from django.views import generic
from .models import ParaHuman, Entrance

# Create your views here.


class IndexView(generic.ListView):
    model = ParaHuman
    template_name = 'index.html'
    queryset = ParaHuman.objects.all()
    template_name_suffix = 'parahuman_list'


class ParaHumanDetailView(generic.DetailView):
    model = ParaHuman
    template_name = 'parahuman.html'


class EntranceDetailView(generic.DetailView):
    model = Entrance
    template_name = 'entrance.html'


class EntrancesListView(generic.ListView):
    model = Entrance
    template_name = 'entrances_list.html'

