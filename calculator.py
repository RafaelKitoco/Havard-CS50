def main():
    x = int(input("introduza o valor do x "))
    print(f"o quadrado do {x} é {quadrado(x)}")
    
def quadrado(n):
    return pow(n, 2)

main()