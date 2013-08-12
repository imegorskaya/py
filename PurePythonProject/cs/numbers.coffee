#Assignments
number = 42
opposite = true

#conditions
number = -42 if opposite

#functions
square = (x) -> x * x

#array
list = [1,2,3,4,5]

#object
math =
  root: Math.sqrt
  square: square
  cube: (x) -> x * square x

#    splats
race =(winner, runners...) ->
  print winner, runners

####  existence
#alert "I knew it" if elvis ?

#array comprehension:
cubes = (math.cube num for num in list)###

