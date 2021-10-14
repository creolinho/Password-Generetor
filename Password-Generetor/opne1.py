import unicodedata

'''codigo para formatar palavras e tirar pontuação
 e caracteres não utilizados em uma senha'''

for i in range(8,14):
    with open(f"{i}letras.txt",'r', encoding ='utf-8') as f:
        for line in f.readlines():
            word = unicodedata.normalize("NFD", line)
            word = word.encode("ascii", "ignore")
            word.decode("utf-8")
            word = str(word)[2:]
            word = str(word)[:-3]
            print(word)
            with open(f'{i}code.txt','a') as w:
                    w.write(str(word))
                    w.write('\n')
                   