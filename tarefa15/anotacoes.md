# Tarefa 15: URL, Hierarquia e Árvores

## Árvore

Uma página html pode conter links para outras páginas. Conforme vamos acessando esses links, forma-se uma hierarquia. Assim, queremos fazer um programa que receba o link de uma página inicial e mostre a hierarquia entre as páginas que podem ser alcançadas a partir da inicial. 

Esssa hierarquia forma uma árvore, em que cada nó corresponde a uma página distinta. 

### Exemplo

```
https://exemplo.com/index.html
    https://exemplo.com/blog/index.html
        https://exemplo.com/blog/primeiro-post.html
            https://exemplo.com/segundo-post.html
        https://exemplo.com/minha-viagem.html
    https://exemplo.com/portifolio.html
```

Visitamos os links na ordem que encontramos nas páginas. Repare que uma página pode ser acessada através de várias outras páginas, mas ela aparecerá na árvore apenas uma vez.
O link de acesso ao segundo post, foi acessado dentro da página do primeiro post. Assim, ele não deverá ser acessado de novo a partir da página dos index.

## Analisando uma página

O que é uma página html? Um arquivo de texto escrito em uma linguagem de marcação de estrutura e formato.

Esse arquivo é formado por uma sequência de tags balanceadas. Como no exemplo:
```
<a href="https://ic.unicamp.br/graduacao/engenharia-da-computacao/">
  Engenharia da Computação
</a>
```
A tag define o link com o texto ``` Engenharia de Computação```. Ou seja, ao clicar na tag, somos redirecionados para esse link. 

### A propriedade href

Ela indica o destino do link. 
Para esta tarefa, vamos supor que todo link corresponde a uma substring com a forma ``` href = "[URL DA PÁGINA]```. Assim, vamos procurar por substrings com esse formato e extrair URL entre as aspas duplas.

### Como utilizar o módulo re para expressões regulares

```python 
>>>import re
>>>regex = r"\(\d{2}\) \d{4,5}-\d{4}"
>>> texto = "Esse é o meu número (00) 12345-6789"
>>> texto = "Ligue para (00) 2345-6789 ou para (01) 12345-4321"
>>> telefones = re.findall(regex, texto)
>>> telefones
['(00) 2345-6789', '(19) 12345-4321']
```

Do mesmo modo que aplicamos isso a um telefone, podemos fazer para uma URL. 

Mais exemplos em [Python RegEx](https://www.w3schools.com/python/python_regex.asp)

## Módulo auxiliar 

### Resolvendo URLs

### Controlando o tamanho da árvore

### Baixando arquivos html

## Entrada e saída 

### Entrada
Linha com a URL da página inicial 
```
https://ic.unicamp.br/~lehilton/mc102qr/index.html 
```

### Saída 
Árovore. Cada subnível da hierarquia dever ter um nível de recuo de 2 espaços. 
```
https://ic.unicamp.br/~lehilton/mc102qr/index.html
  https://ic.unicamp.br/~lehilton/mc102qr/apresentacao.html
  https://ic.unicamp.br/~lehilton/mc102qr/fixacao.html
    https://ic.unicamp.br/~lehilton/mc102qr/fixacao/00-algoritmo.html
      https://ic.unicamp.br/~lehilton/mc102qr/fixacao/01-variaveis.html
        https://ic.unicamp.br/~lehilton/mc102qr/fixacao/02-condicional.html
          https://ic.unicamp.br/~lehilton/mc102qr/fixacao/03-repeticao.html
            https://ic.unicamp.br/~lehilton/mc102qr/fixacao/04-funcoes.html
              https://ic.unicamp.br/~lehilton/mc102qr/fixacao/05-praticas.html
                https://ic.unicamp.br/~lehilton/mc102qr/fixacao/06-listas.html
                  https://ic.unicamp.br/~lehilton/mc102qr/fixacao/07-ordenacao.html
                    https://ic.unicamp.br/~lehilton/mc102qr/fixacao/08-matrizes.html
                      https://ic.unicamp.br/~lehilton/mc102qr/fixacao/09-arquivos.html
                        https://ic.unicamp.br/~lehilton/mc102qr/fixacao/10-colecoes.html
                          https://ic.unicamp.br/~lehilton/mc102qr/fixacao/11-eficiencia.html
                            https://ic.unicamp.br/~lehilton/mc102qr/fixacao/12-recursao.html
  https://ic.unicamp.br/~lehilton/mc102qr/unidades/01-problemas-algoritmos.html
    https://ic.unicamp.br/~lehilton/mc102qr/unidades/02-escrevendo-algoritmos.html
      https://ic.unicamp.br/~lehilton/mc102qr/unidades/03-linguagens-programacao.html
        https://ic.unicamp.br/~lehilton/mc102qr/unidades/04-estruturas-elementares.html
          https://ic.unicamp.br/~lehilton/mc102qr/unidades/05-listas.html
            https://ic.unicamp.br/~lehilton/mc102qr/unidades/06-funcoes.html
              https://ic.unicamp.br/~lehilton/mc102qr/unidades/07-algortimos-iterativos.html
                https://ic.unicamp.br/~lehilton/mc102qr/unidades/08-matrizes.html
                  https://ic.unicamp.br/~lehilton/mc102qr/unidades/09-colecoes.html
                    https://ic.unicamp.br/~lehilton/mc102qr/unidades/10-eficiencia.html
                      https://ic.unicamp.br/~lehilton/mc102qr/unidades/11-recursao.html
                        https://ic.unicamp.br/~lehilton/mc102qr/tarefas/14-recursao.html
                          https://ic.unicamp.br/~lehilton/mc102qr/tarefas/13-algoritmos-eficientes.html
                            https://ic.unicamp.br/~lehilton/mc102qr/tarefas/12-colecoes-dinamicas.html
                              https://ic.unicamp.br/~lehilton/mc102qr/tarefas/11-dicionarios-e-tuplas.html
                                https://ic.unicamp.br/~lehilton/mc102qr/tarefas/10-imagens-binarias.html
                                  https://ic.unicamp.br/~lehilton/mc102qr/tarefas/09-conceito-frequencia.html
                                    https://ic.unicamp.br/~lehilton/mc102qr/tarefas/08-funcoes.html
                                      https://ic.unicamp.br/~lehilton/mc102qr/tarefas/07-percorrer-listas.html
                                        https://ic.unicamp.br/~lehilton/mc102qr/tarefas/06-listas.html
                                          https://ic.unicamp.br/~lehilton/mc102qr/tarefas/05-condicional.html
                                            https://ic.unicamp.br/~lehilton/mc102qr/tarefas/04-entendendo-algoritmos.html
                                              https://ic.unicamp.br/~lehilton/mc102qr/tarefas/03-estruturas-controle.html
                                                https://ic.unicamp.br/~lehilton/mc102qr/tarefas/02-problemas-algoritmos.html
                                                  https://ic.unicamp.br/~lehilton/mc102qr/tarefas/01-primeira-tarefa.html
```