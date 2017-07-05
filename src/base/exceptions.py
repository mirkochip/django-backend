from rest_framework import status
from rest_framework.exceptions import APIException


class MappedExceptionMixin(object):
    """
    Mixin to provide error mapping lookup behaviour.
    """
    code = None
    error_code = None
    errors = []
    status_code = None  # status.HTTP_400_BAD_REQUEST
    message = None
    detail = None
    mapping = None
    context = {}

    def __init__(self, message='', context=None, errors=None, error_code=None, *args, **kwargs):
        self.code = self.code or self.__class__.__name__
        self.error_code = error_code or self.error_code
        self.message = message or self.message
        self.errors = errors or self.errors

        if not self.status_code:
            self.status_code = status.HTTP_400_BAD_REQUEST

        if context:
            self.context = context

        if self.context and self.message:
            self.message = self.message.format(**self.context)


class HackatrainException(Exception):
    """
    This is for all hackatrain-related exceptions, both API and non-API
    """


class HackatrainAPIException(MappedExceptionMixin, APIException, HackatrainException):
    """
    All exceptions throwable by the api should inherit from this
    customized base class, NOT from the rest_framework APIException
    """

    def __str__(self):
        return self.message or ''


class InvalidInputException(HackatrainAPIException):
    code = 'INVALID_INPUT'
    message = 'Invalid input data'
