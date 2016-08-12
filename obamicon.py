# skeleton code for obamicon
from PIL import Image

# ===============================================================
# define colors as variables so we can recall them later:
# dark blue: (0, 51, 76)
# red: (217, 26, 33)
# light blue: (112, 150, 158)
# yellow: (252, 227, 166)
# ===============================================================
dark_blue = (0, 51, 76)
red = (217, 26, 33)
light_blue = (112, 150, 158)
yellow = (252, 227, 166)
pixel_list = []
# ===============================================================
# define a function that obama-fies the image.
# this function will take our images' pixel list as a parameter.
# for each pixel in your image's pixel list, "obama-fy" it by 
# creating a new RGB value (dark blue, red, light blue, or yellow) 
# based on the intensity of that pixel. return a pixel list 
# containing the RGB values of the obamafied picture.
# ===============================================================
def obamafy(pixel_list):
	for item in pixel_list:
		intensity = item[0] + item[1] + item[2]
		if intensity > 182:
			pixel_list[item] = dark_blue
		elif intensity >= 182 < 364:
			pixel_list[item] = red
		elif intensity >= 364 < 546:
			pixel_list[item] = light_blue
		else:
			pixel_list[item] = yellow



	# 	if intensity is < 182 then add dark blue to the new list
	# else if intensity is >= 182 and < 364 then add red to the new list
	# else if intensity is >= 364 and < 546 then add light blue to the new list
	# else add yellow to the new list
	# get my pixe list 
	# loop through the pixel list and get each pixel individaually 
	# decide which pixel does into each category 
# ===============================================================
# ask the user for the image name and open the image
file = input("File Name")
im = Image.open(file)
picture = list(im.getdata())
# print(picture)
obamafy(picture)
print(pixel_list)

# im.getdata(im)
im.show("im")

# ===============================================================
# convert the image into a list of pixel RGB values
# ===============================================================
#for loop and conditionals 
# im.getdata("obama.jpe")


# ===============================================================
# obamafy your image by calling your function
# ===============================================================
#just call the functions 
# ===============================================================
# create a new image and copy the new obama-fied pixel list into the image
# ===============================================================

# ===============================================================
# finally, show and save the image
# ===============================================================

