import string

def is_valid_sentence(sentence):
    # Check if the sentence ends with a punctuation mark
    if sentence.strip()[-1] in string.punctuation:
        return True
    elif sentence.strip()[-1].isnumeric():
        return True
    else:
        return False
    

def read_file(file_path):
    contents = ''
    with open(file_path, 'r') as f:
        contents = f.read()
    return contents
