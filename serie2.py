n=int(input("Digite n :"))
s="serie: "

for i in range(1,n+1):
    b=2**i
    c=b
    if i<n:
        s=s+str(c)+","
    else:
        s=s+str(c)


print(s)