from vetor import vector

class particle:
    
    def __init__(self, inicialPosition : tuple, mass : float, size : float, color : tuple ,isLocked : bool = False) -> None:
        """Inicializa uma partícula com as condições iniciais"""
        self.r : vector = vector(inicialPosition[0], inicialPosition[1])
        
        if mass != 0:
            self.m : float = mass
        else:
            raise ZeroDivisionError('Mass cannot be 0')
        
        self.size = size
        self.color = color
        self.v : vector = vector(0,0)
        self.a : vector = vector(0,0)
        self.locked : bool = isLocked
    
    def __str__(self) -> str:
        return self.r.__str__()
        
    def move(self, dt : float) -> None:
        """Move a partícula atual por um período dt"""
        if not self.locked:
            new_v = self.v + self.a * dt
            self.v = new_v
            new_r = self.r + self.v * dt
            self.r = new_r
            
    def applyForce(self, force : vector) -> None:
        """Calcula a aceleração quando é aplicada uma força"""
        self.a = force / self.m

