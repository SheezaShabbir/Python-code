def list_o_matic(word,Fruits_list):
    if(word == ""):
        word=Fruits_list.pop()
        line=str(word)+" "+"popped from list"
        return line
    elif(word in Fruits_list):
       word=Fruits_list.remove(word)
       line="1 instance of"+" "+str(word)+" "+"removed from list"
       return line
    elif(word not in Fruits_list):
        if(word not in Fruits_list):
           word=Fruits_list.append(word)
           line="1 instance of "+" "+str(word)+" "+" appended to list"
           return line
   




#Test of the list:
Fruits_list=["Apple","Banana","Mango","Grapes","Orange","Pineapple"]
while True:
      print("Look at all the Fruits",Fruits_list)
      word=input("enter the name of fruit:")
      if(word.lower()!="quit"):
         print(list_o_matic(word,Fruits_list))
      else:
          break
    
        
