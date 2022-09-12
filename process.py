from aksara_tokenizer import BaseTokenizer
from conllu import parse
import re


def aksara_tokenize(token_lists):
    res = []
    for token_list in token_lists:
        tokenizer = BaseTokenizer()
        res.append(tokenizer.tokenize(token_list.metadata["text"])[0])
    return res


def main():
    input_pud = read_conllu('id_pud-ud-test.conllu')
    input_gsd = read_conllu('id_gsd-ud-test.conllu')
    input_csui = read_conllu('id_csui-ud-test.conllu')

    aksara_pud = aksara_tokenize(input_pud)
    aksara_gsd = aksara_tokenize(input_gsd)
    aksara_csui = aksara_tokenize(input_csui)

    # for i in range(len(input_csui)):
    #     if accuracy(aksara_csui[i], input_csui[i]) == True:
    #         print(i , " benar")
    #     elif accuracy(aksara_csui[i], input_csui[i]) == False:
    #         print(i , " salah")

    accuracy(aksara_csui[10], input_csui[10])

def read_conllu(filename):
    with open(filename,  encoding='utf-8', errors='ignore') as data:
        annotations = data.read()
    sentences = parse(annotations)
    return sentences


def accuracy(token, gold_standard):
    T = 0
    N = len(gold_standard)
    i = 0
    j = 0
    print(gold_standard)
    print(token)
    while j < len(token):
        if(i >= len(gold_standard)):
            i = j
            j += 1
        print(gold_standard[i], token[j])
        if str(gold_standard[i]) == token[j]:
            T += 1
            j += 1
        i += 1
    print(T)
    if N != T:
        return False
    else:
        return True


def read_text(filename):
    res = []
    with open(filename, encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
    for line in lines:
        if re.search("^# text =*", line):
            x = line[9:].strip()
            res.append(x)
    return res


if __name__ == "__main__":
    main()
