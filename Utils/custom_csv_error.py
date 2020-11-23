class CSVServiceError(Exception):
    pass


class CSVServiceHTTPError(CSVServiceError):
    pass


class CSVServiceEmptyDataError(CSVServiceError):
    pass
