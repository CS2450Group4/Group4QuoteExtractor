from FileManager import FileManager
from ArticleExtractor import ArticleExtractor
from TextParser import TextParser
from newspaper import ArticleException
#declare variables
usrinput=""
textFile=""
quotes=[]
quoteStr=""
validInput=False

#start main
print("introduction statement")
#as we handle directory files slightly diferent from websites
print("would you like to input text from a file on your computer text from a website\n (C=computer, W=website)")
while(validInput==False):
	usrinput=input()
	if (usrinput.lower()=="c"):
		validFileName=False
		while(validFileName==False):
			try:
				#grab the text from the directory file
				print("what is the directory of the text file you want to grab quotes from?\n")
				filePath=input()
				textFile=FileManager.getText(filePath)
				validFileName=True
			except FileNotFoundError:
				print("we could not find the file you want to open, please check your spelling and try again")
			except PermissionError:
				print("we do not have acces to this file, please try a diferent file")
		validInput=True
	elif(usrinput.lower()=="w"):
		validURL=False
		while(validURL==False):
			try:
				#grab the text from the website
				print("what is the path to the website you want to grab quotes from?\n")
				URL=input()
				if(URL[:3].lower!="http"):
					URL="http://"+URL
				textFile=ArticleExtractor.extractArticleText(URL)
				validURL=True
			except ArticleException:
				print("there was an error grabbing that web page, please check your spelling and try again")
			
		validInput=True
	else:
		#they did not enter an input that was valid
		print("please enter either 'C' if you want to get your qoutes from your computer\nor 'W' if you want to grab your quotes from a website")
		validInput=False

#because word, and some websites do wierd things with their quots
textFile=textFile.replace("”","\"").replace("“","\"")

#process text		
quotes=TextParser.parseText(textFile)
for quote in quotes:
	quoteStr+=quote
	quoteStr+="\n\n"
#display quotes
print("here are the quotes\n\n")
print(quoteStr)


#ask if they want to save the file
validInput=False
while(validInput==False):
	print("would you like to save these quotes to a txt file?\n(y/n)")
	usrinput=input();
	if(usrinput.lower()=="y"):
		#save file
		print("where would you like to save the quotes to?")
		filePath=input()
		FileManager.saveText(quoteStr,filePath)
		validInput=True
	elif(usrinput.lower()=="n"):
		#print("no save")
		#dont save the file but continue
		validInput=True
	else:
		print("please enter a 'y' or a 'n' about weather or not you want to save the file")
		validInput=False
		

