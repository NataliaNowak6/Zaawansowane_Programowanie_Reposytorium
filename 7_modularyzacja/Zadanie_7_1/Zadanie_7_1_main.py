from Magazine import Product

def main():
    p1 = Product.Product("Laptop", 5000)
    p2 = Product.Product("Smartphone", 2500)

    print(p1)
    print(p1.greet())

    print(p2)
    print(p2.greet())

if __name__ == "__main__":
    main()