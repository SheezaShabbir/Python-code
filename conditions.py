def test():
    x=9+4
    print("if answer is true it is ",x==13)
    print("check whether it is true : its",3+3<2+4)
test()

def test2(x,y):
    if(y>=x+x):
      print(y, "greater than or equal", x + x ,"is true.")  
    else:
      x = 3
      y = x + 8
 
x=input("Enter x:")
y=input("Enter y:")
test2(x,y)
if("Hello">"hello"):
   print("True")
else:
   print("False")
name = "Tobias"

print(name == "Alton")
#check casting
str_integer='700'
int_number=200
number_total=int_number+int(str_integer)
print(number_total)
a=int(input("enter digits:"))
b=int(input("enter digits:"))
output=a+b
print(a,"+",b,"=",output)            

size_num = "8 9 10"

size = "8" # user input

if size.isdigit() == False:
    print("Invalid: size should only use digits")
elif int(size) < 8:
    print("size is too low")
elif size in size_num:
    print("size is recorded")
else:
    print("size is too high")


num="20"
if(num.isdigit()):
   print("ok",num.isdigit())
else:
   print("NO",num.isdigit())
operator=input("Select operator(*,/):")
a=int(input("enter digits:"))
b=int(input("enter digits:"))
def multiply(a,b,ope):
    if(ope=="/"):
       c=a/b
       equa=str(a)+"/"+str(b)+"="+str(c)
       return equa
    elif(ope=="*"):
        c=a*b
        equa=str(a)+"*"+str(b)+"="+str(c)
        return equa
    else:
        print("Invalid operator")
print(multiply(a,b,operator))
calculation = 5 + 3 + 3 * 2 - 1
print(calculation)

maximum=100
minimum=50
price=144
value=float(input("Enter cheese order weight (numeric value):"))
def cheese_order(val,max,min,p):
    if val>max:
       print(val,"is more than currently available stock.")
    elif val<min:
       print(val,"is below minimum order amount.")
    else:
       print(val,"costs","$"+str(p),".")
cheese_order(value,maximum,minimum,price)

