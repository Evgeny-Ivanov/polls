from django.conf.urls import url, include
from . import views

question_urls = [
    url(r'^/(?P<pk>[0-9a-zA-Z_-]+)$', views.QuestionDetail.as_view(), name='question_detail'),
]

choice_urls = [
    url(r'^/(?P<pk>[0-9a-zA-Z_-]+)$', views.ChoiceDetail.as_view(), name='choice_detail'),
]


app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^auth/$', views.authorization, name='auth'),
    url(r'^question', include(question_urls)),
    url(r'^choice', include(choice_urls)),
]
