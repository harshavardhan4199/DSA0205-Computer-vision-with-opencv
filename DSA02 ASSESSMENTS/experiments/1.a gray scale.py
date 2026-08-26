from PIL import Image

img = Image.open(r"C:\Users\hv364\Downloads\mango image.jpeg")
gray = img.convert('L')
gray.save('gray_image.jpg')

resized = gray.resize((gray.width // 2, gray.height // 2))
resized.save('resized_gray.jpg')

threshold = gray.point(lambda p: 255 if p > 128 else 0)
threshold.save('thresholded_image.jpg')

gray.show()
threshold.show()
