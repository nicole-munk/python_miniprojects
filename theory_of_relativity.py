#Programa para calcular la energía de un objeto según la teoría de la relatividad

def total_energy(mass):
    c=3*10**8
    energy=mass*c**2
    return energy

my_energy=total_energy(52)
print(my_energy)
