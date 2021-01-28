import stdaudio
import stdio
import sys

# Create an array called audio array and get values through standard input
audioArray = []
audioArray = stdio.readAllInts()

# Make sure length of audio array is 32
if len(audioArray) != 32:
    sys.exit("A waltz must contain exactly 32 measures")

# Use a for loop to check other possible errors
for i in range(len(audioArray)):

    # Make sure first 16 values are in the interval [1, 176]
    if i <= 15:
        if audioArray[i] < 1 or audioArray[i] > 176:
            sys.exit("A minuet measure must be from [1, 176]")

    # Make sure last 16 values are in the interval [1, 96]
    if i >= 16:
        if audioArray[i] < 1 or audioArray[i] > 96:
            sys.exit("A trio measure must be from [1, 96]")

for i in range(len(audioArray)):
    if i <= 15:
        stdaudio.playFile("data/M" + str(audioArray[i]))
    else:
        stdaudio.playFile("data/T" + str(audioArray[i]))
stdaudio.wait()
