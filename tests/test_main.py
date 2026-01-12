from scr.main import convert_tempreture

def test_conv_temp_func():
    assert convert_tempreture("Celsius", "Fahrenheit", 22) == 71.60
    assert convert_tempreture("Celsius", "Kelvin", 22) == 71.60
    assert convert_tempreture("Fahrenheit", "Celsius", 22) == -5.56
    assert convert_tempreture("Fahrenheit", "Kelvin", 22) == 267.59
    assert convert_tempreture("Kelvin", "Fahrenheit", 22) == -419.80
    assert convert_tempreture("Kelvin", "Celsius", 22) == -251.00

    assert convert_tempreture("Celsius", "Celsius", 22) == 22.00
    assert convert_tempreture("Fahrenheit", "Fahrenheit", 22) == 22.00
    assert convert_tempreture("Kelvin", "Kelvin", 22) == 22.00