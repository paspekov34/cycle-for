list_ = ["BMW", "MB", "LADA", "KIA", "HONDA"]
string = 'Я езжу на автомобиле марки, '
cars_count = 0
for i in range(len(list_)):
    cars_count = string + list_[i]
    print(cars_count)
    # - не понял как сделать, cars_count += 10 если вставляю в цикл,
    # ошибку выдаёт, но как понимаю выходит здесь правильно!

list_ = ["BMW", "MB", "LADA", "KIA", "HONDA"]
cars_count = 0
for i in range(len(list_)):
    cars_count += 10
    print(f'Я езжу на автомобиле марки, {cars_count}')
# - если так делать то не выдает марки машин, если после for i in range(len(list_)):
# добавить [i] или номер индекса то тоже ошибку выдает! Что делаю не так???







