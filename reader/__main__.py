# import sys from the python repository
import sys

# import the reader module from the reader package
import reader

# read file in sys path with the reader class and close at the end
r = reader.Reader(sys.argv[1])
try:
    print(r.read())
finally:
    r.close()
