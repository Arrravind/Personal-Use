import random
r=random.randrange(1,101)
count=0
while True:
    count+=1
    n=int(input("Guess The Number :"))
    if n==r:
        print("you Guessed the Right Answer!!")
        break
    elif n<r:
        print("Too Low")
    else:
        print("Too high")
print("Total No of tries :",count)
if count<=3:
    print("Insane!!!!")
elif (count>3 and count<=5):
    print("Well Done")
else:
    print("Not Bad")
    
