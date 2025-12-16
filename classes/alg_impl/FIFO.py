from classes.Algoritmo import Algoritmo
from collections import deque

class FIFO(Algoritmo):

    def __init__(self):
        self.nome = "FIFO"

    def executa_algoritmo(self, cadeia_ref, total_quadros):
        quadros = set()
        fila = deque()
        faltas_pagina = 0
        eviccoes = 0

        for p in cadeia_ref:
            if p in quadros:
                continue

            faltas_pagina += 1

            if len(frames) < num_frames:
                frames.add(p)
                fila.append(p)
            else:
                velha = fila.popleft()
                frames.remove(velha)

                eviccoes += 1

                frames.add(p)
                fila.append(p)

        return {
            "algoritmo": self.nome,
            "total_quadros": total_quadros,
            "total_referencias": len(cadeia_ref),
            "faltas_pagina": faltas_pagina,
            "eviccoes": eviccoes,
            "conjunto_residente": list(quadros.keys())
        }
