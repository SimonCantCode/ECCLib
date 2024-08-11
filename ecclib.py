
# The eliptic curve we encrypt on
#secp256k1

# y^2 = x^3 + 7 (mod p)
# y^2 = x^3 + ax + b 

def duplicatePoint(point: tuple, a, b, mod) -> tuple:
    x1 = point[0]
    y1 = point[1]

    # The pow function has to be used to get the correct multiplicative inverse of the denominator
    l = (3 * x1**2 + a) * pow(2 * y1, -1, mod)
    n = y1 - l * x1
    x2 = (l**2 - 2 * x1) % mod
    y2 = (-l * x2 - n) % mod

    return (x2, y2)

def addPoints(pointP: tuple[int, int], pointQ: tuple[int, int], a, b, mod) -> tuple[int,int]:
    if pointP == pointQ:
        return duplicatePoint(pointP, a, b, mod)
    
    x1 = pointP[0]
    y1 = pointP[1]
    x2 = pointQ[0]
    y2 = pointQ[1]

    # The denominator of l has to be separate to get a whole number multiplicative inverse
    # l = (y2 - y1) * 1/(x2 - x1) done modually is the same as:
    l = (y2 - y1) * pow(x2 - x1, -1, mod) # % mod 
    
    n = y1 - l * x1
    x3 = (l**2 - x1 - x2) % mod
    y3 = (-l * x3 - n) % mod

    return (x3, y3)

def scalePoint(n: int, point: tuple[int], a, b, mod) -> tuple[int]:
    x1 = point[0]
    y1 = point[1]

    if n <= 1:
        return

    newPoint: list[int] = list(uplicatePoint(point, a, b, mod))
    for i in range(n-2): # As to not run if n = 2
        newPoint = list(addPoints(newPoint, point, a, b, mod))
        print(newPoint)

    return tuple(newPoint)


# TODO: 
#make a class with operator overloading
#diffie-helman
#real numbers

def main():
    a=0
    b=7

    # 6.5
    #print(duplicatePoint((0,1), 0,1,7))

    # 6.10
    print(scalePoint(4, (2,3),0,1,11))

if __name__ == "__main__":
    main()
