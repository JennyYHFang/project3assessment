from django.shortcuts import render, redirect
from .models import Wishitem
from django.views.generic.edit import CreateView, DeleteView

# Create your views here.
def home(request):
    return render(request, 'home.html')


class WishitemAdd(CreateView):
    model = Wishitem
    fields = ['description']

class WishitemDelete(DeleteView):
    model = Wishitem
