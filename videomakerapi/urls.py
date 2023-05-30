# urls.py
from django.urls import path
from api.views import (
    AudioBlockListAPIView,
    AudioBlockCreateAPIView,
    AudioBlockRetrieveAPIView,
    AudioBlockUpdateAPIView,
    AudioBlockDeleteAPIView,
    AudioFragmentAPIView,
)

urlpatterns = [
    path('audio-blocks/', AudioBlockListAPIView.as_view(), name='audio-blocks-list'),
    path('audio-blocks/create/', AudioBlockCreateAPIView.as_view(), name='audio-blocks-create'),
    path('audio-blocks/<int:pk>/', AudioBlockRetrieveAPIView.as_view(), name='audio-blocks-retrieve'),
    path('audio-blocks/<int:pk>/update/', AudioBlockUpdateAPIView.as_view(), name='audio-blocks-update'),
    path('audio-blocks/<int:pk>/delete/', AudioBlockDeleteAPIView.as_view(), name='audio-blocks-delete'),
    path('audio-fragments/', AudioFragmentAPIView.as_view(), name='audio-fragments-list'),
]
