import segno

qrcode = segno.make_qr("")
qrcode.save(
    "borderless_qrcode1.png",
    scale=20
)