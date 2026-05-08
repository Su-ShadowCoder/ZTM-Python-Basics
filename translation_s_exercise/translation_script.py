
# situation:
# translate the txt file document by using a python script


# strategy:
# 1 first look for a translation module

# 2 check and validate translation module

# 3 make sure you have env for the module that belongs to the project

# 4 install the module in the specific env folder

# 5 read the documentation further in how to use it 

# 6 write the file code and  use the method specefic for it 



from translate import Translator

translator = Translator(to_lang='ja')


try:
	with open('./textfile.txt', mode='r+') as my_file:
		text = my_file.read()
		translation = translator.translate(text)
		print(translation)
		with open('./test-ja.txt', mode='w') as my_file2:
			my_file2.write(translation)
except FileNotFoundError as err:
	print('file does not exist!')
