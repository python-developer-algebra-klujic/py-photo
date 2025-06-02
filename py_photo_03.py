from PIL import Image


photo_path = r'./algebra_campus.jpg'
photo = Image.open(photo_path)

photo_bw = photo.convert(mode='L')

photo_bw.save(r'./algebra_campus_bw.jpg')
photo_bw.show()
