n=int(input("Digite n :"))
s="serie={"
for i in range ( 1,n+1):
    c=i**2
    if i<n:
        s=s+str(c)+","
    else:
        s=s+str(c)

print (s)