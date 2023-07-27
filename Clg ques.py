a=[]
no=int(input("Enter how many elements are there :"))
print("\n\"Elements should be given in acending order\"")
for i in range(1,no+1):
    print("\nEnter element no",i,end='')
    r=input(" here :")
    a.append(r)
print("\n\tThe Entered List is :",a)

    
c=[]
k=['_']
lent=len(a)

for i,j in enumerate(a):
    if a.count(j)>1:
        del a[i]
        a.append(k[0])

for i in range(len(a)):
    if a[i]==k[0]:
        c.append(a[i])
        
d=len(a)
e=len(c)
f=d-e

print("\nRequired Output : \t",f,",",a)

        
        
