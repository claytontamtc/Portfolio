import string

mode = input("1 for table of contents, 2 for other ")
val = input("enter sentence ")
f = open('temp.txt', 'w')
f.write("")
f.close()

#table of contents
if (mode == "1"):
    f1 = open('temp.txt', 'a')
    page = 585
    #different fonts have different sizes
    #Number of tabs changes with each font type.
    char_tabs = "\t\t\t\t\t\t\t\t\t\t\t"
    #punctuation marks need one less tab to fit
    punc_tabs = "\t\t\t\t\t\t\t\t\t\t"
    for char in range(0, len(val)):
        if(val[char] == " "):
            #print('\" \"' + tabs + str(page) +  "\n")
            f1.write('\" \"' + punc_tabs + str(page) +  "\n\n")
        elif(val[char] in string.punctuation):
            #print('\"' + val[char] + '\"' + tabs + str(page) + "\n")
            f1.write('\"' + val[char] + '\"' + punc_tabs + str(page) + "\n\n")
        else:
            #print(val[char] + tabs + str(page) + "\n")
            f1.write(val[char] + char_tabs + str(page) + "\n\n")

        page += 1
    f1.close()

#normal writing
elif (mode == "2"):
    f2 = open('temp.txt', 'a')
    for char in range(0, len(val)):
        #print(val[char])
        f2.write(val[char] + "\n")
    f2.close()
