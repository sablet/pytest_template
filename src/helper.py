import os


def remove_str(input_str, remove_str_list=None):
    """
    :param input_str: str
    :param remove_str_list: str
    :rtype str
    """
    if remove_str_list is None:
        remove_str_list = ['\n', '\"', '\'', ' ']
    if not remove_str_list:
        return input_str
    else:
        return remove_str(
                input_str.replace(remove_str_list[0], ""),
                remove_str_list[1:]
            )


def type_return(checked_str):
    """
    :param checked_str: str
    :rtype: type
    """
    if checked_str.isdigit():
        if checked_str[0] == '0':
            return str
        else:
            return int
    else:
        if checked_str.replace('.', '', 1).isdigit():
            return float
        else:
            return str


def csv_header2dict(input_name):
    """
    :param input_name: str
    :rtype: dict
    """
    with open(input_name) as f:
        key_arr = f.readline()
        example = f.readline()

    return {
        remove_str(key): type_return(remove_str(value))
        for key, value in zip(
            key_arr.split(','),
            example.split(',')
        )}
