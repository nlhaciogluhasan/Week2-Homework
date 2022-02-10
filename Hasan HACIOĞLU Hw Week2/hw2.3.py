""""
Date : 09.02.2022
Prepared by the Program : Hasan
Name Of The Program : Detection of how many and which letters in the entered text

"""

list2=[]
dictionary={}
list1=list(input("Enter a text : "))
#######################################################################################
for i in list1:  #The purpose of the for loop here is to throw the letters of the entered text into the list one by one.
    list2.append(i)
#######################################################################################    
for i in list1:   #The purpose of the for loop here is to determine which letter has how many.
    if i in dictionary:
        dictionary[i]+=1
    else:
        dictionary[i]=1     
        
s=sorted(dictionary.items())   #It is intended here to be sorted in alphabetical order.
print(s)