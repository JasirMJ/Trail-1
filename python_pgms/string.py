str="Hello World "

print(str)

print (str[0])#first letter

print(str[2:5])#string 3 to 5

print (str[2:])#string starting from 3rd character

print (str*2)#string prints 2 times

print(str+"!!")#concantination

print(str[:6]+"python")#updating string
#print(str[0:5]+"this is")

H="Hello"
print(H not in str)#membership look for character exist or not

name='sumi'
age=22
height=169
print("My name %s is %d old and I'm %dcm tall!"%(name,age,height))
print("%s is %d years old"%(name,age))
#name = "John"
#age = 23
#print("%s is %d years old." % (name, age))

para_str=""" this is a long string contains
    TAB( \t ) and
    NEWLINEs [\n] and
    just a NEWLINE within the variable assignment will also show up"""
print (para_str)

print("\\now all good")
print(r"\\ i am okay")
print(u"lololololol")

str1="sumi"
str2="INDIA"
print(str1.capitalize())
print(str2.lower())
print(str1.upper())
print(str2.count("I",0,4))

