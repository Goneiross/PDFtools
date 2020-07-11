import PyPDF4
import slate3k as slate 
import os
import logging

logging.propagate = False 
logging.getLogger().setLevel(logging.ERROR)

def findWords(documentName) :
    with open(documentName, 'rb') as f:
        extracted_text = slate.PDF(f)
    with open("names.txt") as n:
        names = [name.rstrip() for name in n]
    pageNumber = len(extracted_text)
    print ("Document :", documentName)
    print ("Nombre de pages :", pageNumber)
    print("-------------------------------------------------")

    for name in names :
        pages = []
        for pageIndex in range (0, len(extracted_text)) :
            if (extracted_text[pageIndex].find(name) != -1) :
                pages.append(pageIndex + 1)
        if (pages != []) :
            print ("Mot trouvé :", name)
            print (pages)
    f.close()
    n.close()

def main():
    documentNames = []
    dir_path = os.path.dirname(os.path.realpath(__file__))
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.endswith('.pdf'):
                print(file)
                documentNames.append(file)
    for documentName in documentNames :
        print ("Document :", documentName)
        findWords(documentName)

main()