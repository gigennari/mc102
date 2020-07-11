from modulo import carregar_imagem_decodificada

def testar_leitura_pbm():
    largura, altura, imagem = carregar_imagem_decodificada("testes/teste1.txt")
    assert largura == 8
    assert altura == 6
    matriz_esperada = [
        ['0', '0', '0', '0', '0', '0','0', '0'],
        ['1', '1', '1', '1', '0', '0', '0', '0'],
        ['1', '1', '1', '1','1', '1', '1', '1'],
        ['1', '1', '1', '1','1', '1', '1', '1'],
        ['1', '1', '1', '1','1', '1', '1', '1'],
        ['1', '1', '1', '1','1', '1', '1', '1'],
    ]
    assert imagem == matriz_esperada
    print(imagem)

testar_leitura_pbm()