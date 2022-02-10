""""
Date : 09.02.2022
Prepared by the Program : Hasan
Name Of The Program : Lucky Numbers

"""
#######################################################################################
liste=[]
n=int(input("Enter a number : "))
for i in range(1,n+1):             #The purpose of the for loop here is; is to generate numbers in a list up to the entered number.
    liste.append(i)
print ("List = ",liste )
#######################################################################################
i=1
iteration=0
while i<len(liste):   #The purpose of the while loop here is to subtract the 2nd numbers in the 1st iteration, 
    del(liste [i:n:i+1])  #the 3rd numbers in the 2nd iteration and continue until the end.
    i=i+1
    iteration =iteration+1
    print(iteration,". iteration : ",liste)

print ("\nLucky Numbers : ",liste) 
