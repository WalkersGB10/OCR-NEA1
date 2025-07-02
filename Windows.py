#imports
import winsound
from random import randint
import sys

#setup
qs = {}
chances = 2
score = 0

#functions
def encrypt(password):
  newpassword = ""
  char = "abcdefgjijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
  for i in password:
    pos = char.index(i)
    if pos > (len(char)-6):
      newpassword += char[pos-(len(char)-6)]
    else:
      newpassword += char[pos+6]
  return newpassword


def login(user):
  f = open("Users.txt", "r")
  contents = f.read()
  f.close()

  contents = contents.split("\n")
  for i in range(0, len(contents)):
    contents[i] = contents[i].split(":")

  password = input("Password: ")
  password = encrypt(password)

  for i in contents:
    if user in i:
      if password == i[1]:
        print("Welcome")
        return
  print("Incorrect username or password")
  sys.exit()


#main
user = input("Username: ")
login(user)
f = open("Questions.txt", "r")
contents = f.read()
f.close()

contents = contents.split("\n")
for i in range(0, len(contents)):
  contents[i] = contents[i].split(":")

while chances > 0:
  question = randint(0, len(contents)-1)
  pair = contents[question]

  print("\nArtist:", pair[1])
  print("Song initials: ")
  for i in pair[0].split():
    print(i[0], end=" ")

  winsound.PlaySound(pair[0]+".wav", winsound.SND_FILENAME | winsound.SND_ASYNC)

  
  while chances > 0:
    answer = input("\nWhat is the song name?").lower()
    if answer == pair[0].lower():
      if chances == 2:
        score +=3
      else:
        score += 1
      print("Correct")
      chances = 2
      break
    else:
      print("Incorrect")
      chances -= 1
print("The correct answer was:", pair[0])

print("Your final score was:", score)

f = open("Highscores.txt", "r")
highscores = f.read().split("\n")
f.close()

for i in range(0, len(highscores)):
  highscores[i] = highscores[i].split(":")


for i in range(0, len(highscores)):
    if score > int(highscores[i][1]):
        highscores.pop()
        highscores.pop()
        highscores.insert(i, [user, str(score)])
        break

f = open("Highscores.txt", "w")
for i in range(0, len(highscores)):
  f.write(highscores[i][0] + ":" + highscores[i][1] + "\n")
  print(str(i+1), " :", highscores[i][0], highscores[i][1])
f.close()
