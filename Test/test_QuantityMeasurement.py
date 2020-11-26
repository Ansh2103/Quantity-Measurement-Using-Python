from Main.Quantity_Measurement import *
import pytest

@pytest.mark.parametrize('first_unit, first_value, second_unit,second_value,output',
                         [(Weights.GRAM, 30, Weights.MG, 30000, True), (Weights.KG, 0.033, Weights.MG,
                                                                               33000, True)])
def testing_QuantityMeasurementBy_WeightConversion(first_unit, first_value, second_unit, second_value, output):
    first_weight = QuantityMeasurements(first_unit, first_value)
    second_weight = QuantityMeasurements(second_unit, second_value)
    assert first_weight.compare(second_weight) == output

@pytest.mark.parametrize('first_unit, first_value, second_unit,second_value,output',
                         [(Weights.KG, 30, Weights.GRAM, 30000, True), (Weights.TONNE, 0.033, Weights.GRAM,
                                                                               33000, True)])
def testing_QuantityMeasurementBy_WeightConversion(first_unit, first_value, second_unit, second_value, output):
    first_weight = QuantityMeasurements(first_unit, first_value)
    second_weight = QuantityMeasurements(second_unit, second_value)
    assert first_weight.compare(second_weight) == output

@pytest.mark.parametrize('first_unit, first_value, second_unit,second_value,output',
                         [(Weights.KG, 20, Weights.GRAM, 20000, 40), (Weights.TONNE, 20, Weights.KG,
                                                                             20000, 40000)])
def testing_QuantityMeasurementBy_AddingWeights(first_unit, first_value, second_unit,second_value, output):
    first_weight = QuantityMeasurements(first_unit, first_value)
    second_weight = QuantityMeasurements(second_unit, second_value)
    assert first_weight.add(second_weight) == output

#Distance Unit testing is done with parameterize pytest

@pytest.mark.parametrize('first_unit, first_value, second_unit,second_value,output',
                         [(Distance.INCH, 5, Distance.CENTIMETER, 15, False), (Distance.INCH, 2, Distance.CENTIMETER, 5, True),
                          (Distance.FEET, 9, Distance.YARD, 3, True), (Distance.FEET, 2, Distance.INCH, 24, True)])
def test_for_length_conversion(first_unit, first_value, second_unit, second_value, output):
    first_distance = QuantityMeasurements(first_unit, first_value)
    second_distance = QuantityMeasurements(second_unit, second_value)
    assert first_distance.compare(second_distance) == output

@pytest.mark.parametrize('first_unit, first_value, second_unit,second_value,output',
                         [(Distance.FEET, 2, Distance.INCH, 24, 48), (Distance.CENTIMETER, 800, Distance.METER, 8, 635.2),
                          (Distance.INCH, 24, Distance.FEET, 2, 48),(Distance.CENTIMETER, 800, Distance.METER, 8, 635.2)])
def test_for_adding_two_lengths(first_unit, first_value, second_unit, second_value, output):
    first_distance = QuantityMeasurements(first_unit, first_value)
    second_distance = QuantityMeasurements(second_unit, second_value)
    assert first_distance.add(second_distance) == output


#Temperature Unit testing is done with parameterize pytest

@pytest.mark.parametrize('first_unit, first_value, second_unit,second_value,output',
                         [(Temperature.FAHRENHEIT, 80.6, Temperature.CELCIUS, 27, True)])
def test_for_temperature_conversion(first_unit, first_value, second_unit, second_value, output):
    first_temperature = QuantityMeasurements(first_unit, first_value)
    second_temperature = QuantityMeasurements(second_unit, second_value)
    assert first_temperature.compare(second_temperature) == output


@pytest.mark.parametrize('first_unit, first_value, second_unit,second_value,output',
                         [(Temperature.FAHRENHEIT, 185, Temperature.CELCIUS, 85, 370)])
def test_for_temperature_addition(first_unit, first_value, second_unit, second_value, output):
    first_temperature = QuantityMeasurements(first_unit, first_value)
    second_temperature = QuantityMeasurements(second_unit, second_value)
    assert first_temperature.add(second_temperature) == output