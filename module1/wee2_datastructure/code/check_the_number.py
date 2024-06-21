def check_the_number(n):
    """
    Kiểm tra xem số n có nằm trong khoảng từ 1 đến 4 hay không.
    """
    list_of_numbers = []
    result = ""
    for i in range(1, 5):
        # Thêm i vào list_of_numbers
        list_of_numbers.append(i)
    if n in list_of_numbers:
        result = "True"
    else:
        result = "False"    
    return result

# Kiểm tra hàm với giá trị N = 7
n = 7
assert check_the_number(n) == "False"

# Kiểm tra hàm với giá trị N = 2 và in kết quả
n = 2
result = check_the_number(n)
print(result)
