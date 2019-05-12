
def printme( str ):
    print( str )
    return

printme("i'm sumi")
printme("im 42 years old")

def change( mylist ):
    mylist.append([1,2,3])
    print("inside",mylist)
    return
mylist=[10,20,30]
change( mylist )
print("outside",mylist)
