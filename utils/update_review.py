from book.models import Review, Book
import csv


with open("review_process.csv", newline='', encoding="UTF-8") as f:
    rdr = csv.reader(f)
    for line in rdr:
        try:
            book = Book.objects.get(naver_id=line[0])
            entity = Review(book=book, star = line[1], content=line[2])
            entity.save()
        except :
            print(line[0])
