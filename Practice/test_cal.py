from calculator import square

def test_square():
    num=[-5,-4,-3,0,1,5,4,"cat"]
    for i in num:
        assert square(i)==i*i
