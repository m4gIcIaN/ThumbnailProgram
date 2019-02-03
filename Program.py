from PIL import Image

def main():
	imageEdit = input("What image would you like to edit: ")
	fileName = imageEdit.split(".")
	thumbSizes = [(8, 8), (16, 16), (32, 32), (64, 64), (128, 128)]

	inputSize = int(input("What size of thumbnail would you like?\n 1.(8,8)\n 2.(16,16)\n 3.(32,32)\n 4.(64,64)\n 5.(128,128)\n Type a Number: "))

	if inputSize == 1:
		wantedSize = thumbSizes[0]
		sizeString = "8x8"
		print("Thumbnail size will be set to 8x8")
	elif inputSize == 2:
		wantedSize = thumbSizes[1]
		sizeString = "16x16"
		print("Thumbnail size will be set to 16x16")
	elif inputSize == 3:
		wantedSize = thumbSizes[2]
		sizeString = "32x32"
		print("Thumbnail size will be set to 32x32")
	elif inputSize == 4:
		wantedSize = thumbSizes[3]
		sizeString = "64x64"
		print("Thumbnail size will be set to 64x64")
	elif inputSize == 5:
		wantedSize = thumbSizes[4]
		sizeString = "128x128"
		print("Thumbnail size will be set to 128x128")
	else:
		print("No correct value chosen. Setting to default size of (16, 16)")
		wantedSize = thumbSizes[1]


	firstImage = Image.open(imageEdit)
	firstImage.thumbnail(wantedSize)
	firstImage.save(fileName[0] + "Edited(" + sizeString + ")." + fileName[1])
	print("Finished")


if __name__ == "__main__":
	main()