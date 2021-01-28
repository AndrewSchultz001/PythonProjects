import rsa
import stdio
import sys


# Entry point.
def main():
    # Accept lo & hi as int command-line arguments
    lo = int(sys.argv[1])
    hi = int(sys.argv[2])

    # Send lo & hi through keygen function from rsa.py and set equal to array a
    a = rsa.keygen(lo, hi)

    # Print out value n, e, & d from variable a
    for i in range(len(a)):
        stdio.write(str(a[i]) + " ")
    stdio.writeln()


if __name__ == '__main__':
    main()
