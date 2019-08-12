import os

os.chdir('path')
for file_list in os.listdir():
	file_name, file_ext = os.path.splitext(file_list)
	try:
		file_title, file_num = file_name.split(' ')
	except Exception:
		file_name+=" (0)" 
		file_title, file_num = file_name.split(' ')
	file_num = str(int(file_num.strip()[1:-1])+1).zfill(2)
	file_name = 'file name {}{}'.format(file_num, file_ext)	
	os.rename(fiel, file_name)
	print(file_name)

