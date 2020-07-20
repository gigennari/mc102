# O PROGRAMA AGENDA.PY

O programa agenda.py é um programa que permite que o usuário crie uma agenda e realize algumas operaçãoes sobre ela. O usuário deve digitar na linha de comando o nome da agenda, a operação a ser realizada (inicializar, criar, alterar, remover e listar) e o argumentos necessários para a operção. 

O programa usa o argparse para receber cada um dos elementos:

```console
Posicional:
acao                  ação sobre a agenda.

Opcional:
-a AGENDA, --agenda AGENDA (nome de sua agenda)                   
--evento EVENTO       identificador do evento.
--nome NOME           nome do evento.
--descricao DESCRICAO descrição do evento.                  
--data DATA           data do evento xx/xx/xxxx.
--hora HORA           hora do evento xx:xx.
```

Após realizar a operação desejada, ele escreve o arquivo da agenda, no formato csv. 

## PASSANDO AS OPERAÇÕES

### Inicializar
```console
user@notebook$ python3 agenda.py -a agenda.csv inicializar
Uma agenda vazia `agenda.csv` foi criada!
```

### Criar
```console
user@notebook$ python3 agenda.py -a agenda.csv criar --nome "Karate" --descricao "aula online de karate" --data "19/07/2020" --hora "19:00"

Foi adicionado evento 3
```
### Alterar
```console
user@notebook$ python3 agenda.py -a agenda.csv alterar --evento 1 --hora "19:30"
```

### Remover
```console
user@notebook$ python3 agenda.py -a agenda.csv remover --evento 1"

O evento foi removido
```

### Listar
Caso haja evento em um dia:

```console
user@notebook$ python3 agenda.py -a agenda.csv listar --data "19/07/2020"

Eventos do dia 10/06/2020
-----------------------------------------------
Evento 1 - MC102
Descrição: Aula de laboratório
Data: 10/06/2020
Hora: 16:50
-----------------------------------------------
```

Caso não haja:
```console
user@notebook$ python3 agenda.py -a agenda.csv listar --data "10/06/2020"

Não existem eventos para o dia 10/06/2020!
```


## ESTRUTURA DE DADOS DA AGENDA

A estrutura de dados utilizada para manipular a agenda foram dicionários. Cada agenda é um dicionário, com chaves que correpondem ao número dos eventos e com valores no formato de dicionários também, contendo as chaves nome, descricção, data e hora. Usar dicts para a agenda é o jeito mais simples de poder acessar o número de um evento, pois basta usar a função .keys() para obter todas as chaves (importante para obter nuúmeros já existentes e não sobrescrever um evento, além de facilitar iterações para percorrer a agenda). Além disso, é mais simples usar dict para buscar um parâmetro específico do evento, como a data na função que lista todos os eventos de um dia, do que ter que memorizar em qual posição de uma lista, por exemplo, estaria a data.

Um exemplo de agenda seria:
```python 
agenda = {1: {"nome": "Karate" , "descricao": "aula online de karate", "data": "19/07/2020", "hora": "19:00"}, 2: {"nome": "P2 MA141" , "descricao": "prova de geometria analítica", "data": "13/08/2020", "hora": "08:00"}}
```

## FORMATO DO ARQUIVO EM CSV

O arquivo CSV gera uma tabela em que cada linha corresponde a um evento, tal que:
A primeira coluna contém o nome do evento;
A segunda, a descrição;
A terceira, a data;
E a quarta, a hora. 





