def my_function(data, max, min):
    result = []
    for i in data:
        # Nếu i < min thì thêm min vào result
        if i < min:
            result.append(min)
        # Nếu i > max thì thêm max vào result
        elif i > max:
            result.append(max)
        # Nếu không, thêm i vào result
        else:
            result.append(i)
    return result

# Dữ liệu đầu vào và giá trị min, max
my_list = [5, 2, 5, 0, 1]
max = 1
min = 0
assert my_function(data=my_list, max=max, min=min) == [1, 1, 1, 0, 1]

my_list = [10, 2, 5, 0, 1]
max = 2
min = 1
print(my_function(data=my_list, max=max, min=min))
