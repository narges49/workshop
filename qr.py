import qrcode

url = "https://github.com/narges49/workshop/blob/main/file2.py"


qr = qrcode.QRCode(
    version=1, 
    error_correction=qrcode.constants.ERROR_CORRECT_H, 
    box_size=10, 
    border=4,
)


qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill_color="purple", back_color="white")


file_name = "my_qrcode.png"
img.save(file_name)
