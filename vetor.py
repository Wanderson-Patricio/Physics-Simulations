from math import sqrt

class vector:
    
    def __init__(self, x : float, y : float) -> None:
        """Inicializa um vetor com suas componentes em x e y"""

        self.x = x
        self.y = y

    ################################################################
    
    def __add__(self, v):
        """Soma o vetor atual com o vetor v, e retorna um novo vetor"""
        if isinstance(v, vector):
            return vector(self.x + v.x, self.y + v.y)
        
        return None

    ################################################################
        
    def __sub__(self, v):
        """Subtrai o vetor atual com o vetor v, e retorna um novo vetor"""
        if isinstance(v, vector):
            return vector(self.x - v.x, self.y - v.y)
        
        return None

    ################################################################
    
    def __mul__(self, scalar : float):
        """multiplica o vetor atual por um escalar, e retorna um novo vetor"""
        return vector(self.x * scalar, self.y * scalar)

    ################################################################
    
    def __truediv__(self, scalar : float):
        """Divide o vetor atual por um escalar, e retorna um novo vetor"""
        if scalar != 0:
            return vector(self.x / scalar, self.y / scalar)
        else:
            raise ZeroDivisionError("Division by zero is not allowed.")

    ################################################################
    
    def mag(self) -> float:
        """Retorna o módulo do vetor atual"""
        return sqrt(self.x**2 + self.y**2)

    ################################################################
    
    def norm(self) -> None:
        """Normaliza o vetor atual, o tornando um vetor unitári"""
        mag = self.mag()
        if mag != 0:
            self.x /= mag
            self.y /= mag
        else:
            raise ZeroDivisionError('The current vetor is the null vector.')

    ################################################################
    
    def __str__(self) -> str:
        """Método para printar o vetor"""
        return f'({self.x}, {self.y})'

