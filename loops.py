familier_name=""
#while True:
    #familier_name=input()
    #if(familier_name!=""):
      # break;
    #else:
       #print("Finally you use something..")
count = 1

while count >= 1:
    print("loop")
    count +=1

def ignore_case(name):
    answer = ""
    while answer.isalpha() == False:
        answer = input("enter last name: ")
    return answer.lower() == name.lower()
x = 0 

while x < 5:
    x += 1
    print('loop')

    
time = 3

while True:
    print('time is', time)
    if time == 3:
        time = 4
    else:
        break
x = 0 

while True:
    if x < 10:
        print('run forever')
        x += 1
    else:
        break
num_1 = ""
num_temp = ""
num_final = ""

while True:
    num_1 = input("Enter an integer: ")
    if num_1.isdigit():
        num_final = num_temp + num_1
        num_temp = num_final
    else:
        print(num_final)
        break

    
num=3;
if num.isdigit():
   print("Working")
s=0
l=0
m=0      

while True:
    size=input("S,M,L:")
    if(size=='S'):
       s=s+1
    elif(size=='M'):
       m=m+1
    elif(size=='L'):
       l=l+1
    elif(size=='exit'):
       print(s,l,m)
       break;
