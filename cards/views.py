# cards/views.py
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.shortcuts import get_object_or_404, redirect
from .forms import CardCheckForm

from .models import Card
import random
from .forms import GPTCreateForm
from django.views.generic.edit import FormView

class CardDeleteView(DeleteView):
    model = Card
    success_url = reverse_lazy('card-list')  
    template_name = 'cards/card_confirm_delete.html'  

class CardListView(ListView):
    model = Card
    template_name = 'cards/card_list.html'  # Update with your correct template path

    def get_queryset(self):
        sort_by = self.request.GET.get('sort_by', 'box')
        if sort_by == 'topic':
            return Card.objects.all().order_by('topic')
        else:  # Default to sorting by box
            return Card.objects.all().order_by('box')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sort_by = self.request.GET.get('sort_by', 'box')
        context['show_box'] = sort_by != 'topic'

        if sort_by == 'topic':
            cards_grouped = {}
            for card in self.get_queryset().order_by('topic'):
                cards_grouped.setdefault(card.topic, []).append(card)
            context['cards_grouped'] = cards_grouped
        else:
            context['easy_cards'] = Card.objects.filter(box='Easy').order_by('topic')
            context['medium_cards'] = Card.objects.filter(box='Medium').order_by('topic')
            context['hard_cards'] = Card.objects.filter(box='Hard').order_by('topic')

        return context
class CardCreateView(CreateView):
    model = Card
    fields = ["question", "answer", "box", "topic"]
    success_url = reverse_lazy("card-create")

class GPTCreateView(FormView):
    template_name = 'cards/gpt_create.html'
    form_class = GPTCreateForm
    success_url = reverse_lazy('some-success-view')  # Update with your success URL

    def form_valid(self, form):
        # Process the data in form.cleaned_data
        topic = form.cleaned_data['topic']
        number_of_cards = form.cleaned_data['number_of_cards']

        # Logic to generate flashcards goes here

        return super().form_valid(form)  # Redirects to success_url

class CardUpdateView(CardCreateView, UpdateView):
    success_url = reverse_lazy("card-list")

class BoxView(CardListView):
    template_name = "cards/box.html"
    form_class = CardCheckForm

    def get_queryset(self):
        return Card.objects.filter(box=self.kwargs["box_name"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["box_name"] = self.kwargs["box_name"]
        if self.object_list:
            context["check_card"] = random.choice(self.object_list)
        return context
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            card = get_object_or_404(Card, id=form.cleaned_data["card_id"])
            card.move(form.cleaned_data["solved"])

        return redirect(request.META.get("HTTP_REFERER"))

class TopicView(ListView):
    template_name = "cards/topic.html"  # You might need to create this template
    form_class = CardCheckForm

    def get_queryset(self):
        return Card.objects.filter(topic=self.kwargs["topic_name"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["topic_name"] = self.kwargs["topic_name"]
        if self.object_list:
            context["check_card"] = random.choice(self.object_list)
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            card = get_object_or_404(Card, id=form.cleaned_data["card_id"])
            card.move(form.cleaned_data["solved"])
        return redirect(request.META.get("HTTP_REFERER"))