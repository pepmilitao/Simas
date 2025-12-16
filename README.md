# SIMAS - Simulador de Algoritmos de substituição de páginas

## Índice

- [Descrição](#descrição)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Estrutura do repositório](#estrutura-do-repositório)
    - [Organização dos Componentes](#organização-dos-componentes)
- [Métodos Implementados](#métodos-implementados)
- [Comandos Disponíveis](#comandos-disponíveis)
- [Saída Esperada](#-saída-esperada)


## Descrição

---

## Tecnologias Utilizadas

- Linguagem: **Python**
- Paradigma: **Programação Orientada à Objetos**
- Interface: **CLI** (Command Line Interface)

---

## Estrutura do repositório

```text

```

### Organização dos Componentes


## Métodos Implementados


### Inicialização
- [x] `init(int tamanho)`
    - [x] Inicializa a memória física simulada
    - [x] Cria o primeiro bloco livre
    - [x] Impede operações antes da inicialização


### Alocação de Memória
- [ ] `alloc(int tamanho, FitAlg algoritmo)`
    - [ ] Localiza um bloco livre adequado
    - [ ] Aplica o algoritmo selecionado (First, Best ou Worst Fit)
    - [ ] Divide o bloco quando necessário
    - [ ] Atribui um identificador único ao bloco alocado


- [x] `choose_block(int tamanho, FitAlg algoritmo)`
    - [x] Implementa a lógica do First Fit
    - [x] Implementa a lógica do Best Fit
    - [x] Implementa a lógica do Worst Fit


### Liberação de Memória
- [ ] `free_id(int id)`
    - [ ] Localiza o bloco pelo identificador
    - [ ] Marca o bloco como livre
    - [ ] Realiza coalescência com blocos adjacentes


### Visualização
- [ ] `show()`
    - [ ] Exibe o mapa físico da memória (`#` e `.`)
    - [ ] Exibe os identificadores dos blocos
    - [ ] Mantém alinhamento proporcional ao tamanho da memória


### Estatísticas
- [ ] `stats()`
    - [ ] Calcula memória total
    - [ ] Calcula memória ocupada e livre
    - [ ] Identifica buracos (fragmentação externa)
    - [ ] Calcula fragmentação interna
    - [ ] Exibe taxa de uso efetivo da memória

---

## Comandos Disponíveis

| Comando | Descrição |
|-------|-----------|
| `init <tamanho>` | Inicializa a memória com o tamanho especificado |
| `alloc <tamanho> <algoritmo>` | Aloca memória usando First, Best ou Worst Fit |
| `freeid <id>` | Libera um bloco pelo identificador |
| `show` | Exibe o mapa atual da memória |
| `stats` | Exibe estatísticas de uso e fragmentação |



---

## Saída Esperada

Após a execução dos comandos:

```text
> init 64
> alloc 10 first
> alloc 8 first
> freeid 2
> alloc 6 best
> show
```

O simulador deve apresentar uma saída desse tipo:

```text
Mapa de Memória (64 bytes)
------------------------------------------------------------
[##########......######....................................]
[1111111111......333333....................................]
------------------------------------------------------------

Blocos ativos:
[id=1] @0 +10B (usado=10B) | [id=3] @10 +6B (usado=6B)

== Estatísticas ==
Tamanho total: 64 bytes
Ocupado: 16 bytes | Livre: 48 bytes
Buracos (fragmentação externa): 2
Fragmentação interna: 0 bytes
Uso efetivo: 25.00%
```
