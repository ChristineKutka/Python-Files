# You have a pic
# You want to Obamafy it
# You want to take pixels in the image and change their colors

# [(0,1,74), (234, 123, 23)]

# def randomfunction(obamas_address, cherish_middle_name, biggest_number_ever):
# 	print(obamas_address)

# randomfunction(??????)

def obamafy (pixel_list):

# if our pixel_list looks like this: [(0,1,74), (234, 123, 23)]
# Do this (aka loop) for every pixel in the image (represented as a pixel list):
for item in pixel_list:
	# item is going to look like this: (0,1,74) first

# Calculate the intensity values 
# - add the red, green, and blue values
	intensity = item[0] + item[1] + item[2]
	# tuple = (1,2,3)
	# list = [1,2,3]
	# tuple[0] # give me 1

# Change the values so the pixel color changes
# - Based on the rules below, change that pixel color from the original color to either dark blue, red, light blue, or yellow

# If the intensity < 182, then it's dark blue
# If the intensity is between 182 and 364, then it's red
# If the intensity is between 364 and 546, then it's light blue
# all other intensity values, it is yellow
	if intensity is < 182 then add dark blue to the new list
	else if intensity is >= 182 and < 364 then add red to the new list
	else if intensity is >= 364 and < 546 then add light blue to the new list
	else add yellow to the new list

# return the pixel list i was given that i edited to contain the RGB values of the obamafied picture.
	return new list 

# [dark blue, dark blue]