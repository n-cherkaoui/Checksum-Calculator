# Calculates an 8, 16, or 32 bit checksum on an ASCII input file
#
# Author: Nawfal Cherkaoui Elmalki
# Language: Python3
#
# To Compile & Execute: python3 Checksum.py inputFile.txt 8
#
# where inputFile.txt is an ASCII input file
# and the number 8 could also be 16 or 32
# which are the valid checksum sizes, all
# other values are rejected with an error message
# and program termination
#
# Note: All input files are simple 8 bit ASCII input

from sys import argv

# Takes in and prints input file
def take_input():
  count = 0
  
  with open(argv[1]) as f:
    fileText = f.read()

  print("Message: ")
  for char in fileText:
    count+=1
    print(char, end='')
    if count % 40 == 0:
      print("")
    
  return fileText

# Driver function
def main():
  try:
    fileText = take_input()
  except IndexError:
    print("Please specify parameters.")
    return -1

  term = 0
  sum = 0
  k = int(argv[2])
  
  # Calculate the number of bytes per term based on the checksum size
  j_range = (k)//(2**3)
  
  x_count = 0

  # Calculate the checksum
  for i in range(0, len(fileText), j_range):
    
    for j in range(i, j_range+i):
      place_correction = 2**(8*(j_range-(j-i)-1))
      
      try:
        term += ord(fileText[j]) * place_correction
      except (IndexError):
        x_count+=1
        
        # If there is an error reading a byte from the input file,
        # replace it with an 'X' character and continue calculating the checksum
        term += ord('X') * place_correction

    sum+=term
    term = 0

  # Print the number of 'X' characters added to the input file to correct errors,
  # followed by the final checksum in hexadecimal format
  print('X' * x_count)
  
  sum = sum%2**int(argv[2])
  
  print('{} bit checksum is {} for all {} chars'.format(k, f'{sum:x}', len(fileText)+x_count))
  

main()
