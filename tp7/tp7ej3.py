
def missing_no(self):
    numscheck = list(range(0,101))
    list1 = []
    for i,k in zip(self, numscheck):
        if i != k:
            list1.append(i)
        else:
            pass
    missing = list1[0]-1
    return missing


