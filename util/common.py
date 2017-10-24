# _*_ coding:utf-8 _*_

def arg_named(request, arg_name, default=None):
    """return named arg in request

    the type of arg depends on the type of default value.
    """
    try:
        argument = request.args.get(arg_name)[0]
        if default is None:
            return argument
        elif isinstance(default, int):
            return int(argument)
        elif isinstance(default, float):
            return float(argument)
    except:
        return default