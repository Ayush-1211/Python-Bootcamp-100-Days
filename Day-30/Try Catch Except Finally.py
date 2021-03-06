#FileNotFound

try:
    file = open("data.txt")
    dict = {"key": "value"}
    print(dict["alfjkads"])
except FileNotFoundError:
    file = open("data.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed")