class CSVServiceError(Exception):
    pass


class CSVServiceHTTPError(CSVServiceError):
    pass


class CSVServiceInvalidData(CSVServiceError):
    pass
