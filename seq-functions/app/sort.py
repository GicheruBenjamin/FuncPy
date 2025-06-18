
from typing import List, Callable

def sort_ascending(list: List , func: Callable) -> List:
    return list.sort(func)

def sort_descending(list: List , func: Callable) -> List:
    return list.sort(func, reverse=True)