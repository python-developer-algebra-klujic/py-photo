from PIL import Image, ImageFilter

photo_path = r'./algebra_campus.jpg'
photo = Image.open(photo_path)

# photo.filter(ImageFilter.CONTOUR).show()
# photo.filter(ImageFilter.EDGE_ENHANCE).show()
# photo.filter(ImageFilter.EDGE_ENHANCE_MORE).show()
# photo.filter(ImageFilter.EMBOSS).show()
# photo.filter(ImageFilter.FIND_EDGES).show()
# photo.filter(ImageFilter.SHARPEN).show()
# photo.filter(ImageFilter.SMOOTH).show()
# photo.filter(ImageFilter.SMOOTH_MORE).show()

# photo.filter(ImageFilter.BoxBlur(radius=15)).show()
# photo.filter(ImageFilter.GaussianBlur(radius=15)).show()
# photo.filter(ImageFilter.MaxFilter(size=5)).show()
# photo.filter(ImageFilter.MedianFilter(size=5)).show()
photo.filter(ImageFilter.MinFilter(size=5)).show()