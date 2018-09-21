from FileManager import FileManager
print("input the directory of a text file")
filePath=input()
fileText=FileManager.getText(filePath)
fileText=fileText+"this is an added on text"
print("input where you want it saved")
filePath=input()
FileManager.saveText(fileText,filePath)