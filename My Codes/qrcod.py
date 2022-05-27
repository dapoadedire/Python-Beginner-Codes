from faker import Faker
fake= Faker()
print(fake.name())
print(fake.address())
print(fake.city())
print(fake.state())
print(fake.country())
print(fake.pylist())

print(fake.pydict())
print(fake.pyint())
print(fake.text())


fake_international= Faker(['it_IT', 'en_US', 'ja_JP'])

for i in range(10):
    print(fake_international.name())

"""

import qrcode 
img = qrcode.make("https://www.twitter.com/dapo_adedire")
img.save("\\Documents\\Dev\\Codes\\PYTHON\\qrcode.png"


import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('Some data')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

"""