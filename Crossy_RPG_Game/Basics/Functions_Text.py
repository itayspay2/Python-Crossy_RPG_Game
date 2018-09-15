# Python language basics 6
# Functions
# Implementing, calling, parameters, return values


x_pos = 0
e_x_pos = 4

print(x_pos)

# Function to increase x_pos by 1
def move():
    global x_pos   # must retrieve the global value
    x_pos += 1    # changes the value of the global x_pos

move()   # runs the code in the move function
# x_pos = 1

# Function to increase x_pos by 'amount'
def move_by(amount):
    global x_pos
    x_pos += amount

# Functions to check if player and enemy collide
# Output True if the collide and False if the dont

def check_for_collision():
    global x_pos
    global e_x_pos
    if x_pos == e_x_pos:
        return True
    else:
        return False



move_by(5) # need to pass in a value for 'amount'
# x_pos = 6
did_collide = check_for_collision()



print(x_pos)
print(did_collide)
