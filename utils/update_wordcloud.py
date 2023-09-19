from book.models import WordCloud
import csv

WordCloud.objects.all().delete()

idx = 1
with open("keyword.csv", encoding="UTF-8") as f:
    rdr = csv.reader(f)
    for line in rdr:
        word_cloud = WordCloud(main_category=line[0], image="cloud"+str(idx)+".jpg")
        word_cloud.save()
        idx += 1

