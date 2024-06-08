import random
import math

def mae(y_true, y_pred):
    return sum(abs(y_t - y_p) for y_t, y_p in zip(y_true, y_pred)) / len(y_true)

def mse(y_true, y_pred):
    return sum((y_t - y_p) ** 2 for y_t, y_p in zip(y_true, y_pred)) / len(y_true)

def rmse(y_true, y_pred):
    return math.sqrt(mse(y_true, y_pred))

def calculate_loss():
    num_samples = input('Number of samples which are generated: ')
    if not num_samples.isnumeric() or int(num_samples) <= 0:
        print('Number of samples must be a positive integer')
        return
    loss_name = input('Loss function (mae|mse|rmse): ').lower()
    supported_funcs = {'mae': mae, 'mse': mse, 'rmse': rmse}
    if loss_name not in supported_funcs.keys():
        print(f'{loss_name} is not supported')
        return
    log = f'Loss name: {loss_name}, '
    y_true, y_predict = [], []
    for i in range(int(num_samples)):
        pred = random.uniform(0.0, 10.0)
        target = random.uniform(0.0, 10.0)
        y_true.append(target)
        y_predict.append(pred)
        print(f'Loss name: {loss_name}, sample: {i}, pred: {pred}, true: {target}, loss: {supported_funcs[loss_name]([target], [pred])}')
    loss = supported_funcs[loss_name](y_true, y_predict)
    print(f'final {loss_name} = {loss}')
