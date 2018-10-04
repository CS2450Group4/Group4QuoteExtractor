from FileManager import FileManager
from ArticleExtractor import ArticleExtractor
from TextParser import TextParser


print("*****\n\n test.docx text \n\n*****")
print(FileManager.getText("test.docx"))
print("*****\n\n hi.txt \n\n*****")
print(FileManager.getText("hi.txt"))
print("*****\n\n test parseText \n\n*****")
print(TextParser.parseText("\"this is a quote\", this is not a quote \"this is another quote\n with a newline in the middle\""))
print("*****\n\n test article extractor \n\n*****")
print(ArticleExtractor.extractArticleText("http://www.keepinspiring.me/famous-quotes/"))

