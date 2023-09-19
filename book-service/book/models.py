from django.db import models

class MainCategory(models.Model):
    name = models.CharField(max_length=200)

class SubCategory(models.Model):
    name = models.CharField(max_length=200)
    main_category = models.ForeignKey(MainCategory, on_delete=models.CASCADE)

class Book(models.Model):
    main_category = models.ForeignKey(MainCategory, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    naver_id = models.CharField(max_length=300)
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=300)
    publisher = models.CharField(max_length=300)
    publish_date = models.CharField(max_length=200)
    cover_image = models.CharField(max_length=200)
    intro = models.TextField()
    aladin_url = models.CharField(max_length=500)
    kyobo_url = models.CharField(max_length=500)
    yes24_url = models.CharField(max_length=500)
    interpark_url = models.CharField(max_length=500)
    aladin_price = models.CharField(max_length=100)
    aladin_star = models.CharField(max_length=100)
    aladin_review = models.CharField(max_length=100)
    kyobo_price = models.CharField(max_length=100)
    kyobo_star = models.CharField(max_length=100)
    kyobo_review = models.CharField(max_length=100)
    yes24_price = models.CharField(max_length=100)
    yes24_star = models.CharField(max_length=100)
    yes24_review = models.CharField(max_length=100)
    interpark_price = models.CharField(max_length=100)
    interpark_star = models.CharField(max_length=100)
    interpark_review = models.CharField(max_length=100)
    lowest_price = models.CharField(max_length=100)
    avg_star = models.CharField(max_length=100)
    total_review = models.CharField(max_length=100)

class BookSimilarity(models.Model):
    target_book = models.ForeignKey(Book, on_delete=models.CASCADE)
    compare_book_naver_id = models.CharField(max_length=300)
    score = models.FloatField()

class PlatformAnalysis(models.Model):
    task = models.CharField(max_length=100)
    label = models.CharField(max_length=100)
    aladin = models.FloatField()
    yes = models.FloatField()
    kyobo = models.FloatField()
    interpark = models.FloatField()
    total = models.FloatField(null=True)


class BestSeller(models.Model):
    main_category = models.ForeignKey(MainCategory, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rank = models.IntegerField()

class Borrow(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    target_book = models.CharField(max_length=300)
    rank = models.IntegerField()

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    star = models.FloatField()
    content = models.TextField()

class WordCloud(models.Model):
    main_category = models.CharField(max_length=300)
    image = models.CharField(max_length=300)

