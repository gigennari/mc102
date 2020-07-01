bit 0 - cor branca
bit 1- cor preta 

FORMATO PBM
1ª linha - tipo de arquivo (P1)
2ª linha - dimensões da imagem: largura x altura
linhas seguintes - 0 para pixels brancos e 1 para pixels pretos
-essa é um representação conveniente, mas usaria muito espaço para 
imagem com milhões de pixels (megapixels)

Para reduzir a qtde de memória necessária, 
CODIFICAÇÃO RUN-LENGTH
-tamanho da sequencia seguido pelo valor do bit (0/1)
ZZUUUZZUUUUUU
2Z3U2Z6U


NA TAREFA
duas linhas 
4 padrões: 00, 01, 10, 11
1º bit = 1ª linha 
2º bit = 2ª linha 

EXEMPLO
P1C

8 6 --> dimensões; largura x altura (smp numero par)
4 01 4 00 16 11

Teremos nas 2 primeiras linhas:
00000000 
11110000

"4 vezes o 01 em pé e 4 vezes o 00 em pé"

Da 3ª a 6ª linha (16 11)
11111111
11111111
11111111
11111111


modulo --> decodificar a imagem

bordas --> detectar bordas da imagem 
            a borda de um objeto é formada pelos pixels que têm ao
            menos um vizinho que não está no objeto 

            