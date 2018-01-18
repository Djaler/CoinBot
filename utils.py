from typing import Union
from numbers import Number


def format_thousands(number: Union[Number, str], sep: str = ',') -> str:
    """Formats a number with a specified thousands separator"""
    return f'{number:_}'.replace('_', sep)
