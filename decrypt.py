import rsa
import stdio
import sys


# Entry point.
def main():
    # Accept n & d as int command-line arguments
    n = int(sys.argv[1])
    d = int(sys.argv[2])

    # Get number of bits(n) and make it equal to width
    width = rsa.bitLength(n)

    # Get message string form standard input
    message = stdio.readString()

    # Increment by width from [1, len(message)-1]
    for j in range(1, len(message) - 1, width):
        # Set s to a substring of message from i to i + width
        s = message[j - 1: j + width - 1]

        # Set y to decimal representation of s
        y = rsa.bin2dec(s)

        # decrypt y
        y = rsa.decrypt(y, n, d)

        # Print out the character got from decrypting y
        stdio.write(chr(y))


if __name__ == '__main__':
    main()
