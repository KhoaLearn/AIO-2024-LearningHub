import math
def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True

class ActivationFunction:
    def __init__(self, alpha=0.01):
        self.alpha = alpha
    def sigmoid(self, x):
        return 1 / (1 + math.exp(-x))
    def relu(self, x):
        return max(0, x)
    def elu(self, x):
        return x if x > 0 else self.alpha * (math.exp(x) - 1)
    def calculate_activation_function(self, x, acti_func):
        acti_func = acti_func.lower()
        if acti_func == 'sigmoid':
            return self.sigmoid(x)
        elif acti_func == 'relu':
            return self.relu(x)
        elif acti_func == 'elu':
            return self.elu(x)
        else:
            return None
def exercise2():
    x = input('Input x = ')
    if not is_number(x):
        print('x must be a number')
        return
    x = float(x)
    acti_func = input('Input activation function (sigmoid|relu|elu): ')
    acti_lst = ['sigmoid', 'relu', 'elu']
    if acti_func.lower() not in acti_lst:
        print(f'{acti_func} is not supported')
        return
    af = ActivationFunction()
    result = af.calculate_activation_function(x, acti_func)
    print(f'{acti_func.lower()}: f({x}) = {result}')
