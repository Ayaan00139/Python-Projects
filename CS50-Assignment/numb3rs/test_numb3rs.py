from numb3rs import validate

def test_valid_ips():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("140.247.235.144") == True
    assert validate("0.0.0.0") == True

def test_invalid_ips():
    assert validate("256.255.255.255") == False
    assert validate("64.128.256.512") == False
    assert validate("8.8.8") == False
    assert validate("10.10.10.10.10") == False
    assert validate("cat") == False
    assert validate("000.001.010.100") == False
