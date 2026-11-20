
try:
    mass=int(input("Mass:"))
except ValueError:
    print("Mass is invalid")
else:
    c=3*pow(10,8)
    energy=mass*pow(c,2)
    print(f"Energy: {energy}")

