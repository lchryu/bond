text = input("Nhập chuỗi hoặc số: ")
binary = ' '.join(format(ord(char), '08b') for char in text)
print("Mã nhị phân:", binary)
