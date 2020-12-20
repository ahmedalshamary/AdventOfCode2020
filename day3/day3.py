'''
Part 1: 
First Thoughts on this one is that it is a tad tricker then the day1 & day2. 
Quick way to do this is just to use a modulus for the width and loop through till we are done with the height, at each value just see what value we had there. 

Part 2: 
Seems to be really straightforward, we just need to wrap the current thing we did for part 1 into a function and pass values to it. 

I messed up a bit by not entering the right values for the right value, I entered 6 instead of 5 had to copy and paste the input to figure out what was wrong.
'''

file = open('input.txt', 'r')

# Double Array that we read everything into
tree_map = []
map_height = 0
map_width = 0
for line in file:
	tree_map.append(line.strip())
	map_height += 1

map_width = len(tree_map[0])

h_counter = 0
w_counter = 0
t_counter = 0

while(h_counter < map_height - 1) :
	# Go down one
	h_counter += 1
	# Go right 3, if necessary add and then take the modulus value
	w_counter = w_counter + 3 if w_counter + 3 < map_width else (w_counter + 3) % map_width
	# Is tree here
	if tree_map[h_counter][w_counter] == '#' :
		t_counter += 1

print(f"Part 1 solution: {t_counter}")


# Part 2

def tree_counter(tree_map, right, down):
	map_width = len(tree_map[0])
	h_counter = 0
	w_counter = 0
	t_counter = 0

	while(h_counter < map_height - down) :
		# Go down
		h_counter += down
		# Go right
		w_counter = w_counter + right if w_counter + right < map_width else (w_counter + right) % map_width
		# Is tree here
		if tree_map[h_counter][w_counter] == '#' :
			t_counter += 1

	return(t_counter)

'''
	Slopes to test
    Right 1, down 1.
    Right 3, down 1. (This is the slope you already checked.)
    Right 5, down 1.
    Right 7, down 1.
    Right 1, down 2.
'''

val_1 = tree_counter(tree_map, 1, 1)
val_2 = tree_counter(tree_map, 3, 1)
val_3 = tree_counter(tree_map, 5, 1)
val_4 = tree_counter(tree_map, 7, 1)
val_5 = tree_counter(tree_map, 1, 2)

solution = val_1 * val_2 * val_3 * val_4 * val_5
print(f"Part 2: {solution}")