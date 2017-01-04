import os


def remove_str(
        input_str: str,
        remove_str_list=['\n', '\"', '\'', ' ']: list
) ->str:
    if not remove_str_list:
        return input_str
    else:
        self.remove_str(
            self,
            input_str.replace(remove_str_list[0], ""),
            remove_str_list[1:]
        )


def type_return(string: str)->type:
    if string.isdigit() and string[0] != 0:
        return int
    elif string.replace(',' '', 1).isdigit():
        return float
    else:
        return str


def header2dict(input_name: str) -> dict:
    _, ext = os.path.splitext(input_name)
    if ext == "csv":
        separator = ","
    elif ext == "tsv":
        separator = "\t"

    with open(input_name) as f:
        key_arr = f.readline()
        example = f.readline()

    return {remove(key): type_return(remove(value))
            for key, value in zip(key_arr, example)}
