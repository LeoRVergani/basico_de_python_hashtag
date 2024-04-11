import os
# import datetime
# import pyautogui

# pyautogui.press("win")
# pyautogui.write("chrome")

# print(os.listdir("arquivos"))

# print(datetime.date.today())

lista_arquivos = os.listdir("arquivos")
# print(lista_arquivos)
# os.rename("arquivos/abr22.txt", "arquivos/22/abr22.txt")

for arquivo in lista_arquivos:
    if ".txt" in arquivo:
        if "22" in arquivo:
            os.rename(f"arquivos/{arquivo}", f"arquivos/22/{arquivo}")
        elif "23" in arquivo:
            os.rename(f"arquivos/{arquivo}", f"arquivos/23/{arquivo}")

            
