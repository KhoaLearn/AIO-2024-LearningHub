def levenshtein_distance(token1, token2):
    # Khởi tạo ma trận các số 0
    dp = [[0 for _ in range(len(token2) + 1)] for _ in range(len(token1) + 1)]
    
    # Khởi tạo cột đầu tiên và hàng đầu tiên của ma trận
    for i in range(len(token1) + 1):
        dp[i][0] = i
    for j in range(len(token2) + 1):
        dp[0][j] = j

    # Điền giá trị vào ma trận
    for i in range(1, len(token1) + 1):
        for j in range(1, len(token2) + 1):
            if token1[i - 1] == token2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j] + 1,    # Xóa
                               dp[i][j - 1] + 1,    # Chèn
                               dp[i - 1][j - 1] + 1) # Thay thế

    # Ô cuối cùng của ma trận là khoảng cách Levenshtein
    distance = dp[-1][-1]
    return distance

# Kiểm tra hàm
assert levenshtein_distance("hi", "hello") == 4
print(levenshtein_distance("hola", "hello"))
