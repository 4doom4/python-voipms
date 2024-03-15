# coding=utf-8
"""
The Dids API endpoint search

Documentation: https://voip.ms/m/apidocs.php
"""
from voipms.baseapi import BaseApi


class DidsSearch(BaseApi):
    """
    Search for the Dids endpoint.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the endpoint
        """
        super(DidsSearch, self).__init__(*args, **kwargs)
        self.endpoint = 'dids'

    def dids_can(self, search_type, query, province=None):
        """
        Searches for Canadian DIDs by Province using a Search Criteria

        :param search_type: [Required] Type of search (Values: 'starts', 'contains', 'ends')
        :type search_type: :py:class:`str`
        :param query: [Required] Query for searching (Examples: 'JOHN', '555', '123ABC')
        :type query: :py:class:`str`

        :param province: Canadian Province (Values from dids.get_provinces)
        :type province: :py:class:`str`

        :returns: :py:class:`dict`
        """
        method = "searchDIDsCAN"

        if not isinstance(search_type, str):
            raise ValueError("Type of search needs to be a str (Values: 'starts', 'contains', 'ends')")

        if not isinstance(query, str):
            raise ValueError("Query for searching needs to be a str (Examples: 'JOHN', '555', '123ABC')")

        parameters = {
            "type": search_type,
            "query": query
        }

        if province:
            if not isinstance(province, str):
                raise ValueError("Canadian Province needs to be a str (Values from dids.get_provinces)")
            else:
                parameters["province"] = province

        return self._voipms_client._get(method, parameters)

    def dids_usa(self, search_type, query, state=None):
        """
        Searches for USA DIDs by State using a Search Criteria

        :param search_type: [Required] Type of search (Values: 'starts', 'contains', 'ends')
        :type search_type: :py:class:`str`
        :param query: [Required] Query for searching (Examples: 'JOHN', '555', '123ABC')
        :type query: :py:class:`str`

        :param state: Canadian Province (Values from dids.get_states)
        :type state: :py:class:`str`

        :returns: :py:class:`dict`
        """
        method = "searchDIDsUSA"

        if not isinstance(search_type, str):
            raise ValueError("Type of search needs to be a str (Values: 'starts', 'contains', 'ends')")

        if not isinstance(query, str):
            raise ValueError("Query for searching needs to be a str (Examples: 'JOHN', '555', '123ABC')")

        parameters = {
            "type": search_type,
            "query": query
        }

        if state:
            if not isinstance(state, str):
                raise ValueError("United States State needs to be a str (Values from dids.get_states)")
            else:
                parameters["state"] = state

        return self._voipms_client._get(method, parameters)

    def toll_free_can_us(self, search_type=None, query=None):
        """
        Searches for USA/Canada Toll Free Numbers using a Search Criteria

        - Shows all USA/Canada Toll Free Numbers available if no criteria is provided.

        :param search_type: Type of search (Values: 'starts', 'contains', 'ends')
        :type search_type: :py:class:`str`
        :param query: Query for searching (Examples: 'JOHN', '555', '123ABC')
        :type query: :py:class:`str`

        :returns: :py:class:`dict`
        """
        method = "searchTollFreeCanUS"

        parameters = {}

        if search_type:
            if not isinstance(search_type, str):
                raise ValueError("Type of search needs to be a str (Values: 'starts', 'contains', 'ends')")
            else:
                parameters["type"] = search_type

        if query:
            if not isinstance(query, str):
                raise ValueError("Query for searching needs to be a str (Examples: 'JOHN', '555', '123ABC')")
            else:
                parameters["query"] = query

        return self._voipms_client._get(method, parameters)

    def toll_free_usa(self, search_type=None, query=None):
        """
        Searches for USA Toll Free Numbers using a Search Criteria

        - Shows all USA Toll Free Numbers available if no criteria is provided.

        :param search_type: Type of search (Values: 'starts', 'contains', 'ends')
        :type search_type: :py:class:`str`
        :param query: Query for searching (Examples: 'JOHN', '555', '123ABC')
        :type query: :py:class:`str`

        :returns: :py:class:`dict`
        """
        method = "searchTollFreeUSA"

        parameters = {}

        if search_type:
            if not isinstance(search_type, str):
                raise ValueError("Type of search needs to be a str (Values: 'starts', 'contains', 'ends')")
            else:
                parameters["type"] = search_type

        if query:
            if not isinstance(query, str):
                raise ValueError("Query for searching needs to be a str (Examples: 'JOHN', '555', '123ABC')")
            else:
                parameters["query"] = query

        return self._voipms_client._get(method, parameters)

    def vanity(self, search_type, query):
        """
        Searches for USA DIDs by State using a Search Criteria

        :param search_type: [Required] Type of Vanity Number (Values: '8**', '800', '855', '866', '877', '888')
        :type search_type: :py:class:`str`
        :param query: [Required] Query for searching : 7 Chars (Examples: '***JHON', '**555**', '**HELLO')
        :type query: :py:class:`str`

        :returns: :py:class:`dict`
        """
        method = "searchVanity"

        if not isinstance(search_type, str):
            raise ValueError("Type of Vanity Number needs to be a str (Values: '8**', '800', '855', '866', '877', '888')")

        if not isinstance(query, str):
            raise ValueError("Query for searching : 7 Chars needs to be a str (Examples: '***JHON', '**555**', '**HELLO')")

        parameters = {
            "type": search_type,
            "query": query
        }

        return self._voipms_client._get(method, parameters)
