from PIL import Image
import pytesseract

def process_image(iamge_name, lang_code):
	return pytesseract.image_to_string(Image.open(iamge_name), lang=lang_code)

def print_data(data):
	print(data)

def output_file(filename, data):
	file = open(filename, "w+")
	file.write(data)
	file.close()

def main():
	filepath = input("Enter filepath: ")
	img = Image.open(filepath)
	data = process_image(img, "eng")
	print_data(data)
	output_file(filepath + ".txt", data)

if  __name__ == '__main__':
	main()
