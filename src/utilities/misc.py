def singleton(singleton):
    """
    Decorator which is used to create singletons
    """
    __instances_dict = {}

    def wrapper(*args, **kwargs):
        if not __instances_dict.get(singleton):
            singleton_obj = singleton()
            __instances_dict[singleton] = singleton_obj
        return __instances_dict[singleton]

    return wrapper
