import re
import sys

header = re.compile(r'^(#+) +(.*)$') # Apanha headers do tipo #, ##, ###, etc.
bold = re.compile(r'\*\*(.*?)\*\*|__(.*?)__') # Apanha texto a bold
italic = re.compile(r'\*(.*?)\*|_(.*?)_') # Apanha texto em itálico
link = re.compile(r'\[(.*)\]\((.*)\)') # Apanha links
image = re.compile(r'!\[(.*)\]\((.*)\)') # Apanha imagens
numbered_list = re.compile(r'^\d+\. +(.*)$') # Apanha listas numeradas


# necessito de ler o ficheiro test.md e ler linha a linha


def md_to_html(md_file, output_file):
    html_lines = []  # Lista para armazenar as linhas convertidas
    in_list = False  # Flag para controlar listas

    with open(md_file, 'r') as file:
        for line in file:
            line = line.strip()  # Remove espaços extras no início e fim



            # Processamento de listas numeradas
            if numbered_list.match(line):
                if not in_list:
                    html_lines.append('<ol>')
                    in_list = True
                html_lines.append(numbered_list.sub(r'<li>\1</li>', line))
                continue  # Evita que listas passem por outras substituições

            else:
                if in_list and line != '':
                    html_lines.append('</ol>')  # Fecha a lista quando encontramos uma linha normal
                    in_list = False
                
                # Cabeçalhos
                if header.match(line):
                    i = len(header.match(line).group(1))
                    line = f'<h{i}>{header.match(line).group(2)}</h{i}>'
                # Aplicação das restantes transformações de Markdown
                line = bold.sub(r'<b>\1\2</b>', line)
                line = italic.sub(r'<i>\1\2</i>', line)
                line = link.sub(r'<a href="\2">\1</a>', line)
                line = image.sub(r'<img src="\2" alt="\1">', line)

                html_lines.append(line)

        if in_list:
            html_lines.append('</ol>')  # Fecha a lista no final do ficheiro, se necessário

    with open(output_file, 'w') as f:
        f.write("\n".join(html_lines))

    print(f"Conversão concluída! O HTML foi salvo em '{output_file}'.")

md_to_html('test.md', 'test.html')
