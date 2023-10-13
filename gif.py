import os 
import imageio

file_list= sorted(os.listdir("assignment8/images"))

IMAGES=[]

for file_name in file_list:
    file_path = "assignment8/images/" + file_name
    image = imageio.imread(file_path)
    IMAGES.append(image)


imageio.mimsave("assignment8/my_output.gif" , IMAGES)