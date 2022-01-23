from imaplib import Int2AP
import random
from re import X


def primary():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = 13
  rnd = random.randint(0, last)

  print(quotes[rnd],end="")
  print(quotes[random.randint(0, last)])

  #print(quotes)

def write():
  print("Now we'll add your favourtie quote to the list:\n")
  print("Enter a quote:")
  f = open("quotes.txt", "a")
  x = input()
  print(f"Inserting to file now!")
  quotes = f.write(x + "\n")

  f.close()
  print("\nInserted successfully!")

  
if __name__== "__main__":
  print("\n First we'll display a random quote from the file. Then, you can add your own quote to the file.")
  primary()
  write()