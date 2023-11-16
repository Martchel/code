import cv2
import numpy as np
import matplotlib.pyplot as plt

# The next step is to read the image using the imread function 
# and then convert it to RGB format with the help of the 
# cvtColor function. We then plot the image using the imshow 
# function. The code for the same is shown below:

img =cv2.imread("image.img")
if img.shape[2] == [3]:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

plt.figure(figsize=(10,10))
plt.imshow(img)
plt.axis("off")
plt.title("Orignial Image")
plt.show()


# The next step in the process is to convert the image into a 
# grayscale format using the cvtColor function. The reason 
# behind doing so is that it simplifies the process and helps 
# in the time complexity of the program later on.

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)

plt.figure(figsize=(10,10))
plt.imshow(gray, cmap = "gray")
plt.axis("off")
plt.title("Grayscale Image")
plt.show()

# To make things simpler for us, we will get an edged image of 
# the grayscale image and then apply the convolutional network 
# to the image.

edges = cv2.adaptiveThreshold(gray, 255, 
                               cv2.ADAPTIVE_THRESH_MEAN_C,
                               cv2.THRESH_BINARY, 9, 9)

plt.figure(figsize=(10,10))
plt.imshow(edges, cmap = "gray")
plt.axis("off")
plt.title("Edged Image")
plt.show()

# The final step is to apply the convolutional filter using 
# the bilateralFilter function. We then make use of the bitwise 
# operation and pass the original image and the edged image to 
# turn images into cartoons.

color = cv2.bilateralFilter(img, 9, 250, 250)
cartoon = cv2.bitwise_and (color, color, mask=edges)
plt.figure(figsize=(10,10))
plt.imshow(cartoon, cmap = "gray")
plt.axis("off")
plt.title("Cartoon Image")
plt.show()