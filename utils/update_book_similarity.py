from book.models import BookSimilarity, Book
import csv

BookSimilarity.objects.all().delete()

with open("book_similarity_final.csv", encoding="UTF-8") as f:
    rdr = csv.reader(f)
    for line in rdr:
        try:
            book = Book.objects.get(naver_id=line[1])
            book_similarity = BookSimilarity(target_book = book, compare_book_naver_id = line[2], score=float(line[3]))
            book_similarity.save()
        except Book.DoesNotExist:
            print(line[1])