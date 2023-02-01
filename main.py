def flatten_list(l):
    l = eval(l)
    lis = []
    for i in l:
        s = []
        st = str(i)[::-1]
        for j in range(0,len(st),3):
            s.append(st[j:j+3][::-1])
        s = s[::-1]
        lis.append(",".join(s))
    return lis

print(flatten_list(input()))
