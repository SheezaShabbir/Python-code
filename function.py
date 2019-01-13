def first_code():
    print("My name is Sheeza.")
    print("This is my first function.")
first_code()
def yel_it(phrase):
    print(phrase.upper()+"!")
yel_it("This is all jokes.")    
    
#for default values:
def yel_it(phrase="This is me."):
    print(phrase.upper()+"!")
#Passing value
yel_it("This is all jokes.")
#for default value
yel_it()
#Another task
phrase=input()
yel_it(phrase)
def add_num(num_1 = 10):
    print(num_1 + num_1)
add_num()
#Another task with return
def make_doctor(name):
    return name
full_name=input()
print(make_doctor(full_name))
#Another task
def make_schedule(period1, period2 ,peroid3):
    schedule = ("\n[1st] " + period1.title() + "\n[2nd] " + period2.title()+"\n[3nd] " + peroid3.title())
    return schedule

student_schedule = make_schedule("mathematics", "history","Science")
print("SCHEDULE:", student_schedule)

def add_numbers(num_1, num_2 = 10):
    return num_1 + num_2
print(add_num(100))
def bird_available(bird):
    bird_types = 'crow robin parrot eagle sandpiper hawk pigeon'
    if(bird in bird_types):
       return True
    else:
       return False
bird=input()
value=bird_available(bird)
if(value==True):
   print("The",bird,"available is true.")
else:
   print("The",bird,"available is false.")
   #task
def how_many():
    requested = input("enter how many you want: ")
    return requested

# get the number_needed
number_needed = how_many()
print(number_needed, "will be ordered")

def fishstore(fish,price):
    sentence="Fishtype:"+" "+fish+" "+"costs"+" "+"$"+price
    return sentence
fish=input("enter the fish name:")
price=input("enter the fish price(no symbols):")
print(fishstore(fish,price))
year = "2001" 

if year.isdigit():
    print(year, "is all digits")  
else:
   pass
       
        
    
