import pytest
from Main.Quantity_Measurement import QuantityMeasurementSystem

@pytest.fixture
def quantity_measurement_handler():
    '''
    created Object of Main.Quantitymeasurement class
    :return: it returns the object created 'quantity measurement system'
    '''
    quantity_measurement_system = QuantityMeasurementSystem()
    return quantity_measurement_system