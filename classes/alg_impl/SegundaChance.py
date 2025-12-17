from classes.Algoritmo import Algoritmo

class SegundaChance(Algoritmo):

    def __init__(self):
        self.nome = "Segunda chance"

    def executa_algoritmo(self, cadeia_ref, total_quadros):
        quadros = []
        ref_bit = {}
        ponteiro = 0
        faltas_pagina = 0
        eviccoes = 0

        for p in cadeia_ref:
            # Page hit
            if p in quadros:
                ref_bit[p] = 1
                continue

            faltas_pagina += 1

            # Memória ainda não cheia
            if len(quadros) < total_quadros:
                quadros.append(p)
                ref_bit[p] = 1
            else:
                # Procura vítima
                while True:
                    atual = quadros[ponteiro]
                    if ref_bit[atual] == 0:
                        # Substitui
                        quadros[ponteiro] = p
                        del ref_bit[atual]
                        eviccoes += 1
                        ref_bit[p] = 1
                        ponteiro = (ponteiro + 1) % total_quadros
                        break
                    else:
                        ref_bit[atual] = 0
                        ponteiro = (ponteiro + 1) % total_quadros

        return {
            "algoritmo": self.nome,
            "total_quadros": total_quadros,
            "total_referencias": len(cadeia_ref),
            "faltas_pagina": faltas_pagina,
            "eviccoes": eviccoes,
            "conjunto_residente": list(quadros)
        }