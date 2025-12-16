from classes.Algoritmo import Algoritmo

class NRU(Algoritmo):

    def __init__(self, reset_intervalo):
        self.nome = "NRU"
        self.reset_intervalo = reset_intervalo

    def executa_algoritmo(self, cadeia_ref, quadros):
        quadros = []
        bits = {}  # pagina -> [R, M]
        faltas_pagina = 0
        eviccoes = 0

        for i, p in enumerate(cadeia_ref):
            # Reseta bits R periodicamente
            if i % self.reset_intervalo == 0:
                for q in bits:
                    bits[q][0] = 0

            if p in quadros:
                bits[p][0] = 1
                continue

            faltas_pagina += 1

            if len(quadros) < total_quadros:
                quadros.append(p)
                bits[p] = [1, 0]
            else:
                # Classifica páginas
                classes = {0: [], 1: [], 2: [], 3: []}

                for q in quadros:
                    R, M = bits[q]
                    classe = 2 * R + M
                    classes[classe].append(q)

                # Escolhe vítima da menor classe não vazia
                for c in range(4):
                    if classes[c]:
                        vitima = random.choice(classes[c])
                        break

                quadros.remove(vitima)
                del bits[vitima]

                eviccoes += 1

                quadros.append(p)
                bits[p] = [1, 0]

        return {
            "algoritmo": self.nome,
            "total_quadros": total_quadros,
            "total_referencias": len(cadeia_ref),
            "faltas_pagina": faltas_pagina,
            "eviccoes": eviccoes,
            "conjunto_residente": list(quadros.keys())
        }