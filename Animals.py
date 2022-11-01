#####  Animal Guessing  #####
#### Jose Mancilla ####
### Artificial Intelligence ####

import sys

#Read file into the game
def readfile(file_Name):
    file = open('', "r")
    file.close()


#Funciton that creates a question
def NewQuestion(question, right, wrong):
  return [question, right, wrong]#Returns the three parameters in a list format for answers


#Function that prints each question from animals
#Returns the question [do i swim ¡?] first call
def AskQuestion(q):
  print ("%s " % q,)
  return sys.stdin.readline().strip().lower()


#Function that returns and checks the node
def CheckQuestion(node):
  return type(node).__name__ == "list"

#Funtion that takes the answer
#if the answer len is more than 0 then return just a y
#if not return false
def ReturnedYes(YesAns):
  if len(YesAns) > 0:
    return YesAns.lower()[0] == "y" #a yes or y will work
  return False


# Function that takes as parameter the question ['can i swim', 'shark','horse']
# if CheckQuestion true
def getAnswer(question):
  if CheckQuestion(question):
    return AskQuestion(question[0]) #can i swim?
  else: #
    return AskQuestion("Is your animal a %s?" % (question)) #if the animal swims this is a shark if not its a hosrse



#Function to return final game
def FinalGame(final):
  print (final)#We have guessed the animal



#Function to print question to start again
#calls returenedYes to check if the user wants to play again
#calls ask question to send the question
def NewGame():
  return ReturnedYes(AskQuestion("Play again? Yes/No "))


#Function Animal guessed takes a message to print since we have guessed correctly
#calls FinalGame function with the the message from FinalGame
def AnimalGuessed(Final):
  FinalGame(Final)
  if NewGame():#if new game true play a new game again with saved list
    return Data
  else:
    with open("animals.txt","a")as f:
        print(Data,file=f)
    sys.exit(0) #else exit the progrm

    #print (Data)#Returns the list with questions and animals



#Function if the animal is not guessed moved on to the next question
#takes a question and the animal of the user(answer)
def RightQuestion(question, animal):

  if CheckQuestion(question):
     #if the answer is yes to the question, 'can i swim?'
    if animal:
      return question[1] #return into the question 'am i a shark '
    else:
      return question[2] #since we can't swim return 'am i a horse'
#means we guessed the animal send a winning message to animak guessed
  else:
    if animal:#if the answer is yes means we found the animal
      return AnimalGuessed("Lets gooooo!, We guessed your animal!")#send final game the message
    else:#if answer to the question is your animal a shark is no then we need to add a question
      return AddNewQuestion(question)#call AddNewQuestion with the current question list





#Function takes tree parameters
#tree[0] hold the question
def FixTree(tree, lastAnimal, NewList):
  if not CheckQuestion(tree):
    if tree == lastAnimal:
      return NewList #return the new list[new question,the new input animal, the animal that 'was right']
    else:
      return tree
  else:
    return NewQuestion(tree[0],
      FixTree(tree[1], lastAnimal, NewList), #tree[1] holds the correct answer of the tree, if i swim is yes tree[1] is a shark
      FixTree(tree[2], lastAnimal, NewList))#tree[2] hold the other side of the tree, if I swim is yes tree[2] holds the horse



#fucntion takes a wrong choice of animal answer as parameter
def AddNewQuestion(OldAnimal):
  global Data #variables work outside of the function

#call ask question to recieve the animal the user was thinking
  NewAnimalRight = (AskQuestion("You win, What animal were you thinking about?"))

#Call ask question with the new animals sincw we got it wrong
  HelperQuestion = AskQuestion("Write a question that would differenciate %s from %s:"
  % (NewAnimalRight, (OldAnimal)))
#ask the question if the answer of the question is yes or no to check where is added on the list
  yes = ReturnedYes(AskQuestion("If we include this question in the game, " +
  "and your animal was %s, the answer would be Yes/No " % (NewAnimalRight)))

  # Create new question node
  #if the answer to the question is yes
  #return NewQuestion with correct animal in tree[1] which is the correct position
  #if answer to question is no means the wrong animal goes in tree[1]
  if yes:
    addtree = NewQuestion(HelperQuestion, NewAnimalRight, OldAnimal)
  else:#a no answer
    addtree = NewQuestion(HelperQuestion, OldAnimal, NewAnimalRight)

  # Create new tree and start over again
  Data = FixTree(Data, OldAnimal, addtree)
  return Data


#main
Data = (NewQuestion('Can I swim?', 'Shark', 'Horse')) #we can add the database of animals here
addtree = Data

print ("Welcome to Animal Guessing game!")
print ("Think about an animal and we will guess it!... eventually")


while True:
  UserAnswer = ReturnedYes(getAnswer(addtree))
  addtree = RightQuestion(addtree, UserAnswer)
