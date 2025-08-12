filename = "sample.txt"

try:
    with open(filename, "r") as file:
        print("reading file content:")
        for i, line in enumerate(file, start=1):
            print(f"line {i} : {line.strip()}")
except FileNotFoundError:
    print(f"error: the file '{filename}' was not found")