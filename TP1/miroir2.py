import sys

phrase_invers = ""

for arg in sys.argv[1:] :
   phrase_invers += "".join(reversed(arg))
   phrase_invers += " "

print(phrase_invers)