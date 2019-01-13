#showing lists
#adding list
numbers=[2,3,4,5,6,7,8,9]
total=0
for number in numbers:
    total+=number
print(numbers)
print(total)
#sorting and filtering
words=['asd','yesd','oka','asdkdj','dksjhdasj']
shortwords=""
longwords=""
for word in words:
    if(len(word)<5):
       shortwords+=word+"\n"
    else:
       longwords+=word+"\n"
print("Short Words\n",shortwords)
print("Long words\n",longwords)
#counting and searching
search_word="a"
total=0
for word in words:
    total+=word.lower().count(search_word)
    print("Finding in each word",total)
print(total)
cities = ["New York", "Shanghai", "Munich", "Tokyo", "Dubai", "Mexico City", "São Paulo", "Hyderabad"]

for city in cities:
    if city.startswith("P"):
        print(city)
    elif city.startswith("D"):
        print(city)
#range()
for i in range(20):
    print(i)
cities = ["New York", "Shanghai", "Munich", "Tokyo", "Dubai", "Mexico City", "São Paulo", "Hyderabad"]
half=int(len(cities)/2)
for word in range(half):
    print(cities[word])
#range(start,stop)
for i in range(11,20):
    print(i)
#range(start,stop,step)
for i in range(11,40,5):
    print(i)    
