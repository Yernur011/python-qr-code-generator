# test
# test 23
# test qwerty


# Генерация QR кода
# import segno
#
# qrcode = segno.make_qr("testing pull request")
# qrcode.save(
#     "borderless_qrcode1.png",
#     scale=20
# )
#



############################################################

#Запись чего то в файл

"""
with open('file.txt', 'w') as file:
    # Записываем строку в файл
    for i in range(10000000000):
        number = str(i).zfill(10)
        print(number)
        file.write(number + "\n")
"""
############################################################

# отправка сообщения whats app

import pywhatkit


qrcode = segno.make_qr("testing pull request")
qrcode.save(
    "borderless_qrcode1.png",
    scale=20
)