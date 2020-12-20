'''
Part 1 pretty straightforward, just loop through input and check if valid
Part 2 also straightforward, i wasted like  10 mins here because i used == instead of =, didn't realize cause no error message only wrong value.
'''

file = open('input.txt', 'r')

# Part 1 Solution

def is_valid_part1(min, max, password, char):
    count = password.count(char)
    if (count >= min and count <= max):
        return True

# Part 2 Solution
def is_valid_part2(pos_1, pos_2, password, char):
    bool_1 = password[pos_1] == char
    bool_2 = password[pos_2] == char
    return bool_1^bool_2


valid_count_1 = 0
valid_count_2 = 0    

for line in file:
    args = line.split()

    # Getting min, max , and positions that start at index 1 instead of 0
    nums = args[0].split("-")
    min = int(nums[0])
    max = int(nums[1])
    pos_1 = min - 1
    pos_2 = max - 1

    # Remove ":"
    char = args[1][0]

    password = args[2]

    valid_count_1 = valid_count_1 + 1 if is_valid_part1(min, max, password, char) else valid_count_1
    valid_count_2 = valid_count_2 + 1 if is_valid_part2(pos_1, pos_2, password, char) else valid_count_2

print(f"Part 1 : {valid_count_1}")
print(f"Part 2 : {valid_count_2}")