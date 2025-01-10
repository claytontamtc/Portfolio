import string
import random
import json

"""
#replace word of length 5 with either Barry or Allen
def maybe_replace(word, alternate):
    if len(word) == 5:
        if(alternate == 1):
            return 'Barry'
        else:
            return 'Allen'
        
        #alternate word
        alternate = alternate * -1
        
    else:
        return word
"""

def b_or_a(alternate):
    if(alternate == 1):
        return "Barry"
    else:
        return "Allen"

#constants for use in program
Letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

reroll = ['z', 'q', 'j', 'x', 'k', 'v', 'b', 'y', 'w', 'g', 'p']

Punctuation = ['.', ',', ';', ':', '!', '?', '-', '...', '\'']

end_puncs = ['.', '!', '?', '-', '...']

chance = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


#keeps going until 2 is given for mode
while(True):
    #implement replacement from a list of random (hololive and common) words of a certain length
    mode = input("0 for fake random words, 1 for random words, and 2 to exit: ")
    #check for exit
    if(mode == "2"):
        print("Bye bye :)")
        break

    length_of_story = input("Enter length of story: ")

    barry = input("Barry? y or n: ")

    word_count = 0

    #creates a random word with random letters
    #the created word may not be a real word
    if(int(length_of_story) <= 0):
        print("Invalid story length.\n")


    #replace all 5 letter words with "Barry" and "Allen" alternating
    #eg. "Hi my name is Garth Simpson my first is third in range of winning"
    #becomes
    #    "Hi my name is Barry Simpson my Allen is Barry in Allen of winning"
    if(barry == 'y'):
        rep = open('randomStoryBarry.txt', 'w')
        rep.write("")
        rep.close()

        # 1 for "Barry"
        #-1 for "Allen"
        alternate = 1
    else:
        alternate = 0
        

    if(mode == "0"):
        #create text file
        f = open('randomStory.txt', 'w')
        f.write("")
        f.close()

        word = ""
        sentence_start = True
        f1 = open('randomStory.txt', 'a')
        if(barry == 'y'):
            rep = open('randomStoryBarry.txt', 'a')
                
        while(word_count < int(length_of_story)):
            #choose random letter
            new_letter = random.choice(Letters)
            #print(new_letter)

            #weighted chance towards more common letters
            #reroll if new_letter is in the bottom 11 most common letters
            #reroll = ['z', 'q', 'j', 'x', 'k', 'v', 'b', 'y', 'w', 'g', 'p']
            if(new_letter in reroll):
                new_letter = random.choice(Letters)
                #print("reroll")
                #print(new_letter)

            #makes letter captial if first letter in sentence
            if(sentence_start):
                word = word + new_letter.upper()
                sentence_start = False
            else:
                word = word + new_letter


            #"A" and "I" are the only valid one letter words
            #This makes sure that words that are length one, that aren't "A" or "I"
            #do not get printed to the text document
            if(len(word) == 1 and word != "A" and word != "I"):
                end_word = 10
            else:
                end_word = random.choice(chance)
                #print(end_word)
                
            #25% chance to end word
            #max length of word is 45
            if(end_word <= 5 or len(word) > 45):
                #append word to text file
                f1.write(word)

                #add text to barry file
                #replaces with 5 letter words with
                #an alternating "Barry" or "Allen"
                # 1 for "Barry"
                #-1 for "Allen"
                if(barry == 'y'):
                    if(len(word) == 5):
                        rep.write(b_or_a(alternate))
                        #alternate words
                        alternate = alternate * -1
                    else:
                        rep.write(word)
                                                    
                #add space or punctuation mark
                #and if a newline wasn't just added
                if((word_count + 1) < int(length_of_story)):
                    #randomly decide whether or not to add a puncuation mark
                    # 20% chance to add punctuation
                    punc = ""
                    add_punc = random.choice(chance)
                    #print(add_punc)

                    if(add_punc <= 4):
                        #choose random punctuation mark
                        punc = random.choice(Punctuation)
                        #print(punc)
                        f1.write(punc)

                        #add to barry text file
                        if(barry == 'y'):
                            rep.write(punc)
                    
                    #check if the next word is the start of a new sentence
                    if(punc in end_puncs):
                        sentence_start = True
                        
                        #random chance to start newline if punctuation mark is valid.
                        #35% chance to add a newline
                        new_line = random.choice(chance)
                        #print(new_line)
                        if(new_line <= 7):
                            f1.write("\n\n")
                            
                            #add to barry text file
                            if(barry == 'y'):
                                rep.write("\n\n")
                                
                        #add space instead of newline after   
                        else:
                            f1.write(" ")

                            #add to barry text file
                            if(barry == 'y'):
                                rep.write(" ")

                    else:
                        f1.write(" ")

                        #add to barry text file
                        if(barry == 'y'):
                            rep.write(" ")
                        
                #add ending punctuation for the last word
                else:
                    last_punc = random.choice(end_puncs)
                    #print(last_punc)
                    f1.write(last_punc)

                    #add to barry text file
                    if(barry == 'y'):
                        rep.write(last_punc)
                    

                # reset word to blank
                word = ""
                #increase word count of story
                word_count += 1

        f1.close()
        if(barry == 'y'):
            rep.close()
            

    elif(mode == "1"):
        #create text file
        g = open('randomStoryReal.txt', 'w')
        g.write("")
        g.close()
        
        #dictionary of random words where the keys are the words
        #and the values are all 1
        word_file = open("words_dictionary.json", 'r')
        word_list = json.load(word_file)

        """print(type(word_list))

        stop = 0
        for key, value in word_list.items():
            if(stop < 10):
                print(f"\nKey: {key}")
                print(f"Value: {value}\n")
                stop += 1
            else:
                break"""

        sentence_start = True
        selection = ""

        f2 = open('randomStoryReal.txt', 'a')
        if(barry == 'y'):
            rep2 = open('randomStoryBarry.txt', 'a')   
        
        while(word_count < int(length_of_story)):
            #chooses a random word from the dictionary
            selection = random.choice(list(word_list.keys()))
            #print(selection)

            #makes the firs letter captial if it's the first word in the sentence
            if(sentence_start):
                selection = selection.capitalize()
                sentence_start = False

            #append word to text file
            f2.write(selection)

            #add text to barry file
            #replaces with 5 letter words with
            #an alternating "Barry" or "Allen"
            # 1 for "Barry"
            #-1 for "Allen"
            if(barry == 'y'):
                if(len(selection) == 5):
                    rep2.write(b_or_a(alternate))
                    #alternate words
                    alternate = alternate * -1
                else:
                    rep2.write(selection)
                                       
            #add space or punctuation mark
            #and if a newline wasn't just added
            if((word_count + 1) < int(length_of_story)):
                #randomly decide whether or not to add a puncuation mark
                # 20% chance to add punctuation
                punc = ""
                add_punc = random.choice(chance)
                #print(add_punc)

                if(add_punc <= 4):
                    #choose random punctuation mark
                    punc = random.choice(Punctuation)
                    #print(punc)
                    f2.write(punc)

                    #add to barry text file
                    if(barry == 'y'):
                        rep2.write(punc)
                    
                #check if the next word is the start of a new sentence
                if(punc in end_puncs):
                    sentence_start = True
                        
                    #random chance to start newline if punctuation mark is valid.
                    #35% chance to add a newline
                    new_line = random.choice(chance)
                    #print(new_line)
                    if(new_line <= 7):
                        f2.write("\n\n")
                            
                        #add to barry text file
                        if(barry == 'y'):
                            rep2.write("\n\n")
                                
                    #add space instead of newline after   
                    else:
                        f2.write(" ")
                        
                        #add to barry text file
                        if(barry == 'y'):
                            rep2.write(" ")

                else:
                    f2.write(" ")

                    #add to barry text file
                    if(barry == 'y'):
                        rep2.write(" ")
                        
            #add ending punctuation for the last word
            else:
                last_punc = random.choice(end_puncs)
                #print(last_punc)
                f2.write(last_punc)

                #add to barry text file
                if(barry == 'y'):
                    rep2.write(last_punc)

                    
            #increase word count of story
            word_count += 1

        f2.close()
        if(barry == 'y'):
            rep2.close()
        #close json file    
        word_file.close()


    else:
        print("Invalid mode number")        
        

        """#replace all 5 letter words with "Barry" and "Allen" alternating
        #eg. "Hi my name is Garth Simpson my first is third in range of winning"
        #becomes
        #    "Hi my name is Barry Simpson my Allen is Barry in Allen of winning"
        #doesn't work as intended
        #don't know why
        #it randomly chooses which one to replace with
        #oh well
        if(barry == 'y'):
            rep = open('randomStoryBarry.txt', 'w')
            rep.write("")
            rep.close()

            # 1 for "Barry"
            #-1 for "Allen"
            alternate = 1
            rep = open('randomStoryBarry.txt', 'a')
            for line in open('randomStory.txt'):
                split_line = line.split()
                new_split_line = []
                for word in split_line:
                    if(alternate == 1):
                        new_split_line.append(maybe_replace(word, 1))
                    else:
                        new_split_line.append(maybe_replace(word, -1))
                    #print(new_split_line)
                    alternate = alternate * -1
                    #print(alternate)
                    
                new_line = ' '.join(new_split_line)
                rep.write(new_line + '\n')
            rep.close()
            
        else:
            rep = open('randomStoryBarry.txt', 'w')
            rep.write("No Barry Allen")
            rep.close()
        """
