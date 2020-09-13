from django.shortcuts import render
from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    DetailView,
    UpdateView
)
from .models import Tweet
# Create your views here.

class TweetListView(ListView):
    model = Tweet
    template_name = 'tweet/tweet_list.html'
    context_object_name = 'tweets'

    def get_queryset(self):
        query = Tweet.objects.all()
        return query

class TweetDetailView(DetailView):
    model = Tweet

class TweetCreateView(CreateView):
    model = Tweet

class TweetDeleteView(DeleteView):
    model = Tweet

class TweetUpdateView(UpdateView):
    model = Tweet