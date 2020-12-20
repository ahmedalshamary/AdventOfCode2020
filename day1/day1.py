''' 
Part 1, I used a dict to store the minus values and used those as indexes to look from on the second loop. This should find the solution twice.

Part 2 : Was a bit tricker since I thought that there should exist an optimal solution where you didn't either have to make a bunch of combinations in memory or loop through things a bunch of times. I couldn't think of anything so I just mad all the possible combinations in a list and then looped through them to find the write answer. There might be a better way but I am not that smart
'''

from itertools import combinations

# Stuff used for both solutions
number_array = []

file = open('input.txt', 'r')

for line in file:
	number_array.append(int(line))

# Part 1 Solution
minus_dict = {}

for line in number_array:
	index = 2020 - line
	minus_dict[index] = line

for line in number_array:
	if line in minus_dict :
		print("Part 1 solution")
		print(str(line * minus_dict[line]))
		break

# Part 2 Solution
combos = list(combinations(number_array, 3))
for combo in combos :
	if combo[0] + combo[1] + combo[2] == 2020 :
		print("Part 2 Solution")	
		print(combo[0]*combo[1]*combo[2])
		break

