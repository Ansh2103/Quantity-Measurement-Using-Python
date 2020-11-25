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

