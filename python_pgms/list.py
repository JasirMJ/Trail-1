list=[ 'english' , 200 , "hindi" , 199 , 22]
tiny=[123,"jack"]
list2=[1,3,5,7,9,2,4,6,8]

print (list)
print (list[0])
print (list[1:3])
print (list[2:])
print (tiny*2)
print(list+tiny)

#updating list
print("before updating")
print(list)
print(list[0])
print("after updating")
list[0]="french"
print(list[0])
print(list)

#deleting elements
print("before deleting")
print(list)
del list[4]
print("after deleting")
print(list)

#basic list operations
length=len([1,2,3])
print("the length is",length)

concat=[1,2,3,4]+[5,6,7]
print(concat)

repeat=['hi']*4
print(repeat)

member=3 not in [1,2,4,]
print(member)

for x in [1,2,3]:
    print(x)

#indexing slicing and matrixes
l=['spam','Spam','SPAM!']
print(l[2])
print(l[-1])
print(l[-2:-1])

#compare list
l2,l1=[1,2,3,4,5,6,7,8],[4,3,2,1]
#print(cmp(l1,l2))
print(len(l1))
print(max(l1))
print(min(l1))

#append to list
aList=[123,'xyz','abc','abc']
print(aList)
print(aList.append(2009))
print(aList.count('abc'))
bList=['ok','cool',123,'poopy']
aList.extend(bList)
print(aList)
print(aList.index('123'))

