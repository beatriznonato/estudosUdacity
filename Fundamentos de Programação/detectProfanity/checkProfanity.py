import urllib

def readText():
    quotes = open ("C:\Users\julio\OneDrive\Área de Trabalho\detectProfanity\movieQuotes.txt")
# open lê conteúdos de um arquivo no computador
    contentsOfFile = quotes.read()
    print(contentsOfFile)
    quotes.close()
    checkProfanity(contentsOfFile)

def checkProfanity(textToCheck):
    connection = urllib.urlopen('http://www.wdylike.appspot.com/?q='+textToCheck)
# urlopen estabelece uma conexão com um site na internet
    output = connection.read()
    print(output)
    connection.close()
    if 'true' in output:
        print('Profanity Alert!!!')
    elif 'false' in output:
        print('This document has no curse words!')
    else:
        print('Could not scan the document properly')

readText()
    
