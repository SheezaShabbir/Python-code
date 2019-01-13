letters=['A','B','C','D']
print(letters,type(letters))

numbers=[1,2,3,4,5,6]
print(numbers,type(numbers))


Mixedlist=["Sheeza","Kinza",12345,numbers,letters]
print(Mixedlist,type(Mixedlist))


print(numbers[0]+numbers[1]+numbers[2])
print(numbers[-3]+numbers[-1]+numbers[-2])
Mixedlist.append("Tayyab")
print(Mixedlist)
#using indexing you can replace items in alist but can not add a value at a new index.
# for the purpose of new index one can use insert method in list
numbers.insert(6,7)
print(numbers)
numbers.insert(7,"Sheeza")
print(numbers)
numbers.insert(2,"Aliza")
print(numbers)
del numbers[2]
print(numbers)
del numbers[-1]
print(numbers)
# poping items from the list without argument pop() method,,,It pop from right to left
print(letters)
print(letters.pop())
print(letters)
#can also pop specific item using pop(index)

print(letters)
print(letters.pop(1))
print(letters)
while Mixedlist:
      print(Mixedlist.pop(),"Just check list",Mixedlist)
# nOw the remove method where we give item as a parameter to remove but in previous work we were giving index:
words=["ok","hell","dream","wow"]
while "hell" in words:
      words.remove("hell")
      print(words)


