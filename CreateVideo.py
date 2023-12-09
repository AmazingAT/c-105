import cv2
import os

path = "Images"

images = []

for image in os.listdir(path):
    name,extension = os.path.splitext(image)
    if extension in [".jpg",".png",".jpeg",".gif"]:
        #            "Image/110.jpg"
        file_name  = path +"/"+image
        images.append(file_name)

# print(len(images))

count = len(images)
frame  = cv2.imread(images[0])
height, width, channels = frame.shape

size  = (width,height)
print(size)

out = cv2.VideoWriter("Video.mp4", cv2.VideoWriter_fourcc(*"DIVX"),50,size)


for i in range(0,count-1):
    frame = cv2.imread(images[i])
    out.write(frame)
out.release()
print("Done")
