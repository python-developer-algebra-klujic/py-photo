from PIL import Image


photo_path = r'./algebra_campus.jpg'

# photo = Image.open('algebra_campus.jpg')
photo = Image.open(photo_path)


print(f'Format: {photo.format}')
print(f'Size: {photo.size}')
print(f'Mode: {photo.mode}')

photo.show()
