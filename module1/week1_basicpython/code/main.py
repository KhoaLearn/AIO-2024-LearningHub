from metrics import calculate_f1_score
from activation import exercise2
from loss import calculate_loss
from approximation import (
    approximate_sin, 
    approximate_cos, 
    approximate_sinh, 
    approximate_cosh
)
from mdnre import md_nre_single_sample

if __name__ == '__main__':
    # Q1
    print('Question 1: ')
    assert round(calculate_f1_score(tp=2, fp=3, fn=5), 2) == 0.33
    print(round(calculate_f1_score(tp=2, fp=3, fn=5), 2))
    print('-------------------')
    
    # Q2
    print('Question 2: ')
    exercise2()
    print('-------------------')
    
    # Q3
    print('Question 3: ')
    calculate_loss()
    print('-------------------')
    
    # Q4
    print('Question 4: ')
    print(approximate_sin(3.14, 10))
    print(approximate_cos(3.14, 10))
    print(approximate_sinh(3.14, 10))
    print(approximate_cosh(3.14, 10))
    print('-------------------')
    
    # Q5
    print('Question 5: ')
    print(md_nre_single_sample(100, 99.5, 2, 1))
    print(md_nre_single_sample(50, 49.5, 2, 1))
    print(md_nre_single_sample(20, 19.5, 2, 1))
    print(md_nre_single_sample(0.6, 0.1, 2, 1))
    print('-------------------')
