import PyPDF4
import slate3k as slate 

documentName = 'document.pdf'

with open(documentName, 'rb') as f:
    extracted_text = slate.PDF(f)
with open("names.txt") as n:
    names = [name.rstrip() for name in n]
pageNumber = len(extracted_text)

print ("Document :", documentName)
print ("Nombre de pages :", pageNumber)
print("-------------------------------------------------")

for name in names :
    print ("Mot recherché :", name)
    for pageIndex in range (0, len(extracted_text)) :
        if (extracted_text[pageIndex].find(name) != -1) :
            print (pageIndex)
        else :
            print("false")
            
f.close()
n.close()
