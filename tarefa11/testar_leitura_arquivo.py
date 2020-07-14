from frequencia.py import ler_arquivo_texto

def testar_leitura_arquivo():
    nome_do_aqrquivo = 'testes/texto5.txt'
    palavras_esperadas = ['eu', 'fui', 'à', 'feira', 'comi', 'pastel', 'na', 'feira', 'e', 'mamãe',
     'tomou','guaraná', 'com', 'pastel']

    palavras_calculadas = ler_arquivo_texto(nome_do_aqrquivo)

    assert palavras_calculadas == palavras_esperadas
    

testar_leitura_arquivo()