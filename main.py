# test


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


def send_message():
    mobile = '+77066693596'
    message = 'Ассаламагалейкум'
    pywhatkit.sendwhatmsg(mobile, message, 14, 46)
    print("Successfully Sent!")


def main():
    send_message()


if __name__ == '__main__':
    main()