try:
    with open("example.txt","x") as file:
        file.write("Fayl yangi amlimot bilan yaratildi")
except FileExistsError:
    print("fayl allaqachon mavjud")