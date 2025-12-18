from classes.alg_impl.FIFO import FIFO
from classes.alg_impl.LFU import LFU
from classes.alg_impl.LRU import LRU
from classes.alg_impl.MFU import MFU
from classes.alg_impl.NRU import NRU
from classes.alg_impl.Otimo import Otimo
from classes.alg_impl.SegundaChance import SegundaChance
import argparse
import os

def ajuda():
    print("\nComandos disponíveis:")
    print("  help                  mostra esta mensagem")
    print("  exit                  encerra o simulador")
    print("  algo <alg>            seleciona o algoritmo (fifo, lru, opt, sc, nru, lfu, mfu)")
    print("  frames <n>            define o número de quadros (frames) na memória")
    print("  trace <arquivo>       carrega o arquivo de referências de páginas (.trace)")
    print("  run                   executa a simulação com as opções atuais")
    print("  stats                 exibe os resultados da última simulação\n")

print("Bem-vindo ao SIMAS - Simulador Interativo de Memória por Acesso a Swaps :)")
print("Digite 'help' para ver os comandos disponíveis.\n")

ALGORITMOS = {
    "fifo": FIFO,
    "lru": LRU,
    "opt": Otimo,
    "sc": SegundaChance,
    "nru": NRU,
    "lfu": LFU,
    "mfu": MFU
}

# Estado da sessão
algoritmo_nome = None
algoritmo_inst = None
num_frames = None
trace_path = None
trace_refs = None
ultimo_resultado = None

def imprimir_resultado(resultado):
    if not resultado:
        print("Nenhuma simulação realizada ainda.")
        return
    total_refs = resultado['total_referencias']
    faltas = resultado['faltas_pagina']
    taxa = (faltas / total_refs) * 100 if total_refs > 0 else 0.0
    print(f"\nAlgoritmo: {resultado['algoritmo']}")
    print(f"Frames: {resultado['total_quadros']}")
    print(f"Referências: {total_refs}")
    print(f"Faltas de página: {faltas}")
    print(f"Taxa de faltas: {taxa:.2f}%")
    print(f"Evicções: {resultado['eviccoes']}")
    print("Conjunto residente final:")
    frame_ids = ' '.join(str(i) for i in range(resultado["total_quadros"]))
    page_ids = ' '.join(str(p) for p in resultado["conjunto_residente"])
    print(f"frame_ids: {frame_ids}")
    print(f"page_ids:  {page_ids}\n")

def ler_trace(caminho):
    # Tenta abrir no caminho informado
    if os.path.isfile(caminho):
        pass
    else:
        # Tenta dentro do diretório 'traces'
        if os.path.isfile(os.path.join("traces", caminho)):
            caminho = os.path.join("traces", caminho)
        else:
            print(f"Arquivo '{caminho}' não encontrado.")
            return None
    try:
        with open(caminho, "r") as f:
            return [int(linha.strip()) for linha in f if linha.strip()]
    except Exception as e:
        print(f"Erro ao ler '{caminho}': {e}")
        return None

while True:
    entrada = input("[SIMAS]> ").strip().split()
    if not entrada:
        continue
    comando, *args = entrada

    match comando.lower():
        case "help" | "?":
            ajuda()
        case "exit" | "quit":
            print("Encerrando SIMAS.")
            break
        case "algo":
            if not args:
                print("Erro: use 'algo <algoritmo>', ex: algo fifo")
                continue
            if args[0] not in ALGORITMOS:
                print("Algoritmo inválido! Opções: fifo lru opt sc nru lfu mfu")
                continue
            algoritmo_nome = args[0]
            algoritmo_inst = ALGORITMOS[algoritmo_nome]()
            print(f"Algoritmo selecionado: {algoritmo_nome.upper()}")
        case "frames":
            if not args or not args[0].isdigit():
                print("Erro: use 'frames <n>', ex: frames 3")
                continue
            num_frames = int(args[0])
            print(f"Número de quadros definido para {num_frames}.")
        case "trace":
            if not args:
                print("Erro: use 'trace <arquivo>', ex: trace traces/silberschatz2001.trace")
                continue
            trace_path = args[0]
            trace_refs = ler_trace(trace_path)
            if trace_refs is not None:
                print(f"Arquivo de traço '{trace_path}' carregado ({len(trace_refs)} referências).")
        case "run":
            if not (algoritmo_inst and num_frames and trace_refs):
                print("Faltam parâmetros! Use 'algo', 'frames' e 'trace' antes de rodar a simulação.")
                continue
            print("Executando simulação...")
            ultimo_resultado = algoritmo_inst.executa_algoritmo(trace_refs, num_frames)
            imprimir_resultado(ultimo_resultado)
        case "stats":
            imprimir_resultado(ultimo_resultado)
        case _:
            print("Comando inválido. Digite 'help' para ver os comandos.")