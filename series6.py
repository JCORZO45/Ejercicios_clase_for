n=int(input("Digite el número de series :"))
s="serie= {"

for i in range(1,n+1):
    

    if i<n:
        s=s+str(3+(i-1)*5)+ ", "
    else:
        s=s +str(3+(i-1)*5)

print(s)