from aksara_tokenizer import BaseTokenizer
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
    print(aksara_pud[0:5])


if __name__ == "__main__":
    # main()
    read()
