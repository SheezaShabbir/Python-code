#python has a built in module for json
#converting from json to python
import json
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
y=json.loads(x)
#python word
print(y["age"])
#converting from python to json
x={"name":"John", "age":30, "city":"New York"}
y=json.dumps(x)
#json string
print(y)
