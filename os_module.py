import os

#faylni o'chirish

file_path = "example.txt"
if os.path.exists(file_path):
    os.remove(file_path)
    print(f"Fole {file_path} o'chirildi")
else:
    print('Fayl mavjud emas')