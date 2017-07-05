from rest_framework.response import Response
from six import text_type


def exception_handler(exc, context):

    data = {
        'message': text_type(exc),
        'errors': getattr(exc, 'errors', []),
        'code': getattr(exc, 'code', ''),
        'error_code': getattr(exc, 'error_code', ''),
    }

    return Response(data, status=exc.status_code)
