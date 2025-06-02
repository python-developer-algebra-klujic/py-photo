from PIL import Image
from PIL.Image import Transpose

photo_path = r'./algebra_campus.jpg'
photo = Image.open(photo_path)

help(photo.transpose)

# photo_flip_lr = photo.transpose(method=Transpose.FLIP_LEFT_RIGHT)
# photo_flip_lr.show()

# photo_flip_tb = photo.transpose(method=Transpose.FLIP_TOP_BOTTOM)
# photo_flip_tb.show()

# photo_flip_r90 = photo.transpose(method=Transpose.ROTATE_90)
# photo_flip_r90.show()

# photo_flip_r180 = photo.transpose(method=Transpose.ROTATE_180)
# photo_flip_r180.show()

# photo_flip_r270 = photo.transpose(method=Transpose.ROTATE_270)
# photo_flip_r270.show()

# photo_flip_transpose = photo.transpose(method=Transpose.TRANSPOSE)
# photo_flip_transpose.show()

photo_flip_transverse = photo.transpose(method=Transpose.TRANSVERSE)
photo_flip_transverse.show()
