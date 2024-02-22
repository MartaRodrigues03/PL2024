import sys
import re


def md_to_html(linha):
    global na_lista
    #cabecalhos
    match = re.match(r'^(#+)\s+(.*)$', linha)
    if match:
        conta = len(match.group(1))
        linha = f'<h{conta}>{match.group(2)}</h{conta}>'

    #bold
    linha = re.sub(r'\*\*(.*?)\*\*',r'<b>\1</b>',linha)

    #italico
    linha = re.sub(r'\*(.*?)\*',r'<i>\1</i>',linha)

    #lista numerada
    linha = re.sub(r'^(\d+\.)\s*(.*)$', r'<li>\2</li>', linha, flags=re.MULTILINE)

    #link
    linha = re.sub(r'\[(.*?)\]\((.*?)\)',r'<a href="\2">\1</a>',linha)

    #imagem
    linha = re.sub(r'\!\[(.*?)\]\((.*?)\)',r'<img src="\2" alt="\1"/>',linha)

    return linha



def main():
    input = sys.argv[1]

    html = f"""<html>
<body>
    """
    na_lista = False
    with open(input,'r') as ficheiro:
        for linha in ficheiro:

            if linha[0].isdigit() and linha[1] == '.':
                if not na_lista:
                    html += '<ol>\n'
                    na_lista = True
                html += md_to_html(linha.strip()) + '\n'
            else:
                if na_lista:
                    html += '</ol>\n'
                    na_lista = False
                html += md_to_html(linha.strip()) + '\n'

        if na_lista:
            html += '</ol>\n'

    html += """
</body>
</html>
    """

    with open("resultado.html",'w') as res:
        res.write(html)
    res.close()




if __name__ == "__main__":
    main()