from book.models import MainCategory, SubCategory, Book
import csv

Book.objects.all().delete()

with open("book_info.csv", newline='', encoding="UTF-8") as f:
	rdr = csv.reader(f)
	for line in rdr:
		main_category = MainCategory.objects.get(name = line[1])
		sub_category = SubCategory.objects.get(name=line[2], main_category=main_category)
		book = Book(main_category=main_category, sub_category=sub_category, naver_id=line[0], title=line[3],author=line[4],publisher=line[5],publish_date=line[6], aladin_price=line[7], aladin_star=line[8], aladin_review=line[9], kyobo_price=line[10], kyobo_star=line[11], kyobo_review=line[12], yes24_price=line[13], yes24_star=line[14], yes24_review=line[15], interpark_price=line[16], interpark_star=line[17], interpark_review=line[18], lowest_price=line[19], avg_star=line[20],total_review=line[21],intro=line[22], cover_image=line[0]+".jpg")
		book.save()