import segno

qrcode = segno.make_qr("Hello, World!")
qrcode.save(
    "borderless_qrcode1.png",
    scale=20
)