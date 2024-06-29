x = int(input("\nThe number to get fact: "))

fact = 1

for i in range(1, x+1):
    fact = fact*i

print(f"\n{x}! = {fact}")
