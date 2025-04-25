class CuboRubik:
    def __init__(self):
        self.caras = {
            'U': ['W']*9,
            'D': ['Y']*9,
            'L': ['O']*9,
            'R': ['R']*9,
            'F': ['G']*9,
            'B': ['B']*9,
        }

    def rotar_horario(self, cara):
        c = self.caras[cara]
        self.caras[cara] = [c[i] for i in [6, 3, 0, 7, 4, 1, 8, 5, 2]]

    def mover_U(self):
        self.rotar_horario('U')        # Solo ejemplo simple sin afectar bordes aún
 


