from modulo import carregar_imagem_codificada

def testar_leitura_p1c():
    largura, altura, codificacao = carregar_imagem_codificada("testes/teste1_p1c.txt")
    assert largura == 8
    assert altura == 6
    codificacao_esperada = ['4', '01', '4', '00', '16', '11']



    assert codificacao == codificacao_esperada
    print(codificacao)

testar_leitura_p1c()