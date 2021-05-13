import requests
from string import ascii_uppercase as alphabet
from pandas import read_csv
from io import StringIO

class Spreadsheet(object):

    def __init__(self, url, id_, sheets=None, columns=None, format_='out:csv'):
        self.url = url
        self.id_ = id_
        self.format_ = format_
        self.sheets = sheets
        self.columns = {
            column: letter for column, letter in zip(columns, alphabet)
        } if columns else {}

    @property
    def urlsheet(self):
        return f'{self.url}/{self.id_}/gviz/tq'

    def query(self, sheet='', range_='', query='', header=0, converters=None):
        for key, value in self.columns.items():
            query = query.replace(key, value)
        params = {}
        params['tqx'] = self.format_
        if self.sheets and sheet:
            params['gid'] = self.sheets[sheet]
        params['tq'] = query
        params['range'] = range_
        response = requests.get(self.urlsheet, params=params)
        response.raise_for_status()
        dataframe = read_csv(
            StringIO(response.text),
            names=self.columns.keys(),
            header=header,
            converters=converters,
            keep_default_na=False,
        )
        return dataframe

