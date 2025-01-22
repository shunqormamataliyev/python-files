# import os
#
# #faylni o'chirish
#
# file_path = "example.txt"
# if os.path.exists(file_path):
#     os.remove(file_path)
#     print(f"Fole {file_path} o'chirildi")
# else:
#     print('Fayl mavjud emas')

import os

dir_path = "/manzil"

if os.path.exists((dir_path)) and os.path.isdir(dir_path):
    os.rmdir(dir_path)  #bo'sh direktoriyani o'chiradi
    print(f"Direktoriya {dir_path} o'chirildi")

else:
    print(("Direktoriyaning mavjud emasligi yoki u bo'sh emasligi"))