from classes.Algoritmo import Algoritmo

class Otimo(Algoritmo):

    def __init__(self):
        self.nome = "Otimo"

    def executa_algoritmo(self, cadeia_ref, total_quadros):
        quadros = set()
        faltas_pagina = 0
        eviccoes = 0
        n = len(cadeia_ref)

        for i, p in enumerate(cadeia_ref):
            if p in quadros:
                continue

            faltas_pagina += 1

            if len(quadros) < total_quadros:
                quadros.add(p)
            else:
                futuro = {}

                for q in quadros:
                    try:
                        futuro[q] = cadeia_ref[i+1:].index(q)
                    except ValueError:
                        futuro[q] = float('inf')

                vitima = max(futuro, key=futuro.get)
                quadros.remove(vitima)
                eviccoes += 1
                quadros.add(p)

        return {
            "algoritmo": self.nome,
            "total_quadros": total_quadros,
            "total_referencias": len(cadeia_ref),
            "faltas_pagina": faltas_pagina,
            "eviccoes": eviccoes,
            "conjunto_residente": list(quadros)
        }