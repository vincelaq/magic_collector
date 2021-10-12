from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    # Card Routes
    path('cards/', views.CardList.as_view(), name="card_list"),
    path('cards/new/', views.CardCreate.as_view(), name="card_create"),
    path('cards/<int:pk>/', views.CardDetail.as_view(), name="card_detail"),
    path('cards/<int:pk>/update/', views.CardUpdate.as_view(), name="card_update"),
    path('cards/<int:pk>/delete/', views.CardDelete.as_view(), name="card_delete"),
    # Deck Routes
    path('decks/<int:pk>/cards/<int:card_pk>/', views.DeckCardAssoc.as_view(), name="deck_card_assoc"),
]
