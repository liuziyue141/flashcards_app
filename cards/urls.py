# cards/urls.py

from django.urls import path
#from django.views.generic import TemplateView
from . import views


urlpatterns = [
    path(
        "",
        views.CardListView.as_view(),
        name="card-list"
    ),
    path(
        "new",
        views.CardCreateView.as_view(),
        name="card-create"
    ),
    path(
        "edit/<int:pk>",
        views.CardUpdateView.as_view(),
        name="card-update"
    ),
    path(
        "box/<str:box_name>",
        views.BoxView.as_view(),
        name="box"
    ),
    path(
        'card/delete/<card_id>/',
        views.delete,
        name='card-delete'
    ),
    path(
        'gpt-create',
        views.GPTCreateView.as_view(),
        name="GPT-card-creation",
    ),
    path(
        'topic/<str:topic_name>/', 
        views.TopicView.as_view(),
        name='topic-view',
    ),

    path(
        'review_new', 
        views.review_new,
        name='review-new',
    ),

    path(
        'get_report',
        views.get_report,
        name = 'get-report',
    ),



]
