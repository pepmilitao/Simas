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
Este projeto consiste no desenvolvimento de um simulador de gerência de memória por paginação, reproduzindo o funcionamento de algoritmos clássicos de substituição de páginas utilizados em sistemas operacionais modernos. O simulador executa leituras de um arquivo de traço de referências e analisa o desempenho de diversas estratégias de remoção de páginas, facilitando estudo e comparação do impacto de cada algoritmo sobre as faltas de página e a eficiência da memória virtual.

Os algoritmos suportados são:

- FIFO (First-In, First-Out)
- LRU (Least Recently Used)
- Ótimo
- Segunda Chance
- Clock
- NRU (Not Recently Used)
- LFU (Least Frequently Used)
- MFU (Most Frequently Used)

---

## Tecnologias Utilizadas

- Linguagem: **Python**
- Paradigma: **Programação Orientada à Objetos**
- Interface: **CLI** (Command Line Interface)

---

## Estrutura do repositório

```text
.
├── ./classes
│   ├── ./classes/alg_impl
│   │   ├── ./classes/alg_impl/FIFO.py
│   │   ├── ./classes/alg_impl/LFU.py
│   │   ├── ./classes/alg_impl/LRU.py
│   │   ├── ./classes/alg_impl/MFU.py
│   │   ├── ./classes/alg_impl/NRU.py
│   │   ├── ./classes/alg_impl/Otimo.py
│   │   └── ./classes/alg_impl/SegundaChance.py
│   └── ./classes/Algoritmo.py
├── ./main.py
├── ./README.md
└── ./traces
    ├── ./traces/belady.trace
    └── ./traces/silberschatz2001.trace

```

## Métodos Implementados

- [x] Leitura do arquivo de referências (.trace)
    - [x] Carrega a sequência de referências de páginas do arquivo especificado.
- [x] Inicialização da estrutura de frames
    - [x] Define e zera os frames disponíveis na memória física.
- [x] Execução dos algoritmos de substituição de páginas
    - [x] FIFO (First-In, First-Out)
    - [x] LRU (Least Recently Used)
    - [x] Ótimo
    - [x] Segunda Chance
    - [x] Clock
    - [x] NRU (Not Recently Used)
    - [x] LFU (Least Frequently Used)
    - [x] MFU (Most Frequently Used)
- [x] Processamento do ciclo de referências
    - [x] Para cada referência, verifica se há falta de página.
    - [x] Aplica a política do algoritmo selecionado para inserir/evictar páginas.
- [x] Controle e atualização das páginas nos frames
    - [x] Gerencia contadores, bits de referência, uso recente, etc.
- [x] Cálculo das métricas de desempenho
    - [x] Número total de faltas de página
    - [x] Taxa de faltas (%)
    - [x] Quantidade de evicções
    - [x] Identificação do conjunto residente final
- [x] Geração da saída dos resultados
    - [x] Exibe, ao final, as métricas e o conteúdo dos frames
    - [x] (Opcional) Exibe passo a passo se modo verbose estiver ativado
---

## Comandos Disponíveis

| Comando | Descrição |
|-------|-----------|
| `--algo <algoritmo>` | Define o algoritmo de substituição a ser usado (ex: lru, fifo, otimo, etc).|
| `--frames <N>` | Define o número de frames físicos na memória. |
| `--trace <arquivo>` | Define o arquivo de referência de página. |
| `--verbose` | (Opcional) Mostra detalhes/explanação das decisões em cada passo. |

---

## Saída Esperada

Após a execução dos comandos:

```text
> ./pager --algo lru --frames 3 --trace traces/silberschatz2001.trace
```

O simulador deve apresentar uma saída desse tipo:

```text
Algoritmo: LRU
Frames: 3
Referências: 20
Faltas de página: 12
Taxa de faltas: 60.00%
Evicções: 12
Conjunto residente final:
frame_ids:
 0 1 2
page_ids:
 1 7 0
```
