
import array

str = 'My name is Kevin'

print( 'str = ' + str )

# We're not allowed to modify strings so we'll need to convert it to a
# character array instead...

charArray        = array.array( 'B', str )     # assignment
charArray[11:16] = array.array( 'B', 'Jason' ) # replacement

str = charArray.tostring() # assignment back to the string object

print( 'str = ' + str )

input( '\n\nPress Enter to exit...' )
