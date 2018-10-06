from FileManager import FileManager
from ArticleExtractor import ArticleExtractor
from TextParser import TextParser
from newspaper import ArticleException

#declare variables
usrinput=""
textFile=""
quotes=[]
quoteStr=""
validInput = False
validFileName = False
FileFound = False
quotesFound = False

#start main
print("This program compiles quotes from an input source of text. \nCurrently supported sources of text are .docx files \nand websites containing articles.")


#as we handle directory files slightly diferent from websites
print("\nSelect the source your text will come from (D=.docx, W=Website): ")
while(validInput == False):

    #Read input into usrinput
	usrinput=input()

    #If the user chose a .docx file as the source...
	if (usrinput.lower()=="d"):

        #While the user 
		while(validFileName==False):
			try:
				#grab the text from the directory file
				print("\nEnter the directory your file is located in: \n(Tip: On Windows, you can paste to the Python shell by right-clicking on \nthe top of the Python shell window, hovering on 'edit', and selcting paste) \n")
				filePath=input()
				validFileName = textFile=FileManager.getText(filePath)
				validFileName=True

            #If the specified file was not found
			except FileNotFoundError:
				print("\nError: File could not be found. Please try again.")

            #If the program was denied access to the specified file
			except PermissionError:
				print("\nError: This program does not have permission to access the specified file. Please try again.")

		validInput=True

    #If the user chose a website as the source...
	elif(usrinput.lower()=="w"):
		validURL=False

		while(validURL==False):
			try:
				#grab the text from the website
				print('\nEnter the URL of the webpage containing the article: \n(Tip: On Windows, you can paste to the Python shell by right-clicking \non the top of the Python shell window, hovering on "edit", and selcting paste)\n')
				URL=input()
				textFile=ArticleExtractor.extractArticleText(URL)
				validURL=True

			except ArticleException:
				print("\nError: Webpage could not be found. Please try again.")
			
		validInput=True

	else:
		#they did not enter an input that was valid
		print("Error: Invalid input\nSelect the source your text will come from (D=.docx, W=Website): ")
		validInput = False

#because word, and some websites do wierd things with their quotes
textFile=textFile.replace("”","\"").replace("“","\"")

#process text		
quotes=TextParser.parseText(textFile)

#Add newlines between each quote
for quote in quotes:
	quoteStr+=quote
	quoteStr+="\n\n"

#If no quotes were found...
if (len(quoteStr) == 0):
    print ("\nNo quotes found in text")

#display quotes
else:
    print("\nQuotes Found:\n\n")
    print(quoteStr)
    quotesFound = True

if (quotesFound == True):

    #ask if they want to save the file
    validInput = False
    while(validInput==False):
	    print("\nWould you like to save these quotes to an existing .txt file? (Y/N)")
	    usrinput=input()

	    if(usrinput.lower()=="y"):
		    #save file
		    print("\nEnter the directory you would like to save the quotes to: \n(warning: In this program's current build, text file must already exist)")
		    filePath=input()
		    FileManager.saveText(quoteStr,filePath)
		    validInput=True


	    elif(usrinput.lower() == "n"):
		    validInput = True

	    else:
		    print("Error: Invalid input")
		    validInput=False


