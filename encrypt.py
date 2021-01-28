import rsa
import stdio
import sys


# Entry point.
def main():
    # Accept n & e as int command-line arguments
    n = int(sys.argv[1])
    e = int(sys.argv[2])

    # Get length number of bits per character needed for encryption and set it equal to width
    width = rsa.bitLength(n)

    # Get value of standard input string and set it equal to message
    message = stdio.readAll()

    for i in message:
        # Set x value to ord(i)
        x = ord(i)

        # Encrpyt x
        x = rsa.encrypt(x, n, e)

        # Print out width-long encrypted value as a binary string
        stdio.write(rsa.dec2bin(x, width))
    stdio.writeln()


if __name__ == '__main__':
    main()
