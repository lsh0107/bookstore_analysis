from book.models import MainCategory, SubCategory
import csv
main_category_list = list()
with open("book_category.csv", "r", encoding="UTF-8") as f:
    rdr = csv.reader(f)
    for  line in rdr:
            if line[0] not in main_category_list:
                    main_category_list.append(line[0])
                    m = MainCategory(name=line[0])
                    m.save()


with open("book_category.csv", "r", encoding="UTF-8") as f:
    rdr = csv.reader(f)
    for  line in rdr:
            main_category = MainCategory.objects.get(name = line[0])
            s = SubCategory(main_category=main_category, name = line[1])
            s.save()