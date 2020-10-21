from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django.views.generic import ListView, DetailView, CreateView
from django.views import View


from .models import *
from .forms import *






def index(request):
    return render(request, "auctions/index.html", {
        "listings": Listings.objects.all()
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")



def create(request):
    form = NewListingForm()
    if request.method == "POST":
        form = NewListingForm(request.POST)
        if form.is_valid():
            print("form is valid")
            obj = form.save()
            print(f"esto es obj {obj}")
            return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/create.html", {
        'form': form
    })


def listing(request, listing_id):
    listing = Listings.objects.get(listing_id=listing_id)
    return render(request, "auctions/listing.html", {
        "listing": listing, 
    })    


class AddCommentView(CreateView):
    model = Comments
    template_name = 'listing.html'
    fields = ['__all__']

class commentsView(ListView):
    model = Comments
    template_name = 'listing.html'
    

class AddListingView(CreateView):
    model = Listings
    template_name = 'add_listing.html'
    fields = ['title', 'description', 'startingbid', 'image', 'category']