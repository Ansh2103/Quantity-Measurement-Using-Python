import pytest

@pytest.mark.parametrize("input, output", [(32, 89.6), (33, 91.4)])
def test_temperature_celsius_to_farenheit(input, output, instance_of_main_class):
    result = instance_of_main_class.temperature_celsius_to_fareheit(input)
    assert result == output


@pytest.mark.parametrize("input, output", [(33, 0.56), (337, 170.8)])
def test_temperature_farenheit_to_celsius(input, output, instance_of_main_class):
    result = instance_of_main_class.temperature_farenheit_to_celsius(input)
    assert result == output


@pytest.mark.parametrize("input, output", [(12, 12 / 1000 ), (7, 7 /1000), (3, 3 / 1000)])
def test_length_meter_to_kilometer(input, output, instance_of_main_class):
    result = instance_of_main_class.length_meter_to_kilometer_conversion(input)
    assert result == output


@pytest.mark.parametrize("input, output", [(12, 12 * 100), (7, 7 * 100), (3, 3 * 100)])
def test_length_meter_to_centimeter(input, output, instance_of_main_class):
    result = instance_of_main_class.length_meter_to_centimeter_conversion(input)
    assert result == output



@pytest.mark.parametrize("input, output", [(3, 3000), (7, 7000),])
def test_weight_grams_to_milligrams(input, output, instance_of_main_class):
    result = instance_of_main_class.weight_grams_to_milligrams_conversion(input)
    assert result == output

@pytest.mark.parametrize("input, output", [(3000, 3), (7000, 7)])
def test_weight_grams_to_kilograms(input, output, instance_of_main_class):
    result = instance_of_main_class.weight_grams_to_kilograms_conversion(input)
    assert result == output


