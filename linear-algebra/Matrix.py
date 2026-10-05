class Matrix:
    MOD = 10 ** 9 + 7
    def __init__(self, data: List[List[int]] | None = None) -> None:
        if data is None:
            self.a = [[0, 0], [0, 0]]
        else:
            self.a = data    
    def __mul__(self, other: Matrix) -> Matrix:
        n = len(self.a)
        m = len(self.a[0])
        l = len(other.a[0])
        product = Matrix([[
            sum(self.a[i][k] * other.a[k][j] for k in range(m)) % MOD
            for j in range(l)
        ] for i in range(n)])
        return product

def bigmod(base: Matrix, power: int) -> Matrix:
    if power == 1:
        return base
    r = bigmod(base, power // 2)
    if power % 2 == 1:
        return r * r * base
    else:
        return r * r
