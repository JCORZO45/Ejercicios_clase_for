n=int(input("Digite el número de series :"))
s="serie= {"

for i in range(1,n+1):
    

    if i<n:
        s=s+"1/"+str((i+1)*i)+ ", "
    else:
        s=s+"1/" +str((i+1)*i)

print(s)