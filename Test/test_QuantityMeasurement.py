from Main.Quantity_Measurement import *
import pytest

@pytest.mark.parametrize('first_unit, first_value, second_unit,second_value,output',
                         [(Weights.kilo_gram, 30, Weights.gram, 30000, True), (Weights.tonne, 0.033, Weights.gram,
                                                                               33000, True)])
def testing_QuantityMeasurementBy_WeightConversion(first_unit, first_value, second_unit, second_value, output):
    first_weight = QuantityMeasurements(first_unit, first_value)
    second_weight = QuantityMeasurements(second_unit, second_value)
    assert first_weight.compare(second_weight) == output


@pytest.mark.parametrize('first_unit, first_value, second_unit,second_value,output',
                         [(Weights.kilo_gram, 20, Weights.gram, 20000, 40), (Weights.tonne, 20, Weights.kilo_gram,
                                                                             20000, 40000)])
def testing_QuantityMeasurementBy_AddingWeights(first_unit, first_value, second_unit,second_value, output):
    first_weight = QuantityMeasurements(first_unit, first_value)
    second_weight = QuantityMeasurements(second_unit, second_value)
    assert first_weight.add(second_weight) == output

@pytest.mark.parametrize('first_unit, first_value, second_unit,second_value,output',
                         [(Distance.inch, 5, Distance.cm, 15, False), (Distance.inch, 2, Distance.cm, 5, True),
                          (Distance.feet, 9, Distance.yard, 3, True), (Distance.feet, 2, Distance.inch, 24, True)])
def test_for_length_conversion(first_unit, first_value, second_unit, second_value, output):
    first_distance = QuantityMeasurements(first_unit, first_value)
    second_distance = QuantityMeasurements(second_unit, second_value)
    assert first_distance.compare(second_distance) == output


@pytest.mark.parametrize('first_unit, first_value, second_unit,second_value,output',
                         [(Distance.feet, 2, Distance.inch, 24, 48), (Distance.cm, 800, Distance.meter, 8, 635.2),
                          (Distance.inch, 24, Distance.feet, 2, 48),(Distance.cm, 800, Distance.meter, 8, 635.2)])
def test_for_adding_two_lengths(first_unit, first_value, second_unit, second_value, output):
    first_distance = QuantityMeasurements(first_unit, first_value)
    second_distance = QuantityMeasurements(second_unit, second_value)
    assert first_distance.add(second_distance) == output