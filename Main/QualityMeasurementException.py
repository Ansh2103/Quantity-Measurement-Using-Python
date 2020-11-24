
class ExceptionQuantityMeasurement(Exception):
    '''
    custum Exception declared
    '''
    def __init__(self,message):
        '''
        declared __init__ method to provide message
        :param message: the message will pass to the constructor;
                    for that we have to declare super method
        '''
        super().__init__(message)
        ''''''