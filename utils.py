from typing import Union


def format_thousands(number: Union[int, float, str], sep: str = ',') -> str:
    """Formats a number with a specified thousands separator"""
    if isinstance(number, str):
        number = float(number) if '.' in number else int(number)
    return f'{number:_}'.replace('_', sep)
