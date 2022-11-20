def do_stuff(num):
    try:
        if num or isinstance(num, int):
            return int(num) + 5
        else:
            return "Input a number"
    except ValueError as err:
        return err
