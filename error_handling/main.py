while True:
    try:
        age = int(input("How old are you?: "))
        8 / age
        # raise ValueError("hey cut it out!!!")
    # handle exception
    # except ValueError as error:
    #     print(f"Please input a number!: {error}")
    #     continue
    except ZeroDivisionError as error:
        print(f"Please input number higher than 0: {error}")
        continue
    # General case
    except Exception as error:
        print(error)
        continue
    # if there is no exception do this
    else:
        print(age)
        break
    # run regardless at the end of anything
    finally:
        print('ok, i am finally done')
    print('can you hear me ?')

# from functools import reduce
#
#
# def sum(*args):
#     try:
#         1/0
#         return reduce(lambda total, num: total + num, args, 0)
#     except (TypeError, ZeroDivisionError) as err:
#         print(err)
#
# print(sum(1, 'haha'))
