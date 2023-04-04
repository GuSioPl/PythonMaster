name = input("Please give me name: ").strip().title()
#name = name.strip() removing white spaces from Left and right but no from between
#name = name.title()
print("Hello", name)
print("Hello " + name) #without space


x = float(input("What's x? "))
y = float(input("What's y "))

z = round(x + y)
print(f"{z}")