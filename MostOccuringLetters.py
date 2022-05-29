##Makind an array to add the already found most occuring alphabet
foundLetters=[" "]

##the input string
s="Python ist sooo eine tolle Programmiersprache!"

#multiple inputs to test. Comment out all other 's' variables except the one you want to use as input
#s="aaaabbbbbccccdddddddeeee"
#s="Heeeellllooooooooooo"
#s="aar you fineee?"

#This function takes @param input String, converts into charater array and sorts the array
#Then calls the findMostOccuring function to find the most occuring alphabet
def mostOccuring3Letters(input):
    
    #converting string into array
    arrayLetters=[""]
    for alphabet in input:
        arrayLetters.append(alphabet)
        
    #get length of array
    arrLen=len(arrayLetters)
    
    #double loop linear travesal used to sort the array
    for letter in range(arrLen):
        for start in range(letter+1,arrLen):
            if arrayLetters[letter]>arrayLetters[start]:
                arrayLetters[letter],arrayLetters[start]=arrayLetters[start],arrayLetters[letter]
    
    
    #found called each time after finding the most occuring letter and then adding that letter to the FoundLetters array
    firstMax=findMostOccuring(arrayLetters)
    secondMax=findMostOccuring(arrayLetters)
    thirdMax=findMostOccuring(arrayLetters)
    
    #Printing the solution
    print("Die drei häufigsten Zeichen sind {}, {} und {}.".format(firstMax,secondMax,thirdMax))
    
#Prints the most occuring alphabet in the array and then adds it to the foundLetters array so that letter is skipped the
    #following times the function is called
def findMostOccuring(arrayLetters):
    max = 1
    
    result = arrayLetters[0]
    count=1;
    
    #travesal of the array from 1 to length of array - 1
    for i in range(1,len(arrayLetters)):
        #check if this alphabet has already been found
        if(arrayLetters[i] not in foundLetters ):
            #check if the next letter is equal to the preceding letter as the array is sorted to same letters are together
                if ( arrayLetters[i] == arrayLetters[i - 1]):
                    #if letters the same then add 1 to count
                    count += 1
                else:
                    #set count back to 1 and new letter not the same as the preceding
                    count = 1
                #check if new count is greater than the max count already found
                if (count > max):
                    #make max to be the count and assign the letter as result
                    max = count
                    result = arrayLetters[i-1]
    
    #add foundLetter to the foundLetters array
    foundLetters.append(result)
    #return the result
    return result

    
    
#run the main mostOccuring3Letters function 
mostOccuring3Letters(s)
