import cv2
image = cv2.imread('images/dungeon.png')

# Grayscale
image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

sobel_x = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)
sobel_OR = cv2.bitwise_or(sobel_x, sobel_y)

laplacian = cv2.Laplacian(image, cv2.CV_64F)

canny = cv2.Canny(image, 30, 200)

