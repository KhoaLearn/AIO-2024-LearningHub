def check_the_number(N):
    list_of_numbers = []
    result = ""
    for i in range(1, 5):
        # Thêm i vào list_of_numbers
        list_of_numbers.append(i)
    
    if N in list_of_numbers:
        results = "True"
    else:
        results = "False"
    
    return results

# Kiểm tra hàm với giá trị N = 7
N = 7
assert check_the_number(N) == "False"

# Kiểm tra hàm với giá trị N = 2 và in kết quả
N = 2
results = check_the_number(N)
print(results)
