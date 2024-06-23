class Cookie:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color


cookie_one = Cookie("Green")
cookie_two = Cookie("Red")

print("\nCookie one is", cookie_one.get_color())
print("Cookie one is", cookie_two.get_color())

cookie_one.set_color("Yellow")

print("\nCookie one is", cookie_one.get_color())
print("Cookie one is", cookie_two.get_color())
