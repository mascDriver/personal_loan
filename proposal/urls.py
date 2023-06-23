from django.urls import path

from .views import *

urlpatterns = [
    path('', CreateProposal.as_view()),
]
