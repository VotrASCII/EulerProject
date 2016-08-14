a, b, c, i, d = 1, 0, 0, 0, []
while(c<=4000000):
    c=a+b
    b=a
    a=c
    if(i%3==1):
        d.append(c)

    i+=1

print(d)    
res=sum(d)
print(res)
