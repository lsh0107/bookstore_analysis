from django.contrib import admin
from .models import MainCategory, SubCategory, Book, BookSimilarity, PlatformAnalysis, BestSeller, Review, WordCloud,Borrow
admin.site.register(MainCategory)
admin.site.register(SubCategory)
admin.site.register(Book)
admin.site.register(BookSimilarity)
admin.site.register(PlatformAnalysis)
admin.site.register(BestSeller)
admin.site.register(Review)
admin.site.register(WordCloud)
admin.site.register(Borrow)