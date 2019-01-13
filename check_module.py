import Module as m
import platform
from Module import person1 #importing object form the Module
m.greeting("Good morning")
print(m.person1["name"])
print(platform.system())
print(dir(platform))#dir() to check built in functions in a module
print(person1["age"])
