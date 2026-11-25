# python-inheritance

Inheritance in Python: `dir()`, subclasses, `isinstance()`, `issubclass()`,
method overriding, `super()` and raising exceptions.

## Files

| File | Description |
| --- | --- |
| `0-lookup.py` | Function that returns the attributes and methods of an object |
| `1-my_list.py` | `MyList`, a `list` that can print itself sorted |
| `2-is_same_class.py` | Is the object exactly an instance of a class? |
| `3-is_kind_of_class.py` | Is the object an instance of a class or of a subclass? |
| `4-inherits_from.py` | Is the object an instance of a strict subclass? |
| `5-base_geometry.py` | Empty class `BaseGeometry` |
| `6-base_geometry.py` | `BaseGeometry` with an unimplemented `area()` |
| `7-base_geometry.py` | Adds `integer_validator()` |
| `8-rectangle.py` | `Rectangle` with private, validated `width` and `height` |
| `9-rectangle.py` | `Rectangle` with `area()` and a description |
| `10-square.py` | `Square` inheriting from `Rectangle` |
| `11-square.py` | `Square` with its own description |
| `tests/` | Doctest files for tasks 1 and 7 |

## Tests

```
python3 -m doctest -v ./tests/1-my_list.txt
python3 -m doctest -v ./tests/7-base_geometry.txt
```
