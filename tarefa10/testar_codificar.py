from modulo import codificar

def testar_codificar():
    # crie um exemplo de imagem pequena para testar
    largura = 8
    altura = 6
    imagem = [
        ['0','0', '0', '0', '0', '0', '0', '0'],
        ['1','1', '1', '1', '0', '0', '0', '0'],
        ['1','1','1','1','1','1','1','1'],
        ['1','1','1','1','1','1','1','1'],
        ['1','1','1','1','1','1','1','1'],
        ['1','1','1','1','1','1','1','1'],
        
    ]

    codificacao_esperada = [4, '01', 4, '00', 16, '11']

    codificacao_calculada = codificar(largura, altura, imagem)
 


    assert codificacao_calculada == codificacao_esperada


testar_codificar()