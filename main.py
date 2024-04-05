import segno

qrcode = segno.make_qr("Hello, World from second branch!")
qrcode.save(
    "borderless_qrcode1.png",
    scale=20
)