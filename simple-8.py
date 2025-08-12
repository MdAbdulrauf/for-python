filename = "output.txt"

text_to_write = input("Enter text to write to the file: ")
with open(filename, "w") as file:
    file.write(text_to_write + "\n")
print("Data successfully written to output.txt.")

text_to_append = input("Enter additional text to append: ")
with open(filename, "a") as file:
    file.write(text_to_append + "\n")
print("Data successfully appended.")

print("\nFinal content of output.txt:")
with open(filename, "r") as file:
    for line in file:
        print(line.strip())
