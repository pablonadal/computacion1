def sum_of_differences(*args):
    list = []
    for i in args:
        list.append(i)
    list.sort(reverse=True)
  #  print(list)
    q1 = list[0]
    w2 = list[1]
    if len(list)==2:
        e3 = list[1]
    else:
        e3 = list[2]
    sum = (q1-w2)+(w2-e3)
    return sum

sum_of_differences(1,2,10)

