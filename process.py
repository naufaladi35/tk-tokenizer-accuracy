from aksara_tokenizer import BaseTokenizer


def main():
    text = "“Meski kebanyakan transisi digital yang terjadi di Amerika Serikat belum pernah terjadi sebelumnya, transisi kekuasaan yang damai tidaklah begitu,” tulis asisten khusus Obama, Kori Schulman di sebuah postingan blog pada hari Senin."
    tokenizer = BaseTokenizer()
    res = tokenizer.tokenize(text)
    print(res)


if __name__ == "__main__":
    main()
