from PIL import Image, ImageFilter

img = Image.open(r'D:\Users\Lietail\Code\Scripting\venv\Imagenes\astro.jpg')

new_image = img.thumbnail((400,400))
new_image.save("thumbnail.jpg")



'''
filtered_img = img.convert('L')
filtered_img.save("grey.png","png")
filtered_img.show()
'''
