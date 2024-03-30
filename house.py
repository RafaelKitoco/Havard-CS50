name = input("what's your name? ")

match name:
    case "Rafael":
        print("Ola Rafael")
    case "Julia":
        print("Ola Julia")
    case _:
        print("who ?")