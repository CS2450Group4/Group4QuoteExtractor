'''a class for geting text and writing text to a file
made by Matthew Snow on 9/18-9/21
'''
from docx import Document


class FileManager:
	'''returns the text in a text file'''
	def __TXT(filePath):
		file=open(filePath)
		fileText=file.read()
		file.close()
		return fileText
	
	
	'''returns the text in a word document'''
	def __DOCX(filePath):
		doc = Document(filePath)
		fullText = []
		for para in doc.paragraphs:
			fullText.append(para.text)
		
		return '\n'.join(fullText)
	
	'''returns the text in the file at "file path"'''
	def getText(filePath):
		fileExtention=filePath.split('.')[ len(filePath.split('.'))-1 ]
		if(fileExtention=="txt"):
			fileText=FileManager.__TXT(filePath)
			
		elif(fileExtention=="docx"):
			fileText=FileManager.__DOCX(filePath)
			
		else:
			'''trying to decide if we should full out throw an error here'''
			return"we can not open file of type "+fileExtention
		
		return fileText
		'''writes the given text into the file at file path(will over ride)'''
	def saveText(text, filePath):
		file=open(filePath,"w")
		file.write(text)
		file.close()

			
		
		
			
		