# Aim:
# Generate ANDNOT function using McCulloch-Pitts Neural Network

# Define input combinations
inputs = [
    [1, 1],
    [1, 0],
    [0, 1],
    [0, 0]
]

# Define weights
w1 = 1
w2 = -1

# Define threshold
theta = 1

print("w1 =", w1)
print("w2 =", w2)
print("Threshold =", theta)

print("\nX1  X2  Yin  Output")

# Process each input combination
for x1, x2 in inputs:

    # Calculate activation value
    yin = (w1 * x1) + (w2 * x2)

    # Apply threshold condition
    if yin >= theta:
        y = 1
    else:
        y = 0

    # Display result
    print(x1, " ", x2, " ", yin, "   ", y)