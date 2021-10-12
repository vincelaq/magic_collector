from django.shortcuts import render, redirect, reverse
from django.views import View
from django.views.generic import DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from .models import Card, Deck


# Create your views here.
class Home(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["decks"] = Deck.objects.all()
        return context

class About(TemplateView):
    template_name = "about.html"

class CardList(TemplateView):
    template_name = "cards/card_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["cards"] = Card.objects.filter(name__icontains=name)
            context["header"] = f"Searching for {name}"
        else:
            context["cards"] = Card.objects.all()
            context["header"] = "Trending Cards"
        return context

class CardCreate(CreateView):
    model = Card
    fields = ['name', 'image', 'text', 'card_type']
    template_name = "cards/card_create.html"
    
    def set_success_url(self):
        return reverse('card_detail', kwargs={'pk': self.object.pk})         

class CardDetail(DetailView):
    model = Card
    template_name = "cards/card_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["decks"] = Deck.objects.all()
        return context
    

class CardUpdate(UpdateView):
    model = Card
    fields = ['name', 'image', 'text', 'card_type']
    template_name = "cards/card_update.html"
    
    def set_success_url(self):
        return reverse('card_detail', kwargs={'pk': self.object.pk})  

class CardDelete(DeleteView):
    model = Card
    template_name = "cards/card_delete_confirm.html"
    success_url = "/cards/"

class DeckCardAssoc(View):

    def get(self, request, pk, card_pk):
        assoc = request.GET.get("assoc")
        if assoc == "remove":
            Deck.objects.get(pk=pk).cards.remove(card_pk)
        if assoc == "add":
            Deck.objects.get(pk=pk).cards.add(card_pk)
        return redirect("home")