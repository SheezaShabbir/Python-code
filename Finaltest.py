def adding_report(type="T"):
    value=""
    total=0
    count=0
    j=0
    items=""
    if(type=='T'):
       print("Input an integer to add to the total or 'Q' to quit:")
       while True:
             value=input("Enter an integer or 'Q':")
             if(value=='Q'):
                break
             elif(value=='q'):
                  break
             elif(value=='Quit'):
                  break
             if(value.isdigit()):
                total=total+int(value)
             elif(value.isalpha()):
                 print(value," is inavlid input")
       print("Total")
       print(total)      
         
    elif(type=='A'):
        print("Input an integer to add to the total or 'Q' to quit:")
        while True:
              value=input("Enter an integer or 'Q':")
              if(value=='Q'):
                break
              elif(value=='q'):
                  break
              elif(value=='Quit'):
                  break
              if(value.isdigit()):
                 count=count+1
                 items=items+value+"\n"
                 total=total+int(value)
              elif(value.isalpha):
                   print(value," is inavlid input")   
        print("items:")
        print("\n",items)
        print("Total:")
        print(total) 
        

while True:
    print("Report type includes All items report (A) or Total sum (T):")
    type=input("Choose report type 'A' or 'T':")
    adding_report(type)
    break

