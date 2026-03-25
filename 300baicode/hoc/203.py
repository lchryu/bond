s = input()  # ví dụ chuỗi có dấu cách

# Lọc ra các ký tự là chữ cái
letters = [ch for ch in s if ch.isalpha()]

# Tìm chữ cái có mã ASCII nhỏ nhất
min_letter = min(letters)
print( min_letter, end= ": ")
print(ord(min_letter))