import sys
import re

def somador():
    soma = 0
    on = False
    for linha in sys.stdin:
        captura = re.findall(r'(on|off|=|\d+)',linha,re.IGNORECASE) #re.IGNORECASE permite identificar as ocorrencias sendo estas maiusculas ou minusculas
        for i in captura:
            if i.lower() == "on":
                on = True
            elif i.lower() == "off":
                on = False
            elif i.isdigit() and on:
                soma += int(i)
            elif i == "=":
                print("Soma atual =",soma)


def main():
    somador()


if __name__ == "__main__":
    main()