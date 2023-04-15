from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='chat'),
    path("room/<str:room_name>/", views.Roomview.as_view(), name="room"),
]