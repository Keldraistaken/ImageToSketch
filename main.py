import cv2

file_path = input("Enter File Path:")

img_gscale = cv2.cvtColor(cv2.imread(file_path), cv2.COLOR_BGR2GRAY)
blr = cv2.GaussianBlur(255-img_gscale, (21, 21), 0)
blr_invert = 255 - blr

sketch = cv2.divide(img_gscale, blr_invert, scale=256.0)
cv2.imshow("Pencil Sketch", sketch)
cv2.waitKey(0)
