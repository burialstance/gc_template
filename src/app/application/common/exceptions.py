class AppException(Exception):
    details: str = 'error'

    def __str__(self):
        return '{}(details="{}")'.format(self.__class__.__name__, self.details)

    def __repr__(self):
        return self.__str__()

