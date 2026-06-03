students = [
    ("An", 22, 9.0),    # Điểm 9.0, Tuổi 22
    ("Bình", 19, 9.0),  # Điểm 9.0, Tuổi 19 (Trùng điểm với An nhưng ít tuổi hơn)
    ("Cường", 19, 7.5),
    ("Dũng", 20, 9.5)
]

students.sort(key = lambda x:( -x[1], x[2]))
for student in students:
    print(student)