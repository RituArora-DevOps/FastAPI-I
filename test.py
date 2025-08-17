from typing import Annotated, get_type_hints, get_origin, get_args

def double(x: Annotated[int, (0,100)]) -> int:
    type_hints = get_type_hints(double, include_extras=True)
    # if get_origin(hint) is Annotated
    print(type_hints)
    return x*2

result = double(4)
print(result)