from book.models import PlatformAnalysis
import csv


with open("books_platform_analysis.csv", encoding="UTF-8") as f:
    rdr = csv.reader(f)
    for line in rdr:
            entity = PlatformAnalysis(task=line[5], label="all", aladin = line[0], kyobo=line[1], interpark=line[3], yes=line[2], total=line[4])
            entity.save()

