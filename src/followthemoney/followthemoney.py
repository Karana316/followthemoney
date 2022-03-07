import os
import json
from urllib.parse import urlencode
import requests
import regex
import pandas as pd
from dotenv import load_dotenv
from .literals import *
load_dotenv()


class FTMGroupConflictError(Exception):
    pass


class FollowTheMoney:

    BASE_URL = 'https://api.followthemoney.org/?dt=1&{0}&APIKey={1}&mode=json&{2}'

    def __init__(self):
        self.key = os.getenv('APIKEY')
        self.filters = {}

    def _check_conflicts(self, grouping, conflict_type='grouping'):
        if conflict_type=='grouping':
            conflicts = GROUPING_CONFLICTS
        else:
            conflicts = FILTER_CONFLICTS

        # check to see if any grouping has listed conflicts, error if any conflicts are also included
        for group in grouping:
            if group in conflicts.keys():
                if any(map(lambda x: x in grouping, conflicts[group])):
                    raise FTMGroupConflictError(
                        f'{group} conflicts with another listed group. One of these: {conflicts[group]}')

    def _get_grouping(self, **kwargs):
        grouping = []

        for key in kwargs.keys():
            grouping += [GROUPS[key][g] for g in kwargs[key]]
        self._check_conflicts(grouping)
        return ','.join(grouping)

    def _url(self, groupings=None):
        if len(self.filters.keys()) > 0:
            filters = urlencode(self.filters)
        else:
            filters = ''

        if groupings:
            params = urlencode(groupings)
        elif groupings is None:
            params = ''
        return self.BASE_URL.format(filters, self.key, params)

    def _get(self, url):

        r = requests.get(url)

        pattern = regex.compile(r'\{"metaInfo.*\}')
        json_parsed = pattern.findall(r.content.decode('utf-8'))[0]
        data = json.loads(json_parsed)

        return data

    def get_entity(self, eid):

        url = self._url({'eid': eid})
        data = self._get(url)
        data = data['records']
        data = pd.json_normalize(data)

        return pd.DataFrame(data)

    def add_filters(self, **kwargs):
        tokens = {TOKENS[k]: v for k, v in kwargs.items()}
        combined = {**self.filters, **tokens}
        self._check_conflicts(combined.keys(), 'filter')
        self.filters = {**self.filters, **tokens}

    def get_data_by_groupings(self, **kwargs):
        if kwargs:
            groupings = {'gro': self._get_grouping(**kwargs)}
        else:
            groupings=None

        url = self._url(groupings)
        data = self._get(url)
        data = data['records']
        data = pd.json_normalize(data)

        return pd.DataFrame(data)
