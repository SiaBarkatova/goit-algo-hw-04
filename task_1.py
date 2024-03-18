def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file_salaries: 
            read_salaries = file_salaries.readlines() # open file as list of lines
        
        total = 0
        for person in read_salaries: #iterate trough list 
            person_data = person.strip().split(",") #split strings into parts
            total += int(person_data[1]) #second part always salary. add to total

    except OSError as err:
        print('Помилка доступу до файлу: ', err)

    average = total / len(read_salaries) #calculating average
    return total, average

total, average = total_salary('salaries.txt')
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")