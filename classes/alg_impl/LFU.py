from classes.Algoritmo import Algoritmo
from collections import OrderedDict

class LFU(Algoritmo):

    def __init__(self):
        self.nome = "LFU"

    def executa_algoritmo(self, cadeia_ref, total_quadros):
        quadros = set()
        freq = {}
        tempo = {}
        faltas_pagina = 0
        eviccoes = 0
        tempo_atual = 0

        for p in cadeia_ref:
            tempo_atual += 1

            if p in quadros:
                freq[p] += 1
                continue

            faltas_pagina += 1
            if len(quadros) < total_quadros:
                quadros.add(p)
                freq[p] = 1
                tempo[p] = tempo_atual
            else:
                # escolhe vítima: menor frequência, depois mais antiga
                vitima = min(
                    quadros,
                    key=lambda q: (freq[q], tempo[q])
                )

                quadros.remove(vitima)
                del freq[vitima]
                del tempo[vitima]
                eviccoes += 1
                quadros.add(p)
                freq[p] = 1
                tempo[p] = tempo_atual

        return {
            "algoritmo": self.nome,
            "total_quadros": total_quadros,
            "total_referencias": len(cadeia_ref),
            "faltas_pagina": faltas_pagina,
            "eviccoes": eviccoes,
            "conjunto_residente": list(quadros)
        }