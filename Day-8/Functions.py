def greet():
    print("Hello Ayush")
    print("How do you do Ayush?")
    print("Isn't the weather nice today?")
greet()

print("-----------------------------------")

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")
greet_with_name("Ayush")

print("-----------------------------------")

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")
greet_with("Ayush","India")         # Positional Argument
greet_with(location="USA", name="Jack")     # Keyword Argument