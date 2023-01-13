def modify_list(l):
    for i in range(len(l) - 1, -1, -1):
        if l[i] % 2 == 1:
            l.remove(l[i])
        else:
            l[i] //= 2
