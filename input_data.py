import os, shutil 
path = os.getcwd()
print(path)

files = []

# for r, d, f in os.walk(path):
	# for file in f:
		# if '.jpg' in file:
			# files.append(os.path.join(r, file))
			
# for f in files:
	# print(f)
	# break
	
# folders = []
# for r, d, f in os.walk(path):
	# for folder in d:
		# folders.append(os.path.join(r, folder))
		
# for f in folders:
	# print(f)
	# break
	
def main():
	print("start")
	i=0
	# for root, dir, filename in os.walk("dataset/test/packages/"):
		# for file in filename:
			# if '.jpg' in file:
				# files.append(os.path.join(root, file))
	
	# for f in files:
		# print(f)
		# dst = "package" + str(i).rjust(5,"0") + ".jpg"
		# src = f
		# dst = "dataset/new_folder/package/" + dst
		
		# # os.rename(src, dst)
		# shutil.copyfile(src,dst)
		# i += 1
		# print(f)
		# # if i==10:
			# # break
	
	vendorMap = {'fruit' : 'fruit', 
				'package' : 'package',
				'veg' : 'veg'
				}
	path = 'dataset/new_folder'
	files1 = os.listdir(path)
	print(files1)
	
	for r, d, f in os.walk(path):
		for file in f:
			if '.jpg' in file :
				files.append(os.path.join(r,file))
				
			
	for f in files:
		shutil.copy(f, 'dataset/input_folder/')
		# break
			# else:
				# print("error")
	print('end')
	
	# for root, dir, filename in os.walk("dataset/new_folder"):
		# for file in filename:
			# if '.jpg' in file:
				# files.append(os.path.join(root, file))
				
		# for f in files:
			# src = f
			# dst =  "dataset/input_folder"
			# i += 1
			
			# if i <= 10:
				# print(f)
				# # break
				# print(i)
				# shutil.copyfile(src,dst)
if __name__ == '__main__':
	main()