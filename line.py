from particle import particle

class line:
    
    def __init__(self, a : particle, b : particle, size : float) -> None:
        self.a = a
        self.b = b
        self.size = size
        
    def len(self) -> float:
        len = self.a.r - self.b.r
        return len.mag()
        