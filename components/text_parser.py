import os
import sys
import json
import fitz
import random



SAMPLE_PAGES_NUM = 4

class PdfParser:
    def __init__(self, doc) -> None:
        self.doc = doc
        


    def get_para_font_details(self):
        page_data = []
        font_sizes = []
        font_styles = []
        
        random_numbers = [random.randint(0, self.doc.page_count-1) for _ in range(SAMPLE_PAGES_NUM)]

        sample_pages = list(map(lambda x: self.doc[x], random_numbers))

        for sample_page in sample_pages:
            txt = sample_page.get_text("json")
            raw_data = json.loads(txt)
            for block in raw_data['blocks']:
                try:
                    for line in block['lines']:
                        for span in line['spans']:
                            #print(f"Font size : {span['size']} | Style : {span['font']} | Text : {span['text']}")
                            page_data.append({
                                'font_size' : span['size'],
                                'font_style' : span['font'],
                                'text' : span['text']
                            })
                            font_sizes.append(span['size'])
                            font_styles.append(span['font'])
                except KeyError :
                    continue
        font_para_size = max(set(font_sizes), key=font_sizes.count)
        font_para_style = max(set(font_styles), key=font_styles.count)

        return font_para_size, font_para_style


    def extract_structure(self):
        prev_type = "subheading"
        current_text = ""
        structured_data = []

        font_para_size, font_para_style = self.get_para_font_details()

        for page in self.doc:
            data = json.loads(page.get_text("json"))
            for block in data['blocks']:
                try:
                    for line in block['lines']:
                        
                        current_type = "para"
                        line_text = ""
                        for span in line['spans']:
                            line_text = "".join([line_text, span['text'].strip()])
                            if span['size'] > font_para_size:
                                current_type = "subheading"
                        if current_type == prev_type:
                            current_text = " ".join([current_text, line_text])
                        else:
                            structured_data.append({
                                "type" : prev_type,
                                "text" : current_text
                            })
                            prev_type = current_type
                            current_text = line_text 
                except KeyError :
                    continue
        self.structured_data = structured_data
        return structured_data
                


        