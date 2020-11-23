import csv
import codecs
import requests

from Utils.custom_csv_error import CSVServiceError, CSVServiceHTTPError, CSVServiceEmptyDataError


class CSVService:

    def get_csv_data(self, url):
        response = self._get_url_response(url)
        csv_data = self._get_csv_content(response)
        return csv_data

    def _get_url_response(self, url):
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            return response
        else:
            raise CSVServiceHTTPError(f"CSVService Error: Invalid url provided HTTP error - {response.status_code}")

    def _get_csv_content(self, response):
        content = []
        wrapper = csv.reader(codecs.iterdecode(response.iter_lines(), 'utf-8'), delimiter=',')
        for record in wrapper:
            content.append(record)

        self._validate_data(content)
        return content

    def _validate_data(self, data):
        if len(data) < 1:
            raise CSVServiceEmptyDataError(f"CSVService Error: CSV content is empty, please check csv url")
