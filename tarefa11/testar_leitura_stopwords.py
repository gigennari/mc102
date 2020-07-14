from frequencia.py import ler_entrada

def testar_leitura_entrada():
    
    caminho_arquivo_esperado = ['testes/texto5.txt']
    stopwords_esperado = ['eu', 'na', 'e']
    
    caminho_arquivo, stopwords = ler_entrada()

    assert caminho_arquivo_esperado == caminho_arquivo

    assert stopwords_esperado == stopwords 
    

testar_leitura_arquivo()