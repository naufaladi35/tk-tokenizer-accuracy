import subprocess
from aksara_tokenizer import BaseTokenizer
from conllu import parse
import re


def aksara_tokenize(input_list):
    res = []
    for input in input_list:
        tokenizer = BaseTokenizer()
        res.append(tokenizer.tokenize(input.metadata["text"])[0])
    return res


def bahasa_tokenize(input_list):
    res = []
    for input in input_list:
        with open('input.txt', 'w', encoding='utf-8', errors='ignore') as file:
            file.write(input.metadata["text"])
        subprocess.run("perl .\\bahasa_tokenizer.pl")
        with open('res-token.txt', encoding='utf-8', errors='ignore') as file:
            res_token = file.read().split("\n")
            res.append(res_token)
    return res


def read_conllu(filename):
    with open(filename,  encoding='utf-8', errors='ignore') as data:
        annotations = data.read()
    sentences = parse(annotations)
    return sentences


def accuracy(token, gold_standard):
    T = 0
    N = len(gold_standard)
    j_init = 0
    for i in range(len(token)):
        for j in range(j_init, N):
            # print(j, gold_standard[j], i, token[i])
            if str(gold_standard[j]) == token[i]:
                j_init = i + 1
                T += 1
                break

    return(T, N)


def total_accuracy(tokens, gold_standards):
    total_T = 0
    total_N = 0
    for i in range(len(tokens)):
        T, N = accuracy(tokens[i], gold_standards[i])
        total_T += T
        total_N += N
    print(total_T, "/", total_N)


def read_text(filename):
    res = []
    with open(filename, encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
    for line in lines:
        if re.search("^# text =*", line):
            x = line[9:].strip()
            res.append(x)
    return res


def main():
    input_pud = read_conllu('id_pud-ud-test.conllu')
    input_gsd = read_conllu('id_gsd-ud-test.conllu')
    input_csui = read_conllu('id_csui-ud-test.conllu')

    aksara_pud = aksara_tokenize(input_pud)
    aksara_gsd = aksara_tokenize(input_gsd)
    aksara_csui = aksara_tokenize(input_csui)
    print("=======Aksara=========")
    print("PUD")
    total_accuracy(aksara_pud, input_pud)
    print("GSD")
    total_accuracy(aksara_gsd, input_gsd)
    print("CSUI")
    total_accuracy(aksara_csui, input_csui)
    print("=======Bahasa=========")

    bahasa_tokenize(input_pud)


if __name__ == "__main__":
    main()
