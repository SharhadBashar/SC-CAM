from os.path import exists

file = 'train_aug.txt'


with open(file, 'r') as lines:
	for line in lines:
		# print(line)
		image, mask = line.strip("\n").split(' ')
		if not exists('./dataset' + image): print(image)
		if not exists('./dataset' + mask): print(mask)