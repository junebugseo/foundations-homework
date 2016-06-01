# June Jeongwon Seo
# 2016-05-25
# Homework 2

#LIST
#1
numbers = [22, 90, 0, -10, 3, 22, 48]
print (len(numbers))

#2
print (numbers[3])
#3
print (numbers[1]+numbers[3])
#4
print (sorted(numbers)[5])
#5
print (numbers[6])

#6
print ("THE LOOP STARTS!")

for x in numbers:
    if x < 10:
        x = 30*x
    if x%2 == 0:
        x = x+6
    if x > 50:
        x = x-10
    if x == -10:
        x = x
    else:
        x = x-1
    print x

#7 Sum the result of each of the numbers divided by two.


#DICTIONARIES
#8
movie = {'title': 'Garden State','year': 2004,'director': 'Zac Braff','budget': 'unknown'}
print ("My favorit movie is", movie['title'], "which was released in", movie['year'], "and was directed by" ,movie['director'])

#9
movie = {'title': 'Garden State','year': 2004,'director': 'Zac Braff','budget': 2500000, 'revenue': 36000000}
print (movie['revenue']-movie['budget'])

#10
if movie['revenue']<movie['budget']:
    print ("It was a flop")
elif movie['revenue']>5*movie['budget']:
    print ("That was a good investment")

#11
boropop = [
    {'boro': 'Manhattan', 'pop': 1600000},
    {'boro': 'Brooklyn', 'pop': 2600000},
    {'boro': 'Bronx', 'pop': 1400000},
    {'boro': 'Queens', 'pop': 2300000},
    {'boro': 'Staten Island', 'pop':470000}
]

#12
print (boropop[1]['pop'])

#13
sumpop = 0
for x in range(0,len(boropop)):
    sumpop = sumpop + boropop[x]['pop']
print sumpop

#14
print (boropop[0]['pop']/8370000)
