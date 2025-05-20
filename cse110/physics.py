import math
mass = float(input("Mass (in kg): "))
gravity = float(input("Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): "))
time = float(input("Time (in seconds): "))
density = float(input("Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): "))
area = float(input("Cross sectional area (in m^2): "))
drag = float(input("Drag constant (0.5 for sphere, 1.1 for cylinder): "))

c = (1 / 2) * density * area * drag
vel = math.sqrt(mass * gravity / c) * (1 - math.exp((-math.sqrt(mass * gravity * c) / mass) * time))
print("\nThe inner value of c is: " + str(round(c, 3)))
print("The velocity after " + str(time) + " seconds is: " + str(round(vel, 3)) + " m/s")
