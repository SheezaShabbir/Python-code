name="Sheeza"
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[-5])
print(name[-6])
print(name[2:5])
print(name[:3])
print(name[4:])
print(name[:0])
print(name[:1])
print(name[:6])
print(name[5:6])
print(name[6:])
print(name[:])
print(name[::2])
print(name[::1])#stepstrings
print(name[1:1:2])#Steping strings
print(name[::-1])#reverse string
print(name[2::-1])#reversing slice of string
name = "Alton"
print(name[::2])
for letter in name:#iterating strings
    print(letter)
name=input()
new_name=""
for i in name:
    if i.lower()=='i':
       new_name+=i.upper()
    elif i.islower()=='o':
       new_name+=i.upper()
    else:
       new_name=name
print(new_name)
for letter in name[::-1]:
    print(letter)
    
print(len(name))#for finding length
sentence="I am fine really what abot you?"
length=len(sentence)
mid=int(length/2)
print(sentence[:mid])
print(sentence[:mid].count("e"))
print(sentence[mid:])
print(sentence[mid:].count("e"))
print(sentence.count("a"))#for counting
print(sentence[:8].count("a"))
#To find the index of where a character or a sub-string occurs within a string, we can use the find method.
#Now lets start
# to find space index
print(sentence.find(""))
print(sentence.find("really"))
#find method with three arguments such as string starting index ,ending index and string itself
print(sentence.find("fine",9,13))

