#region пример нового 23

def task23(start,end):
    if start == end:
        return 1
    if start > end:  #если в ответе 0,поставь галку наоборот(ну типа "<"),здесь поставленна верно
        return 0
    if str(start)[2] > str(start)[1]:
        return task23(start + 1,end) + task23(int(str(start)[0] + str(start)[2] + str(start)[1]),end)
    else:
        return task23(start + 1,end)
print(task23(100,150))

"""
вроде работает(ответ верный всмысле)
надеюсь подлянок не будет и оно будет работать

"""
