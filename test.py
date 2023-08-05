import pytest 
def func(x):
    return x + 5
    
def test_method():
    assert func(3) == 8
def test_method1():
    assert func(7)>11
def test_method2():
    assert func(75) > 78
def avg(scores):
    assert(len(scores) >= 4 and sum(scores) > 80 )
    return sum(scores)/ len(scores)
scores2=[22,88,66,42,90]
print("Avg of Scores:",avg(scores2))
scores3=[33,66,88,60]
print("Avg Of Scores3",avg(scores3))

