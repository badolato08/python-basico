# Python Básico — Sequência de Estudos (comparada ao JS)

Sequência de conceitos básicos de Python — sintaxe, condicionais, operadores,
laços, estruturas de dados, funções — pensada para servir de base **antes**
do projeto Sabor Express (POO). Cada arquivo comenta as diferenças em
relação ao JavaScript, já que é a linguagem de referência mais próxima do projeto Locadora (Node/Express).

## Como usar

Cada arquivo é independente. Basta rodar `python nome_do_arquivo.py` no
terminal.

## Sequência de conteúdos

| # | Arquivo | Conceito principal |
|---|---------|---------------------|
| 1 | `1_variaveis.py` | Variáveis, tipos, f-strings |
| 2 | `2_decisao.py` | `if` / `elif` / `else` |
| 3 | `3_operadores.py` | Operadores lógicos (`and`, `or`, `not`) e de comparação |
| 4 | `4_lacos.py` | `for`, `while` e a ausência do `do-while` em Python |
| 5 | `5_listas.py` | Listas (equivalente a arrays), matrizes, list comprehension |
| 6 | `6_tuplas.py` | Tuplas — dados imutáveis, empacotamento/desempacotamento |
| 7 | `7_dicionarios.py` | Dicionários — equivalente ao objeto do JS |
| 8 | `8_funcoes.py` | Funções, type hints, valor padrão, `lambda` |

### Pasta `lista/` — exercícios aplicados

| # | Arquivo | Conceito praticado |
|---|---------|---------------------|
| 1 | `1_preco.py` | Condicional + formatação numérica |
| 2 | `2_aprovacao.py` | Operadores lógicos |
| 3 | `3_tabuada.py` | Laço `for` |
| 4 | `4_notas.py` | Lista + laço + `sum()`/`max()`/`min()` |
| 5 | `5_imc.py` | Função com retorno + condicional encadeado |
| 6 | `6_coordenadas.py` | Tupla + desempacotamento |
| 7 | `7_catalogo_produtos.py` | Lista de dicionários (aquecimento direto para o Sabor Express) |

## Principais diferenças em relação ao JS

- **Sem declaração obrigatória:** JS exige `let`/`const`/`var`. Python cria
  a variável só ao atribuir (`a = 5`).
- **Sem `{ }` nem `( )` nos blocos/condições:** Python usa apenas `:` e
  indentação.
- **`else if` → `elif`** (uma palavra só), operadores lógicos por extenso
  (`and`/`or`/`not` em vez de `&&`/`||`/`!`).
- **Sem `==` vs `===`:** Python só tem um jeito de comparar (`==`), e ele já
  se comporta como o `===` do JS — nunca converte tipos silenciosamente.
- **`do-while` não existe em Python** — o `4_lacos.py` mostra como simular
  com `while True` + `if...break`.
- **Tuplas são de verdade imutáveis:** diferente do `Object.freeze()` do JS
  (que só ignora silenciosamente a alteração), tentar mudar uma tupla em
  Python sempre gera `TypeError`.
- **Dicionário troca `.` por `[]` obrigatório:** `objeto.chave` (JS) vira
  `dicionario["chave"]` (Python). Acessar uma chave que não existe também
  muda de comportamento: JS retorna `undefined` sem erro, Python gera
  `KeyError` — por isso usamos `.get()` com valor padrão.
- **Sem arrow function:** o mais próximo é o `lambda`, mas só serve para
  expressões de uma linha (arrow function do JS aceita várias linhas com
  `{ }`).
- **Sem type hints nativos no JS puro:** Python já vem com anotações de tipo
  (`def somar(a: int, b: int) -> int`) — em JS isso só existe via
  TypeScript.
- **`number_format`/`toLocaleString` não existem em Python** —
  `lista/1_preco.py` mostra o jeito manual de formatar número no padrão
  brasileiro.

## Conexão com o projeto Sabor Express

O arquivo `7_dicionarios.py` e o exercício `lista/7_catalogo_produtos.py`
usam exatamente o mesmo formato de dados da primeira versão do Sabor
Express (lista de dicionários com `nome`, `categoria`/`preço`, estado) — o
mesmo formato que um array de objetos assume em JS ao receber o resultado
de uma query. A ideia é que, ao chegar no projeto, a estrutura
`restaurantes = [...]` já pareça familiar antes de ela virar uma lista de
objetos na versão POO.
