from django.shortcuts import render
import random
from .models import MainCategory, SubCategory, Book, BookSimilarity, PlatformAnalysis, BestSeller, Review, WordCloud, Borrow


def index(request):
    return render(request, 'book/home.html')

def category(request):
    main_category_list = MainCategory.objects.all()
    sub_category_dict = dict()
    for m in main_category_list:
        sub_category_dict[m.id] = list()
    sub_category_list = SubCategory.objects.all()
    for s in sub_category_list:
        sub_category_dict[s.main_category.id].append(s)
    context = { "main_category_list" : main_category_list,
                "sub_category_dict" : sub_category_dict}
    return render(request, 'book/category.html', context)

def category_detail(request, sub_category_id):
    main_category_list = MainCategory.objects.all()
    sub_category_dict = dict()
    for m in main_category_list:
        sub_category_dict[m.id] = list()
    sub_category_list = SubCategory.objects.all()
    for s in sub_category_list:
        sub_category_dict[s.main_category.id].append(s)

    selected_sub_category = SubCategory.objects.get(id=sub_category_id)

    book_list = Book.objects.filter(sub_category_id=sub_category_id)

    context = {"main_category_list": main_category_list,
               "sub_category_dict": sub_category_dict,
               "selected_sub_category":selected_sub_category,
               "book_list" : book_list}
    return render(request, "book/category-detail.html", context)

def book_detail(request, book_id):

    # book
    book = Book.objects.get(id=book_id)

    # category
    main_category_list = MainCategory.objects.all()
    sub_category_dict = dict()
    for m in main_category_list:
        sub_category_dict[m.id] = list()
    sub_category_list = SubCategory.objects.all()
    for s in sub_category_list:
        sub_category_dict[s.main_category.id].append(s)

    # similarity
    book_similarity_list = BookSimilarity.objects.filter(target_book_id=book_id).order_by("-score")[:5]
    similarity_list = list()

    for book_similarity in book_similarity_list:
        try:
            similarity_list.append(Book.objects.get(naver_id=book_similarity.compare_book_naver_id))
        except:
            pass

    # borrow
    book_borrow_list = Borrow.objects.filter(book=book_id)
    borrow_list = list()


    for book_borrow in book_borrow_list:
        try:
            borrow_list.append(Book.objects.get(naver_id=book_borrow.target_book))
        except:
            pass

    book_recommend_list = list()
    book_recommend_list.extend(similarity_list)
    book_recommend_list.extend(borrow_list)
    random.shuffle(book_recommend_list)
    book_recommend_list = book_recommend_list[:5]


    # review
    book_review_list = Review.objects.filter(book_id =book.id)

    context = {"main_category_list": main_category_list,
                   "sub_category_dict": sub_category_dict,
               "book_recommend_list" : book_recommend_list,
               "book":book,
               "book_review_list" : book_review_list}
    return render(request, 'book/book-detail.html',context )
def bestseller(request):

    # category
    main_category_list = MainCategory.objects.all()
    bestseller_list = dict()
    for m in main_category_list:
        bestseller_list[m.id] = list()
        bestselllers = BestSeller.objects.filter(main_category_id=m.id).order_by("rank")[:10]
        for b in bestselllers:
            bestseller_list[m.id].append(b)

    context = {"main_category_list": main_category_list,
               "bestseller_list" : bestseller_list}

    return render(request, 'book/bestseller.html', context)

def book_store(request):
    main_category_price_result = PlatformAnalysis.objects.filter(task="maincategory_price").order_by("label")
    context = {"main_category_price_result" :main_category_price_result}
    return render(request, 'book/book-store.html', context);

def book_store_price(request):
    main_category_price_result = PlatformAnalysis.objects.filter(task="maincategory_price").order_by("total")
    context = {"main_category_price_result" :main_category_price_result}
    return render(request, 'book/book-store-price.html', context)

def book_store_star(request):
    main_category_star_result = PlatformAnalysis.objects.filter(task="maincategory_star").order_by("total")
    context = {"main_category_star_result" :main_category_star_result}
    return render(request, 'book/book-store-star.html', context)

def book_store_review(request):
    main_category_review_result = PlatformAnalysis.objects.filter(task="maincategory_review").order_by("total")
    context = {"main_category_review_result" :main_category_review_result}
    return render(request, 'book/book-store-review.html', context)

def book_store_price_all(request):
    price_all = PlatformAnalysis.objects.get(task="price_all")
    context = {"price_all" : price_all}
    return render(request, 'book/book-store-price-all.html', context)

def book_store_review_all(request):
    review_all = PlatformAnalysis.objects.get(task="review_all")
    context = {"review_all": review_all}
    return render(request, 'book/book-store-review-all.html', context)

def book_store_star_all(request):
    star_all = PlatformAnalysis.objects.get(task="star_all")
    context = {"star_all": star_all}
    return render(request, 'book/book-store-star-all.html', context)


def trend(request):
    main_category_list = MainCategory.objects.all()
    context = {"main_category_list" : main_category_list}
    return render(request, 'book/trend.html', context);

def trend_detail(request, word_cloud_id):
    word_cloud_list = WordCloud.objects.all()
    word_cloud = WordCloud.objects.get(id=word_cloud_id)
    context = {"word_cloud_list" : word_cloud_list,
               "word_cloud" : word_cloud}
    return render(request, 'book/trend-detail.html', context);


def search(request, keyword):

    book_list = Book.objects.filter(title__contains=keyword)

    context = {"keyword":keyword,
               "len" : len(book_list),
               "book_list": book_list}
    return render(request, "book/search.html", context)