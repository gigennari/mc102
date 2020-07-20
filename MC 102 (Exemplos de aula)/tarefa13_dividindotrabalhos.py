"""
PROBLEMA:

Alguns trabalhos serão passados para dois alunos e eles saberão o grau de dificuldade
de cada trabalho.

Eles resolvem dividir o trabalho seguindo esses critérios:
1) a ordem dos trabalhos não pode ser alterada
2) a divisão precisa ser justa, ou seja, AS SOMAS DOS GRAUS DE DIFICULDADE DOS TRABALHOS
A SEREM FEITOS PELOS DOIS DEVEM TER A MENOR DIFERENÇA
3) o amigo1 sempre faz os primeiros trabalhos e o amigo2, os restantes

ENTRADA: arquivo com vários casos teste --> 1ª linha - um inteiro N que é o numero de trabalhos a serem realizados; 2ª linha - inteiros representando
o grau de dificuldade de cada trabalho 

3
2 3 5
4 
1 2 2 6

SAÍDA: diferença descrita no item 2 dos critérios; add quebra de linha no fim de 
casa resposta (\n)
0
1


Dica: pense em uma forma de calcular a diferença sem percorrer toda a lista de trabalhos
mais de uma vez 


!!! se começarmos somando de fora para dentro, até esgotar o númeor de trabalhos,
e comparando em cada loop a diferença atual com a difença do loop anterior,
talvez dê certo 


"""