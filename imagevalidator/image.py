import imghdr
import os

from io import BytesIO
from urllib.request import urlopen
from validators import url, ValidationFailure, validator


def _image_url(path):
    _result = False

    try:
        if url(path):
            response = urlopen(path)
            data = BytesIO(response.read())
            if imghdr.what(data) is not None:
                _result = True
            else:
                _result = False
    except ValidationFailure:
        _result = False

    return _result


def _image_file(path):
    _result = False

    if os.path.exists(path):
        if imghdr.what(path) is not None:
            _result = True
        else:
            _result = False

    return _result


@validator
def image(path):
    """
    Return whether or not a file is a valid image type.
    If the file is a valid image type this function returns ``True``, otherwise
    :class:`~validators.utils.ValidationFailure`.
    :param path: The path to the file to evaluate.
    """

    _result = False

    if _image_url(path):
        _result = True
    elif _image_file(path):
        _result = True
    else:
        _result = False

    return _result
