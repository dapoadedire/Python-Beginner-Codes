from PIL import Image
img = Image.open("rudiger.jpg")
bw = img.convert("L")
bw.show()