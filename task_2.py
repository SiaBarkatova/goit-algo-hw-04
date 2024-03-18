def get_cats_info(path):
    cats = []
    try:
        with open(path, 'r', encoding='utf-8') as file_cats:
            read_cats = file_cats.readlines() #reading lines from the file

            for cat in read_cats: #iterates trough the cats list
                cat_raw_data = cat.strip().split(",") #split each row into list

                #prepare the dict with data in correct format
                cat_data = { 
                    "id": cat_raw_data[0],
                    "name": cat_raw_data[1],
                    "age": cat_raw_data[2]
                } 
                #add data to the list
                cats.append(cat_data)

    except OSError as err:
        print('Помилка читання файла: ', err)

    return cats
     
cats_info = get_cats_info("cats.txt")
print(cats_info)