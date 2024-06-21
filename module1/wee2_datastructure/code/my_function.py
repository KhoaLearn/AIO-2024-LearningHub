def my_function(data, max_value, min_value):
    """
    Thay thế các giá trị trong data dựa trên giá trị min_value và max_value.
    """
    result = []
    for i in data:
        # Nếu i < min_value thì thêm min_value vào result
        if i < min_value:
            result.append(min_value)
        # Nếu i > max_value thì thêm max_value vào result
        elif i > max_value:
            result.append(max_value)
        # Nếu không, thêm i vào result
        else:
            result.append(i)
    return result
# Dữ liệu đầu vào và giá trị min_value, max_value
my_list = [5, 2, 5, 0, 1]
max_value = 1
min_value = 0
assert my_function(data=my_list, max_value=max_value, min_value=min_value) == [1, 1, 1, 0, 1]
my_list = [10, 2, 5, 0, 1]
max_value = 2
min_value = 1
print(my_function(data=my_list, max_value=max_value, min_value=min_value))