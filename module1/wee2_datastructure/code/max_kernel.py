def max_kernel(num_list, k):
    # Danh sách kết quả để lưu các giá trị lớn nhất
    result = []

    # Duyệt qua danh sách số với khoảng cách k
    for i in range(len(num_list) - k + 1):
        # Lấy k phần tử liên tiếp từ vị trí i
        window = num_list[i:i + k]
        # Tìm giá trị lớn nhất trong khoảng k phần tử
        max_value = max(window)
        # Thêm giá trị lớn nhất vào danh sách kết quả
        result.append(max_value)

    return result

# Kiểm tra chức năng với một trường hợp kiểm thử
assert max_kernel([3, 4, 5, 1, -44], 3) == [5, 5, 5]

# Khởi tạo danh sách số và giá trị k
num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3

# In ra kết quả của hàm max_kernel
print(max_kernel(num_list, k))
