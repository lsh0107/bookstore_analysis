from book.models import PlatformAnalysis
import csv

PlatformAnalysis.objects.all().delete()

with open("book_main_price.csv", encoding="UTF-8") as f:
    rdr = csv.reader(f)
    for line in rdr:
            entity = PlatformAnalysis(task="maincategory_price", label=line[0], aladin = line[1], kyobo=line[2], interpark=line[3], yes=line[4], total=line[5])
            entity.save()

with open("book_main_star.csv", encoding="UTF-8") as f:
    rdr = csv.reader(f)
    for line in rdr:
            entity = PlatformAnalysis(task="maincategory_star", label=line[0], aladin = line[1], kyobo=line[2], interpark=line[4], yes=line[3], total=line[5])
            entity.save()

with open("book_main_review.csv", encoding="UTF-8") as f:
    rdr = csv.reader(f)
    for line in rdr:
            entity = PlatformAnalysis(task="maincategory_review", label=line[0], aladin = line[2], kyobo=line[4], interpark=line[1], yes=line[3], total=line[5])
            entity.save()