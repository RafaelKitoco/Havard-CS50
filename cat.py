i = 3

while i != 0:
    print("meow")
    i -= 1

for i in [1, 2, 3]:
    print("meow")

for i in range(3):
    print("meow")

print("meow\n" * 3, end="")

while True:
    n = int(input("what's number "))
    if n > 0:
        break

for _ in range(n):
    print("meow")

def main():
    n = get_number()
    meow(n)

def get_number():
    n = int(input("what's number"))
    return n

def meow(n):
    for _ in range(n):
        print("meow")

main()