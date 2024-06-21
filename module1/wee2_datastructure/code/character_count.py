def character_count(word):
    """
    Đếm số lần xuất hiện của từng ký tự trong từ.
    """
    # Khởi tạo một từ điển để lưu thống kê ký tự
    character_statistic = {}

    # Duyệt qua từng ký tự trong từ
    for char in word:
        if char in character_statistic:
            # Nếu ký tự đã tồn tại trong từ điển, tăng số đếm lên 1
            character_statistic[char] += 1
        else:
            # Nếu ký tự chưa tồn tại, khởi tạo số đếm là 1
            character_statistic[char] = 1

    return character_statistic

# Kiểm tra chức năng với một trường hợp kiểm thử
assert character_count("Baby") == {'B': 1, 'a': 1, 'b': 1, 'y': 1}

# In ra kết quả của hàm character_count
print(character_count('Khoadeptrai'))