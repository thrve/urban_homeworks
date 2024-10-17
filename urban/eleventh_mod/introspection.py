#!/usr/bin/env python


class MyClass:
    def __init__(self, value):
        self.value = value

    def display_value(self):
        return f'The value is: {self.value}'


def introspection_info(obj):
    obj_type = type(obj).__name__
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith('__')]
    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith('__')]
    module = getattr(obj, '__module__', None)
    info = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': module,
    }

    return info


my_object = MyClass(42)


object_info = introspection_info(my_object)
print(object_info)
