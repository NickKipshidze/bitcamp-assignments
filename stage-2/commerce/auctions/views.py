from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Category, Listing, Comment, Bid


def index(request):
    listings = Listing.objects.filter(active = True)

    return render(request, "auctions/index.html", {
        "listings": listings,
        "categories": Category.objects.all()
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

def create_listing(request):
    if request.method == "GET":
        return render(request, "auctions/create_listing.html", {
            "categories": Category.objects.all()
        })
    elif request.method == "POST":
        user = request.user

        title = request.POST["title"]
        description = request.POST["description"]
        price = request.POST["price"]
        image_url = request.POST["image_url"]
        category = Category.objects.get(name = request.POST["category"])

        bid = Bid(
            bid = float(price),
            user = user
        )

        bid.save()

        listing = Listing(
            title = title,
            description = description,
            image_url = image_url,
            price = bid,
            category = category,
            owner = user
        )

        listing.save()

        return HttpResponseRedirect(reverse(index))

def category(request):
    if request.method == "POST":
        listings = Listing.objects.filter(
            active = True, 
            category = Category.objects.get(
                name = request.POST["category"]
            )
        )

        return render(request, "auctions/index.html", {
            "listings": listings,
            "categories": Category.objects.all()
        })

def listing(request, id):
    watchlist = \
        request.user in \
            Listing.objects.get(pk = id).watchlist.all() 
    
    comments = Comment.objects.filter(
        listing = Listing.objects.get(pk = id)
    )

    owner = request.user.username == Listing.objects.get(pk = id).owner.username

    return render(request, "auctions/listing.html", {
        "listing": Listing.objects.get(pk = id),
        "watchlist": watchlist,
        "comments": comments,
        "owner": owner
    })

def watchlist(request):
    listings = request.user.watchlist.all()
    return render(request, "auctions/watchlist.html", {
        "listings": listings
    })

def watchlist_remove(request, id):
    Listing.objects.get(pk = id).watchlist.remove(request.user)
    return HttpResponseRedirect(reverse(listing, args=(id, )))

def watchlist_add(request, id):
    Listing.objects.get(pk = id).watchlist.add(request.user)
    return HttpResponseRedirect(reverse(listing, args=(id, )))

def comment_add(request, id):
    message = request.POST["comment"]

    comment = Comment(
        commenter = request.user,
        listing = Listing.objects.get(pk = id),
        message = message
    )

    comment.save()

    return HttpResponseRedirect(reverse(listing, args=(id, )))

def bid_add(request, id):
    new_bid = request.POST["bid"]
    listing_info = Listing.objects.get(pk = id)

    if float(new_bid) > listing_info.price.bid:
        updated_bid = Bid(user = request.user, bid = float(new_bid))
        updated_bid.save()
        listing_info.price = updated_bid
        listing_info.save()

        messages.info(request, "Bid Successful")
        return HttpResponseRedirect(reverse(listing, args=(id, )))
    else:
        messages.info(request, "Bid Failed")
        return HttpResponseRedirect(reverse(listing, args=(id, )))

def auction_close(request, id):
    listing_info = Listing.objects.get(pk = id)
    listing_info.active = False
    listing_info.save()

    messages.info(request, "Auction closed")
    return HttpResponseRedirect(reverse(listing, args=(id, )))