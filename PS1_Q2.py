# Question: On a computer, check when you can no longer add a small floating point number to 1.0. Start by
# calculating 1.0 + 1.0 and then decrease the value being added by an order of magnitude each time,
# so you calculate 1.0 + 0.1, 1.0 + 0.01, etc. This should give you an indication of the number of bits
# being used in your floating point representation. Can you find the smallest representable real value
# greater than 1?



# Initialize the starting value
epsilon = 1.0

# Loop to find the smallest representable real value greater than 1.0
while (1.0 + epsilon) != 1.0:
    smallest_epsilon = epsilon  # Store the previous epsilon value
    epsilon /= 2  # Decrease an order of magnitude of the epsilon value

# Output the smallest representable real value greater than 1.0
print("The smallest representable real value greater than 1.0 is:", smallest_epsilon)
print('Difference with theoretical value 2^-52',smallest_epsilon-2**-52)
