import os

for root, dirs, files in os.walk( os.curdir ):

	print( "root = " + root )

	for file in files:
		print( "file = " + file )

	for dir in dirs:
		print( "dir = " + dir )

	print( "\n" )

input( '\n\nPress Enter to exit...' )
