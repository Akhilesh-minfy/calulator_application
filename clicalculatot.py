def add(a,b):
    return a+b

def sub(a,b):
    return a-b
 

def mul(a,b):
    return a*b


def div(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("can't divide by zero")
    else:
        return a/b

def add(l1):
    sum=0
    for i in l1:
        sum+=i
    return sum

def sub(l1):
    sum=0
    for i in l1:
        sum-=i
    return sum

def mul(l1):
    sum=0
    for i in l1:
        sum*=i
    return sum

def div(l1):
    sum=l1[0]
    try:
        for i in range(1,len(l1)):
            sum/=l1[i]
        
    except ZeroDivisionError:
        print("can't divide by zero")

    else:
        return int(sum)

print("select symbol:")
print("addition : +")
print("subtraction : -")
print("multiplication : *")
print("division : /")
choice=str(input("enter your choice:"))
length=int(input("how many numbers you want to operation:"))
list1=[]
for  i in range(length):
    list1.append(int(input(f"enter number {i+1} :")))

   

match choice:
        case '+': res=add(list1)
        case '-': res=sub(list1)
        case '*': res=mul(list1)
        case '/': res=div(list1)
        case _:print("wrong operator")
print(f"Ans:{res}")