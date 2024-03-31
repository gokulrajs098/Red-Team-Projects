import magic
# Install the magic library using the command "pip install python-magic-bin"

def file_identifier(file_path):

	#Create a magic instance. It initializes a magic database and provide methods to perform file type identification
	magic_instance = magic.Magic()

	with open (file_path, 'rb') as file:

		# magic instance reads first 2048 bytes of data and detects the file type
		file_type = magic_instance.from_buffer(file.read(2048))
		return file_type


file_path = input("Enter the file path")
file_type = file_identifier(file_path)
print(f"The file type is {file_type}")