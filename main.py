from classes.alg_impl.FIFO import FIFO
from classes.alg_impl.LFU import LFU
from classes.alg_impl.LRU import LRU
from classes.alg_impl.MFU import MFU
from classes.alg_impl.NRU import NRU
from classes.alg_impl.Otimo import Otimo
from classes.alg_impl.SegundaChance import SegundaChance

import argparse

ALGORITMOS = {
    "fifo": FIFO,
    "lru": LRU,
    "opt": Otimo,
    "sc": SegundaChance,
    "nru": NRU,
    "lfu": LFU,
    "mfu": MFU
}

def imprimir_resultado(resultado):
    total_refs = resultado["total_referencias"]
    faltas = resultado["faltas_pagina"]
    taxa = (faltas / total_refs) * 100 if total_refs > 0 else 0.0

    print(f"Algoritmo: {resultado['algoritmo']}")
    print(f"Frames: {resultado['total_quadros']}")
    print(f"Referências: {total_refs}")
    print(f"Faltas de página: {faltas}")
    print(f"Taxa de faltas: {taxa:.2f}%")
    print(f"Evicções: {resultado['eviccoes']}")
    print("Conjunto residente final:")

    # frame_ids sempre de 0 até total_quadros-1
    frame_ids = ''.join(str(i) for i in range(resultado["total_quadros"]))

    # page_ids na ordem recebida
    page_ids = ''.join(str(p) for p in resultado["conjunto_residente"])

    print(f"frame_ids:{frame_ids}")
    print(f"page_ids:{page_ids}")

def ler_trace(caminho):
    with open(caminho, "r") as f:
        return [int(linha.strip()) for linha in f if linha.strip()]


parser = argparse.ArgumentParser(
    description="Simulador de algoritmos de paginação"
)

parser.add_argument("--algo", required=True, choices=ALGORITMOS.keys())
parser.add_argument("--frames", type=int, required=True)
parser.add_argument("--trace", required=True)

args = parser.parse_args()

cadeia_ref = ler_trace(args.trace)

algoritmo_cls = ALGORITMOS[args.algo]
algoritmo = algoritmo_cls()

resultado = algoritmo.executa_algoritmo(cadeia_ref, args.frames)

imprimir_resultado(resultado)