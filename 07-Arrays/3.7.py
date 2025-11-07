names = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]
longest_name = ""
for name in names:
    if len(name) > len(longest_name):
        longest_name = name

print("Names:", end=" ")
for name in names:
    print(name, end=" ")
print()
print("Longest name:", longest_name)
