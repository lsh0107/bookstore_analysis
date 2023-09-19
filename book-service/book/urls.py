from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('category/', views.category),
    path('category/<int:sub_category_id>/', views.category_detail),
    path('book/<int:book_id>/', views.book_detail),
    path('bestseller/', views.bestseller),
    path('book-store/', views.book_store),
    path('book-store/price', views.book_store_price),
    path('book-store/review', views.book_store_review),
    path('book-store/star', views.book_store_star),
    path('book-store/price-all', views.book_store_price_all),
    path('book-store/review-all', views.book_store_review_all),
    path('book-store/star-all', views.book_store_star_all),
    path('search/<str:keyword>/', views.search),
    path('trend/', views.trend),
    path('trend-detail/<int:word_cloud_id>/', views.trend_detail)

]