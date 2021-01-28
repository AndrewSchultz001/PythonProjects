import stdarray
import stdrandom
import stdio

# Create minuet 2D array with dimensions 11X16 and accept values through standard input
minuet = stdarray.create2D(11, 16, 0.0)
for i in range(len(minuet)):
    for j in range(len(minuet[i])):
        minuet[i][j] = stdio.readInt()

# Create trio 2D array with dimensions 6X16 and accept values through standard input
trio = stdarray.create2D(6, 16, 0.0)
for i in range(len(trio)):
    for j in range(len(trio[i])):
        trio[i][j] = stdio.readInt()

# Create a 1D array to store values from minuet and trio and a size variable to keep track of array
array = stdarray.create1D(32, 0.0)
size = 0

# Get 16 minuet values and storing it in array
for i in range(len(minuet[1])):
    # Create a sum variable to store sum from two roll dices
    sum = 0

    # Use stdrandom to 'roll' the dice and add to sum
    r = stdrandom.uniformInt(0, 6)
    f = stdrandom.uniformInt(0, 6)
    sum += r + f

    # Add value from minuet table to array
    array[size] = minuet[sum][i]
    size += 1

# Get 16 trio values and storing it in array
for i in range(len(trio[1])):
    # Use stdrandom to 'roll' on die
    r = stdrandom.uniformInt(0, 6)

    # Add value from trio table to array
    array[size] = trio[r][i]
    size += 1

# Print out values from array
for i in range(size):
    stdio.write(str(array[i]) + " ")

stdio.writeln()
