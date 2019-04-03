#Hangman
#by Matthew Magardino



import random



"""
useful to make string into a list of chars
returns list (of string inputted)
"""
def OLDstringToList(s):
    l = [];
    for i in range(len(s)):
        l.append(s[i]);
    return l;

def stringToList(s):
    return list(s);


"""
useful to take list of chars and make a string
returns string (of chars from list inputted)
"""
def OLDlistToString(l):
    s = "";
    for i in range(len(l)):
        s += l[i];
    return s;

def listToString(l):
    return "".join(l);



"""
welcome window
returns decision (new game or continue)
"""
def welcome():
    print("____________________");
    print("\nWelcome Player!");
    print("\t1: Start New Game");
    print("\t2: Quit");
    print("____________________");
    ans = int( input("Select an option: ") );
    return ans;



"""
gets a random word from the dictionary
returns a string (the random word)
"""
def getRandomWord():
    special = ["chipotle", "finance", "trash", "medicine", "code", "amazon"]
    dict = [];
    file = open('data/dictionary.txt','r').read().split('\n');
    for line in file:
        dict.append(line);
    index = random.randint( 0 , len(dict)-1 );
    return dict[index];



"""
creates the beginning blanks from the random word chosen
returns string of blanks fitted to answer size
    (2 * size of answer because spaces between blanks)
"""
def makeBlanks(word):
    length = len(word);
    s =[];
    for i in range(0, length * 2, 1):
        if (i % 2 == 0):
            s.append('_');
        else:
            s.append(' ');
    spaces = listToString(s);
    return spaces;



"""
prints the progress, guesses, and lives remaining
"""
def showCurrentState(life, progress, guesses):
    guessed = ""
    for i in range( len(guesses) ):
        guessed += guesses[i];
        guessed += " ";
    print("\nLives: {}".format(life) );
    printBody(life);
    print("Progress: " + progress );
    print("Previous Guesses: " + guessed);



"""
prints a visual of the hangman (stick figure)
"""
def printBody(lives):
    s5 = "|----!\n|\n|\n|\n|\n|_____"
    s4 = "|----!\n|    O\n|\n|\n|\n|_____"
    s3 = "|----!\n|    O\n|   /|\\\n|\n|\n|_____"
    s2 = "|----!\n|    O\n|   /|\\\n|    |\n|\n|_____"
    s1 = "|----!\n|    O\n|   /|\\\n|    |\n|   /\n|_____"
    s0 = "|----!\n|    O\n|   /|\\\n|    |\n|   / \\\n|_____"
    if (lives == 5):
        print(s5);
    elif(lives == 4):
        print(s4);
    elif(lives == 3):
        print(s3);
    elif(lives == 2):
        print(s2);
    elif(lives == 1):
        print(s1);
    else:
        print(s0);



"""
checks to see if new guess is a duplicate
returns true or false
"""
def checkDuplicateGuess(guess, prevGuesses):
    for i in range(len(prevGuesses)):
        if (guess == prevGuesses[i]):
            return True;
    return False;



"""
checks to see if new guess is in the answer
returns true or false
"""
def checkCorrectGuess(currentGuess, answer):
    for i in range(len(answer)):
        if (currentGuess == answer[i]):
            return True;
    return False;



"""
updates progress by filling in blanks
returns new string of progress (blanks and chars separated by spaces)
"""
def updateBlanks(guess, ans, blanks):
    newBlanks = stringToList(blanks);
    for i in range(len(ans)):
        if (guess == ans[i]):
            newBlanks[i*2] = guess;
    stBlank = listToString(newBlanks);
    return stBlank;



"""
checks if progress is complete ( == to answer)
returns true or false
"""
def checkComplete(answer, progress):
    currentAns = "";
    for i in range(len(progress)):
        if (i % 2 == 0):
            currentAns += progress[i];
    if (currentAns == answer):
        return True;
    else:
        return False;



"""
begins game with new word, new blanks
calls run with new setup
"""
def begin():
    answer = getRandomWord();
    blankSetup = makeBlanks(answer);
    run(answer, blankSetup);



"""
runs entire game until either complete word or lose 5 lives
    iterates the following:
        - shows state of game
        - gets new guess
        - checks to see if duplicate
        - if not, add to previous guesses and check if guess is in answer
        - update progress if correct, lose life if not
        - check if finished the word
        - if out of lives or complete word --> gameover
"""
def run(ans, blanks):
    progress = blanks;
    lives = 5;
    notFinished = True;
    guessedLetters = [];
    while(lives > 0 and notFinished):
        showCurrentState(lives, progress, guessedLetters);
        thisGuess = input("\nGuess a letter: ");
        thisGuess = thisGuess.lower();
        duplicateGuess = checkDuplicateGuess(thisGuess, guessedLetters);
        if (duplicateGuess):
            print("\nAlready Guessed: " + thisGuess);
        else:
            guessedLetters.append(thisGuess);
            correctGuess = checkCorrectGuess(thisGuess, ans);
            if (correctGuess):
                print("____________________");
                print("\n\tNice Guess!");
                progress = updateBlanks(thisGuess, ans, progress);
            else:
                print("____________________");
                print("\n\tOuch!");
                lives -= 1;
        isComplete = checkComplete(ans, progress);
        if(lives == 0 or isComplete):
            notFinished = False;
    if (lives == 0):
        loss = False;
        gameover(loss, lives, ans);
    else:
        win = True;
        gameover(win, lives, ans);



"""
prints result of game and the final answer
"""
def gameover(iWon, lives, ans):
    if(iWon):
        print("____________________");
        for i in range(10):
            print("CONGRATS!!! :) ");
    else:
        print("____________________");
        for i in range(10):
            print("Better luck next time :( ");
    printBody(lives);
    print("Answer: " + ans);



"""
main function
begins with welcome window and logic for decision (start game or goodbye)
"""
def main():
    stage = welcome();
    while(stage != 2):
        if(stage == 1):
            begin();
        else:
            print("\nIncorrect input :( ");
            print("Try again");
        stage = welcome();
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~\n\tGoodbye!!");
    print("By Matthew Magardino <3\n~~~~~~~~~~~~~~~~~~~~~~~~~");
    print("\n\n");





main();




#end of hangman
