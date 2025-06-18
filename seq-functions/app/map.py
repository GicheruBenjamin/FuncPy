
from typing import List, Callable

def change_state_thru_list(list: List , func: Callable) -> List:
    return list.map(func)