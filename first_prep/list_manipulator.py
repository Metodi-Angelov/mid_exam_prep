def list_manipulator(some_list, parameter, parameter_two, *args):
    num_list = some_list.copy()
    if parameter == "add":
        if parameter_two == "beginning":
            for i in range(len(args) - 1, -1, -1):
                num_list.insert(0, args[i])

        elif parameter_two == "end":
            for arg in args:
                num_list.append(arg)

    elif parameter == "remove":
        if parameter_two == "beginning" and len(args) <= 0:
            num_list = num_list[1:]
        elif parameter_two == "end" and len(args) <= 0:
            num_list = num_list[:-1]

        if parameter_two == "beginning" and len(args) > 0:
            for arg in args:
                num_list = num_list[arg:]
        elif parameter_two == "end" and len(args) > 0:
            for arg in args:
                num_list = num_list[:-arg]

    return num_list