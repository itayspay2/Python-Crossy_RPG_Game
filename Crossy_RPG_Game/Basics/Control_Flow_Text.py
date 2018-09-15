# Python language basics 4
# control flow
# if statements

is_game_over = False
p_0_x_pos = 0
e_0_x_pos = 3
e_1_x_pos = 5

p_0_x_pos += 2  # p_0_x_pos = 2
if p_0_x_pos == e_0_x_pos:  # False so skip code below
    is_game_over = True
elif p_0_x_pos == e_1_x_pos:  # False so skip code below
    is_game_over = True
else:   # Carried out if all above tests fail to execute
    e_0_x_pos += 1
    e_1_x_pos += 1




## Another way below





if p_0_x_pos == e_0_x_pos or p_0_x_pos == e_1_x_pos:
    is_game_over = True
else:   # Carried out if all above tests fail to execute
    e_0_x_pos += 1
    e_1_x_pos += 1    
    
# Python language basics 5
# while loops
# for in loops

is_game_over = False
p_x_pos = 2
e_x_pos = 3
end_x_pos = 10

while not is_game_over:
    print(p_x_pos)
    print(e_x_pos)
    if p_x_pos == e_x_pos:
        print('you lose')
        is_game_over = True
    elif p_x_pos >= end_x_pos:
        print('you win')
        is_game_over = True
    else:
        p_x_pos += 3
        e_x_pos += 1

x_pos = 5
movements = [1, -2, 6, -3, -2, 4]

for movement in movements:
    x_pos += movement
print(x_pos) 
