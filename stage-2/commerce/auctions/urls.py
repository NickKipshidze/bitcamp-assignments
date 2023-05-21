from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

    path("listing/<int:id>", views.listing, name="listing"),
    path("create_listing", views.create_listing, name="create_listing"),

    path("category", views.category, name="category"),

    path("watchlist_remove/<int:id>", views.watchlist_remove, name="watchlist_remove"),
    path("watchlist_add/<int:id>", views.watchlist_add, name="watchlist_add"),
    path("watchlist", views.watchlist, name="watchlist"),

    path("comment_add/<int:id>", views.comment_add, name="comment_add"),

    path("bid_add/<int:id>", views.bid_add, name="bid_add"),

    path("auction_close/<int:id>", views.auction_close, name="auction_close")
]
