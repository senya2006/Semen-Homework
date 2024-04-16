class Apple:
    def __init__(self, name, founded_year, center, ceo, products):
        self.name = name
        self.founded_year = founded_year
        self.center = center
        self.ceo = ceo
        self.products = products

    def introduce(self):
        print(f"Welcome to {self.name}!")
        print(f"Founded in {self.founded_year} and headquartered in {self.center}.")
        print(f"Current CEO: {self.ceo}")
        print("Our popular products are:")
        for product in self.products:
            print(product)

apple = Apple(
    name="Apple Inc.",
    founded_year=1976,
    center="California, United States",
    ceo="Tim Cook",
    products=["iPhone", "iPad", "Mac", "Apple Watch", "AirPods", "Apple Vision pro"]
)

apple.introduce()