import os
import fitz
from components.text_parser import PdfParser


f_name = "data/report.pdf"

if __name__ == "__main__" :

    try :
        doc = fitz.open(f_name)
        pdfparser = PdfParser(doc=doc)
        #print(pdfparser.extract_structure())
        data = pdfparser.extract_structure()
        for d in data:
            print(f"{d['type']} : {d['text']}")
            print()
    except Exception as e:
        print(e)
    finally:
        doc.close()


