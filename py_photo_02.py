from PIL import Image


photo_path = r'./algebra_campus.jpg'
photo = Image.open(photo_path)

photo_h = photo.size[0]
photo_v = photo.size[1]

left = 0 + 500
upper = 0 + 500
right = photo_h - 500
lower = photo_v - 500

photo_crop = photo.crop((left, upper, right, lower))

photo_crop.show()
