side_a = float(input("Please enter 1 value: "))
side_b = float(input("Please enter 2 value: "))
side_c = float(input("Please enter 3 value: "))

hp = (side_a + side_b + side_c) / 2
area = (hp*(hp - side_a) * (hp - side_b) * (hp-side_c))**0.5

print("Side A = ", side_a, "Side B = ", side_b, "Side C = ", side_c)
print("Perimetr: ", hp, "cm")
print("Area: ", area, "cm")

