#Daniel Bigelow ©2018
#Last Edited: 09/21/2018


#
#The text parser has only been tested as an individual program with test data, not a class function with a driver program. Should still work either way.
#
class TextParser:

    #parseText: Returns a list of strings containing all of the quotes found in the recieved string argument textBody
    @staticmethod
    def parseText(textBody):

        #String to hold a single open quote before it is closed and added to quoteList 
        quoteString = ""

        #List containing each quote in textBody
        quoteList = list()

        #quoteCount = no. quotes - 1
        quoteCount = -1

        #When an opening quotation mark is found, a 0 is pushed to stack. When a closing quotation mark is found
        stack = []

        i = 0

        #For every character in textBody
        while i < len(textBody):

            #If the current character is an opening quotation mark:
            if textBody[i] == "\"" and len(stack) == 0:

               #Push a 0 to the stack to indicate a quote is open
               stack.append('0')

               #Increment quoteCount
               quoteCount = quoteCount + 1

               #Add the quotation mark to quoteString
               quoteString = quoteString + textBody[i]
       
            #If the current quote is not closed:
            elif len(stack) != 0:
                #Add the current character to quoteString
                quoteString = quoteString + textBody[i]

                #If the current character is a closing quotation mark:
                if textBody[i] == "\"":

                    #Pop from stack to indicate the quote has been closed
                    stack.pop()

                    #add the full quote (quoteString) to the list of quotes (quoteList)
                    quoteList.append(quoteString) 

                    #Reset quoteString for a new quote
                    quoteString = ""
            
            #Move to the next character in textBody
            i = i + 1

        #If no quotes were found, raise an exception. No custom exception class right now, so it just prints out an error message
        if len(quoteList) == 0:

             #Error message for testing, remove from final build
             print("Error: No quotes found")
             # raise parsingError("Error while parsing text: No quotes found")

        #If an unclosed quote is found, print an error message. Doesn't throw an exception because some valid quotes were still found.
        if  len(stack) != 0:
            print ("Error: Unclosed quotation marks")
  
 
        return quoteList
