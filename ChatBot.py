#Chat Bot Class
__author__ = 'William Cleghorn'
__version__ = '0.01'
__lastEditDate__ = '3.9.18'

class ChatBot:
  
  def __init__(self):
    self.name = ''
    
    """
    
    These are the ChatBot's conversation checks and responses, these are simple checks and responses and don't legitimately communicate but rather just give a responses
    later plan to add sentence comprehension, topics, train of thought, later use web scraping to pull information about topics. Robot will not form opinions so when asked a
    question it doesn't have an opinion on it will say something along the lines of "i cant say much about that"
    
    """
    self.checkLibrary =[greetingChecks, goodbyeChecks]
    self.responseLibrary = [greetingResponse, goodbyeResponse]
    self.youLibrary = [youChecks] """Add checks for statements talking to the chatbot itself""" 
    """ Expanded libraries for greetings and goodbyes"""
    self.greetingChecks = [0,"hi", "hey", "hello", "yo", "wassup"]
    self.greetingResponse = [0,"hi", "hey", "hello", "greetings earthling"]
    self.youChecks = [0, "you", "pybot", "chatbot"] """dictionary for youLibrary, can be expanded"""
    self.goodbyeChecks = [0, "goodbye", "bye", "see you later", "see you", "cheerio"] 
    self.goodbyeResponse = [0, "bye", "bye bud", "see yah fam", "bye my nig nog", "see you in hell"]
  def respond(self, check, response, strInput):
  
    
    #Add String spacings
    strInput = " " + strInput + " "
    check = " " + check + " "    
    
    
    #Checks in string for word
    if check in strInput:
      return response;
    else:
      return "sorry i cant respond to that";
    
    
  def respondDict(self, checkDict, responseDict, inStr):
    
    for x in range (0, len(checkDict)):
      
      if checkDict[x] in inStr:
        
        return respondDict[randrange(0, len(respondDict))];
                                     
  def analyzeString(self, checkLibrary, responseLibrary, string):
    pass
  
   def input(self, youLibrary): """Input and check for statemetns directly addresssing the program (NO idea what tf im doing, just modeling after what you did)"""
      for x in range (0, len()):
        if checkInsen[x] in youLibrary:
          respondYou = "Are you talking to me, fatty?"
          return respondYou;
    
