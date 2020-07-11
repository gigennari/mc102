from modulo import decodificar

def testar_decodificar():
    # crie um exemplo de imagem pequena para testar
    largura = 8
    altura = 6
    codificacao = ['4', '01', '4', '00', '16', '11']
    imagem = [
        ['0','0', '0', '0', '0', '0', '0', '0'],
        ['1','1', '1', '1', '0', '0', '0', '0'],
        ['1','1','1','1','1','1','1','1'],
        ['1','1','1','1','1','1','1','1'],
        ['1','1','1','1','1','1','1','1'],
        ['1','1','1','1','1','1','1','1'],
      ]

    decodificacao_calculada = decodificar(largura, altura, codificacao)
 
    assert decodificacao_calculada == imagem

testar_decodificar()