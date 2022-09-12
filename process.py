from aksara_tokenizer import BaseTokenizer
from conllu import parse
import re


def aksara_tokenize(input_text):
    res = []
    for line in input_text:
        tokenizer = BaseTokenizer()
        res.append(tokenizer.tokenize(line)[0])
    return res


def read():
    input_pud = []
    input_gsd = []
    input_csui = []
    with open('id_pud-ud-test.conllu', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
        anno = f.read()
        sentences = parse(anno)
    for line in lines:
        if re.search("^# text =*", line):
            x = line[9:].strip()
            input_pud.append(x)

    with open('id_gsd-ud-test.conllu', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
    for line in lines:
        if re.search("^# text =*", line):
            x = line[9:].strip()
            input_gsd.append(x)

    with open('id_csui-ud-test.conllu', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
    for line in lines:
        if re.search("^# text =*", line):
            x = line[9:].strip()
            input_csui.append(x)

    

    aksara_pud = aksara_tokenize(input_pud)
    aksara_gsd = aksara_tokenize(input_gsd)
    aksara_csui = aksara_tokenize(input_csui)
    print(aksara_csui[0:2])

def read_conllu():
    with open('id_csui-ud-test.conllu',  encoding='utf-8', errors='ignore') as data:
        annotations = data.read()
    sentences = parse(annotations)
    print(sentences[0])
    print(sentences[0][0])
    print(sentences[0].metadata['text'])

if __name__ == "__main__":
    # main()
    read()
    read_conllu()
