import logging

from Main.QualityMeasurementException import ExceptionQuantityMeasurement

logging.basicConfig(filename='new_measurement_system.log', level=logging.DEBUG,
                    format=' %(asctime)s| %(name)s |%(message)s  |%(levelname)s ')


class QuantityMeasurementSystem():
    GRAMS_TO_KILOGRAM = .001
    GRAMS_TO_MILLIGRAM = 1000
    METER_TO_CENTIMETER = 100
    METER_TO_KILOMETER = 1000

    def temperature_celsius_to_fareheit(self, input_temperature):
        '''

        :param input_temperature: input shoud be entered by user
        :return: this method will convert temperature celcius
                    into farenheit
        '''

        try:
            fahrenheit_temperature = round(((1.8 * input_temperature) + 32), 2)
            logging.debug("fahrenheit is {}".format(fahrenheit_temperature))
            return fahrenheit_temperature
        except TypeError:
            logging.exception("Exception Occured due to invalid input")
            raise ExceptionQuantityMeasurement("Provide valid number input")


    def temperature_farenheit_to_celsius(self, input_temperature):
        '''

               :param input_temperature: input shoud be entered by user
               :return: this method will convert temperature freheit
                           into celcius
               '''

        try:
            celsius_temperature = round(((input_temperature - 32) * 0.56), 3)
            logging.debug("celsius is {}".format(celsius_temperature))
            return celsius_temperature
        except TypeError:
            logging.exception("Exception Occured due to invalid input")
            raise ExceptionQuantityMeasurement("Provide valid number input")


    def weight_grams_to_kilograms_conversion(self, input_weight):
        '''

               :param input_temperature: input shoud be entered by user
               :return: this method will convert Weight Gram
                           into kilogran
               '''

        try:
            kilo_gram_weight = round((input_weight * self.GRAMS_TO_KILOGRAM), 3)
            logging.debug("kilogram is {}".format(kilo_gram_weight))
            return kilo_gram_weight
        except TypeError:
            logging.exception("Exception Occured due to invalid input")
            raise ExceptionQuantityMeasurement("Provide valid number input")


    def weight_grams_to_milligrams_conversion(self, input_weight):
        '''

               :param input_temperature: input shoud be entered by user
               :return: this method will convert weight Gram
                           into milligram
               '''

        try:
            milli_gram_weight = round((input_weight *  self.GRAMS_TO_MILLIGRAM), 3)
            logging.debug("milliGram is {}".format(milli_gram_weight))
            return milli_gram_weight
        except TypeError:
            logging.exception("Exception Occured due to invalid input")
            raise ExceptionQuantityMeasurement("Provide valid number input")



    def length_meter_to_centimeter_conversion(self, input_length):
        '''

               :param input_temperature: input should be entered by user
               :return: this method will convert length meter
                           into centimeter
               '''

        try:
            centi_meter_length = round((input_length * self.METER_TO_CENTIMETER), 3)
            logging.debug("centimeter is {}".format(centi_meter_length))
            return centi_meter_length
        except TypeError:
            logging.exception("Exception Occured due to invalid input")
            raise ExceptionQuantityMeasurement("Provide valid number input")


    def length_meter_to_kilometer_conversion(self, input_length):
        '''

               :param input_temperature: input shoud be entered by user
               :return: this method will convert lenght meter
                           into kilometer
               '''

        try:
            kilo_meter_length = round((input_length / self.METER_TO_KILOMETER), 3)
            logging.debug("kilometer is {}".format(kilo_meter_length))
            return kilo_meter_length
        except TypeError:
            logging.exception("Exception Occured due to invalid input")
            raise ExceptionQuantityMeasurement("Provide valid number input")