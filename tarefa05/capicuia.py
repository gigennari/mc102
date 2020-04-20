capicuia = input(str())

if len(capicuia) == 1:
	print('sim')

elif len(capicuia) == 2:
	if capicuia[0] == capicuia[1]:
		print('sim')
	else:
		print('não')

elif len(capicuia) == 3:
	if capicuia[0] == capicuia[2]:
		print('sim')
	else:
		print('não')


elif len(capicuia) == 4:
	if capicuia[0] == capicuia[3] and capicuia[1] == capicuia[2]:
		print('sim')
	else:
		print('não')

else:
	print('não')
