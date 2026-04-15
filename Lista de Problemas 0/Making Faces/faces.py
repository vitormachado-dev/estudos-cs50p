def main():
    text = input()
    convert(text)

def convert(texto):
    texto = texto.replace(':)','🙂')
    texto = texto.replace(':(','🙁')
    print(texto)

main()