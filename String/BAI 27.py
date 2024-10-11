#Hàm title() dùng để chuyển viết hoa chữ cái đầu tiên của mỗi từ trong chuỗi
s="machine learning"
s=s.title()
print(s)
#Hàm translate() dùng để biến đổi chuỗi theo bảng chuyển đổi kí tự
s="machine learning"
trans=str.maketrans("ae","ou")
s=s.translate(trans)
print(s)