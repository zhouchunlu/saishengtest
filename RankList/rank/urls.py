from django.conf.urls import url
from rank.views import RankView

app_name = "rank"

urlpatterns = [
    url('^rank', RankView.as_view(), name='rank')
]
