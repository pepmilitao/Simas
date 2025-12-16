from classes.Algoritmo import Algoritmo

class LRU(Algoritmo):

    def __init__(self):
        self.nome = "LRU"

    def executa_algoritmo(self, cadeia_ref, total_quadros):
        frames = OrderedDict()
        faltas_pagina = 0
        eviccoes = 0

        for p in cadeia_ref:
            if p in frames:
                frames.move_to_end(p)
            else:
                faltas_pagina += 1

                if len(frames) >= num_frames:
                    frames.popitem(last=False)
                    eviccoes += 1

                frames[p] = True

        return {
            "algoritmo": self.nome,
            "total_quadros": total_quadros,
            "total_referencias": len(cadeia_ref),
            "faltas_pagina": faltas_pagina,
            "eviccoes": eviccoes,
            "conjunto_residente": list(quadros.keys())
        }