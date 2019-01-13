def str_analysis(pass_argument):
    if(pass_argument.isdigit()):
       int_conversion=int(pass_argument)
       if(int_conversion>90):
         printvalue=str(int_conversion)+" "+"is pretty big number."
         return printvalue
       elif(int_conversion<90):
         printvalue=str(int_conversion)+" "+"is pretty small number than expected."
         return printvalue
       else:
         printvalue=str(int_conversion)+" "+"is number between expected."
         return printvalue  
    elif(pass_argument.isalpha()):
         printvalue=pass_argument+" "+"is all alphabetical characters!"
         return printvalue
    else:
        printvalue=pass_argument+" "+"neither all alpha nor all digit."
        return printvalue


while True:
    stro=input("enter a word or a digit:")
    if(stro!=""):
      print(str_analysis(stro))
      break
    
    
