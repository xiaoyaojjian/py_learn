#-*-coding:utf-8-*-
#-*-coding:utf-8-*-
__author__ = 'zlxs'
'''
day 4: Handler API and Error
json API definition
'''
import json
import logging
import inspect
import functools


class APIError(Exception):

    """docstring for APIError"""
    """
	The base APIError which contains error(required),data(optional) and message(optional).
	"""

    def __init__(self, error, data="", message=""):
        super(APIError, self).__init__(message)
        self.error = error
        self.data = data
        self.message = message


class APIValueError(APIError):

    """docstring for APIValueError"""
    """
	Indicate the input value has error or invalid.The data specifies the error field of input form.
	"""

    def __init__(self, field,message=""):
        super(APIValueError, self).__init__('value:invalid', field, message)


class APIResoureNotError(APIError):

    """docstring for APIResoureNotError"""
    """
	Indicate the resoure was not found.The data specifies the resoure name.
	"""

    def __init__(self, field, message=""):
        super(APIResoureNotError, self).__init__(
            'value:not found', field, message)


class APIPermissionError(APIError):

    """docstring for APIPermissionError"""
    """
	Indicate the api has no permession.
	"""

    def __init__(self, message=""):
        super(APIPermissionError, self).__init__(
            'permession:forbidden', 'permession', message)
        self.arg = arg
