# cyclotron

Usando o Python, pip, venv e pytest.

## Para poder usar a aplicação

Com o git use: git clone https://github.com/ladcs/cyclotron

Entre na pasta: cd cyclotron

Use: python -m venv .venv && .\Scripts\active

Instale as dependencias com: python -m pip dev-req.txt

## Com as dependencias instaladas

O pytest, python -m pytest, irá retornar todos os testes automatizados feitos, que são eles:

### test_change_lines_columns

Testa se muda a primeira linha para todos os valores em 'e' caso a entrada for 'e'.

Testa se muda a última linha para todos os valores em 'p' menos o último e testa se muda todos os valores para 'p' caso a entrada for 'p'.

Testa se muda a última coluna para 'e' caso a entrada for 'e'.

Testa se todos os valores da primera coluna muda para 'p' e todos os valores da última coluna muda para 'p' menos o último valor caso a entrada seja 'p'.

### Teste create cyclotron

Testa se com uma dimensão da matriz menor que 4 retorna uma mensagem de erro.

Testa se ao invés de enviar uma particula é enviado um número ou uma string qualquer, se retorna uma mensagem de erro.

Testa se ao não enviar nada para particula se retorna o cyclotron original.

Testa se enviar uma particula se segue a ideia para cada um:

Para a particula p:

retorno:

[p, p, p, p]
[p, 1, 1, p]
[p, 1, p, p]
[p, p, p, 1]

para a particula e:
 
retorno:

[e, e, e, e]
[1, 1, 1, e]
[1, 1, 1, e]
[1, 1, 1, e]

para a partícula n:

retorno:

[n, n, n, n]
[1, 1, 1, 1]
[1, 1, 1, 1]
[1, 1, 1, 1]


### Test generate matrix

Testa se ao enviar um valor para linhas (n), outro para colunas (m) e outro para valor (k), retorna uma matriz de nxm com todos os valores sendo k.

### Test square matrix

Testa se ao enviar um valor para as dimensões da matriz quadrade menores que 4 retorna uma mensagem de erro.

Testa se ao enviar dimensões de 4 e de 8 se retorna matriz quadrada com todos os valores em 1 com as dimensõees de 4 e 8 respectivamente.
