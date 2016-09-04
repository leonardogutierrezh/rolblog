from django.conf.urls import url
from .views import (
    IndexView, ParaHumanDetailView, EntranceDetailView,
    EntrancesListView,
)


urlpatterns = [
    url(
        r'^$',
        IndexView.as_view(), name='index'
    ),
    url(
        r'^entrances/$',
        EntrancesListView.as_view(), name='entrances'
    ),
    url(
        r'^(?P<pk>[0-9]+)/$',
        ParaHumanDetailView.as_view(), name='parahuman'
    ),
    url(
        r'^entrance/(?P<pk>[0-9]+)/$',
        EntranceDetailView.as_view(), name='entrance'
    ),
]
