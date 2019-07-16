
global outputstr

def PrintIsVowel(string):
    print (string)
    
def IsUppercaseVowel(inputchar):
    if (inputchar == 'A' or inputchar == 'E' or inputchar == 'I' or inputchar == 'O' or inputchar == 'U'):
        #print("Yipee! you entered a valid Uppercase vowel, " + inputchar)
        outputstr = "Yipee! you entered a valid Uppercase vowel, " + inputchar
        PrintIsVowel(outputstr)
        return True

def IsLowercaseVowel(inputchar):
    if (inputchar == 'a' or inputchar == 'e' or inputchar == 'i' or inputchar == 'o' or inputchar == 'u'):
        #print("Yipee! you entered a valid Lowercase vowel, " + inputchar)
        outputstr = "Yipee! you entered a valid Lowercase vowel, " + inputchar
        PrintIsVowel(outputstr)
        return True

def IsVowel(inputchar):
    if (IsUppercaseVowel(inputchar)) or (IsLowercaseVowel(inputchar)):
        #print("Yipee! you entered a valid vowel, " + inputchar+ " hope you like this game! if you are tired, type quit ")
        outputstr = "Yipee! you entered a valid vowel, " + inputchar+ " hope you like this game! if you are tired, type quit "
        PrintIsVowel(outputstr)
        return True
    else:
        #print("Great! however, " + inputchar + " is not a valid vowel, try again...")
        outputstr = "Great! however, " + inputchar + " is not a valid vowel, try again..."
        PrintIsVowel(outputstr)
        return False

    
def AskForLetter(inputstr):
    '''This function takes an input and validates 1. the length of the input and then 2. the input is an alphabet'''
    
    try:
        ret = len(inputstr) 
        if ret==1:
            if inputstr.isalpha():
                #print("Good you input a valid alphabet, " + inputstr)
                outputstr = "Good you input a valid alphabet, " + inputstr
                IsVowel(inputstr)
                PrintIsVowel(outputstr)
            else:
                #print("Oops! You did not enter an alphabet.")
                outputstr = "Oops! You did not enter an alphabet."
                PrintIsVowel(outputstr)
        elif ret ==4:
            if  inputstr == 'quit' or inputstr == 'Quit':
                print ("Quitting...")
                return False
            else:
                #print("Sorry, you entered a string of length ", ret, ". Just enter one character")
                outputstr = "Sorry, you entered a string of length ", ret, ". Just enter one character"
                PrintIsVowel(outputstr)
        else:
            #print("Sorry, you entered a string of length ", ret, ". Just enter one character")
            outputstr = "Sorry, you entered a string of length ", ret, ". Just enter one character"
            PrintIsVowel(outputstr)
        return True
    except:
        return True



user_input = input("Enter any letter ")
valid_input = AskForLetter(user_input)
while valid_input:
    user_input = input("Enter another letter ")
    valid_input = AskForLetter(user_input)
    outputstr = "what should I print?"
    
print ("Bye Bye!")


        
    
