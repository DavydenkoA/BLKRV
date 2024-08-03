def izmer(width, height):
    width, height = map(int, input().split())
    print(f"Периметр прямоугольника, равен {(width + height)*2}")


izmer("width", "height")
