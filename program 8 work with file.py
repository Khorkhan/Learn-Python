# write file
with open("data.txt", "w") as f:
    f.write("Hello World\n")

# read file
with open("data.txt", "r") as f:
    content = f.read()
    print(content)