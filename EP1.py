a, b, c=[], [], []
for i in range(1000):
    if(i%3==0):
        a.append(i)

    elif(i%5==0):
        b.append(i)

    elif(i%15==0):
        c.append(i)

res=sum(a)+sum(b)-sum(c)
print(res)
