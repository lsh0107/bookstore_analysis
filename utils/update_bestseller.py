from book.models import BestSeller, MainCategory, Book
import csv
import pandas as pd
book_info = pd.read_csv("book_info_and_bookstore_url.csv")

book_info_process = book_info.drop_duplicates(["book_title"]).groupby("main_category").head(20)
book_info_process = book_info_process[["main_category", "book_id"]]

book_info_process.to_csv("bestseller.csv")

BestSeller.objects.all().delete()

with open("bestseller.csv", encoding="UTF-8") as f:
    rank = 1
    rdr = csv.reader(f)
    for line in rdr:
        try:
            main_category = MainCategory.objects.get(name = line[1])
            book = Book.objects.get(naver_id=line[2])
            entity = BestSeller(main_category=main_category, book=book, rank = rank)
            entity.save()
            rank+=1
        except:
            pass