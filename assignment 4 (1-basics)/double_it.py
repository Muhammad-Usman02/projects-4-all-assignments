# Ask the user to enter a number
user_input = int(input("Enter a number: "))

# Initialize the current value
curr_value = user_input * 2  # First doubling

# Print the first doubled value
print(curr_value, end=' ')

# Continue doubling until value is 100 or more
while curr_value < 100:
    curr_value = curr_value * 2
    print(curr_value, end=' ')
