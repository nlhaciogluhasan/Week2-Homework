""""
Date : 09.02.2022
Prepared by the Program : Hasan
Name Of The Program : common letters in two different words entered, letters in the first word but not in the second word
                      and detection of the letters in the second word that are not in the first word

"""
set1=set(input("Enter a word : "))          #We get 2 word entries from the user and put them in the "set".
set2=set(input("Enter second word : "))
#######################################################################################
#set3=set1.intersection(set2)              #Here we put the desired operations into a "set". intersection, difference operations.
#set4=set1-set2                            #But below we can also do them in a single line.
#set5=set2-set1
#mylist=[list(set3),list(set4),list(set5)]
#######################################################################################

#Here, we convert the desired operations to the "list" data type and put them in a list.
mylist=[list(set1.intersection(set2)),list(set1-set2),list(set2-set1)] 
i=0
while i<3:                  #The purpose of the while loop here is to "sort" the list elements first and then combine the elements.
    mylist[i].sort()
    mylist[i]="".join(mylist[i])
    i+=1
print(mylist)