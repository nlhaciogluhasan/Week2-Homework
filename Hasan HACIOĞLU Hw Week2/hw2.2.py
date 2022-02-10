""""
Date : 09.02.2022
Prepared by the Program : Hasan
Name Of The Program : Right and Left Shift operation according to the size and sign of the number to be entered

"""
list1=[]
n=int(input("Enter a positive or negative number (Positive Number: Right Shift, Negative Number: Left Shift) : "))
m=int(input("How many elements will your list have?"))
for i in range(m):
    k=input("Enter the element of your list : ")
    list1.append(k)
print(list1,"My list\n")

if n<0:
    print("-------Left shift by",abs(n),"-------")
    for i in range(abs(n)):
        list1.append(list1[0])
        del list1[0]
    print("Final List :\n",list1)

elif n>0:
    print("-------Right shift by",n,"-------")    
    for i in range(n):        
        list1.insert(0,list1[m-1])  
        del list1[m]      
    print("Final List :\n",list1)
        
    