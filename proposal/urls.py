from django.urls import path

from .views import *

urlpatterns = [
    path('api/proposal/', CreateProposal.as_view()),
]
