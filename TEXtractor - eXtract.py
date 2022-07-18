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
	data = process_image("Coursera Python for Everybody SPECIALIZATION.jpg", "eng")
	print_data(data)
	output_file("Coursera Python for Everybody SPECIALIZATION.txt", data)

if  __name__ == '__main__':
	main()