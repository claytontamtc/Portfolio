import string
import sys

#"0 for test, 1 for table of contents, 2 for other "
mode = input("0 for test\n1 for table of contents\n2 for review text\n3 for cancel\n")
#reads song names and data

#stop program
if(mode == "3"):
    sys.exit("Request Canceled")
    

#IMPORTANT NOTICE
#Non English Letters/Characters will crash the program
#Incorrect Quotation Marks will also crash the program

#each line is one song
n = open('songnameTitle.txt', 'r')

#table of contents
if (mode == "1"):
    #open shortened titles
    f1 = open('songformatT.txt', 'w')

    #add page numbers
    f3 = (open('pagenumbers', 'r')).readlines()

    L = n.readlines()

    # format song info for table of contents
    # Only the song name is needed

    index = 0
    while (index <len(L)):
        f1.write(L[index] + "\t" + f3[L])
        f1.write("\n\tArtist(s)\n\n")
        f1.write("\tDate Added\n\n")
        f1.write("\tReview\n\n")
        f1.write("\tOld Rating\n\n")
        f1.write("\tNew Rating\n\n")
        index += 1

    f1.close()

#normal writing
if (mode == "2"):
    f2 = open('songformatR.txt', 'w')
    # format song info for review
    # Ln == (full) song name
    Ln = (open('songname.txt', 'r')).readlines()
    # La == artist
    La = (open('songartist.txt', 'r')).readlines()
    # Lor == old rating
    Lor = (open('songoldr.txt', 'r')).readlines()
    # Lnr == new rating
    Lnr = (open('songnewr.txt', 'r')).readlines()
    # Ld == date added
    Ld = (open('songdate.txt', 'r')).readlines()
    
    index2 = 0
    while (index2 < len(Ln)):
        #Manually center align when you get to writing the review
        f2.write("Song:\n")
        f2.write(Ln[index2])
        f2.write("\n\n\n\n")
        
        f2.write("Artist(s):\n")
        f2.write(La[index2])
        f2.write("\n\n\n\n")

        f2.write("Date Added:\n")
        f2.write(Ld[index2])
        f2.write("\n\n\n\n")

        f2.write("Review:\n\nIt good song.\n\n\n\n")

        
        f2.write("Old Rating:\n")
        #Different prints for if the score is a decimal number
        #Score is an int
        #Removes trailing newline
        if(Lor[index2].strip().isdigit()):
            #print(Lor[index2])
            f2.write(Lor[index2].strip() + " / 10\n")
        #Score is not an int
        else:
            f2.write(str(float(Lor[index2].strip())) + " / 10\n")
            
        f2.write("\n\n\n\n")
        

        f2.write("New Rating:\n")
        #Different prints for if the score is a decimal number
        #Score is an int
        #Removes trailing newline
        if(Lnr[index2].strip().isdigit()):
            #print(Lnr[index2])
            f2.write(Lnr[index2].strip() + " / 10\n")
        #Score is not an int
        else:
            f2.write(str(float(Lnr[index2].strip())) + " / 10\n")
            
        f2.write("\n\n\n\n")

        
        index2 += 1

    #Ln.close()
    #La.close()
    #Lor.close()
    #Lnr.close()
    #Ld.close()
    f2.close()

n.close()

