quote=input("enter a 1 sentence quote, non-alpha separate words:").lower()
word=""
for check in quote:
    if(check.isalpha()):
       word+=check
    else:
        if(word and word[0]
           > "g" ):
            print(word.upper())
            word = ""
        else:
            word = ""
print(word.upper())
