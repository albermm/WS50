from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django.views.generic import ListView, DetailView, CreateView
from django.views import View
from django.db.models import Max


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
    if request.method == "POST":
        obj = Bids()
        obj.username = request.user
        obj.listing = Listings.objects.get(listing_id=listing_id)
        obj.amount = request.POST.get('bid_amount')
        bidlist = Bids.objects.filter(listing_id = listing_id).aggregate(Max('amount'))
        print(f"bidlist es {bidlist},")
        currentbid = int(request.POST.get('bid_amount'))
        maxbid = int(bidlist['amount__max'])
        startingbid = int(listing.startingbid)
        print(f"bidlist es {maxbid}, start bid is {startingbid}, current bid is {currentbid}")
        if currentbid > startingbid and currentbid > maxbid:
            obj.save()
            print(f"salvado y comparado")
        
    return render(request, "auctions/listing.html", {
        "listing": listing, 
    })    


class AddCommentView(CreateView):
        model = Comments
        template_name = 'add_comment.html'
        form_class = PostForm



def LikeView(request, pk):
    listing = get_object_or_404(Listings, listing_id=request.POST.get('watchlist_id')) #watch_id is the name we gave to the button in the template
    listing.watchlist.add(request.user) #save the user as well
    return HttpResponseRedirect(reverse('listing', args=[str(pk)]))


def bids(request, listing_id):
    form = NewBidForm()
    #listing = Listings.objects.get(listing_id=listing_id)

    if request.method == "POST":
        form = NewBidForm(request.POST)
        if form.is_valid():
            obj = Bids()
            obj.username = request.user
            obj.listing = request.POST.get('listing_id')
            obj.bid_amount = form.cleaned_data['bid_amount']
            obj.save()
        return HttpResponseRedirect('/')
    else:
        listing = Listings.objects.get(listing_id=listing_id)
        return render(request, "auctions/listing.html", {
            "listing": listing, 
        })    
