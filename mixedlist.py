#combine two lists
numers=[1,10,9,6,2]
words=['a','a','a','a','a']
numers.extend(words)
print(numers)
#concatenate cities
alllist=numers+words
for w in alllist:
    print(w)
#reverse list
words.reverse()
print(words[-1])

#sort and sorted method
quiz_scores = [20, 19, 20, 15, 20, 20, 20, 18, 18, 18, 19]
quiz_scores.sort()
print(quiz_scores)

game_points = [3, 14, 0, 8, 21, 1, 3, 8]
sorted_points = sorted(game_points)
print(sorted_points)
#split methood
line="I am waiting for a long time."
linenew=line.split()
print(linenew)
for i in linenew:
    print(i)
#split method for splitting characters:
linenew=line.split('a')
print(linenew)
linenew=line.split('\n')
for i in linenew:
    print(i)
#join method to join a new string with the list
name=['S','H','E','E','Z','A']
nospace=""
print(nospace.join(name))
name=['S','H','E','E','Z','A']
star="**\n"
print(star.join(name))

