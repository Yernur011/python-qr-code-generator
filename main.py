import segno

qrcode = segno.make_qr("testing pull request")
qrcode.save(
    "borderless_qrcode1.png",
    scale=20
)