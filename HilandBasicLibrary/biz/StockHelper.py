from hiland.data import StringHelper


def get_exchange_name(stock_code):
    exchange_name = "SZ"
    if stock_code.startswith("6"):
        exchange_name = "SH"

    if stock_code.startswith("9"):
        exchange_name = "SH"

    if stock_code.startswith("7"):
        exchange_name = "SH"

    return exchange_name


def get_standard_code(stock_code):
    is_standard = StringHelper.is_contains(stock_code, ".")
    if is_standard:
        return stock_code
    else:
        return stock_code + "." + get_exchange_name(stock_code)


if __name__ == '__main__':
    code = "002005"
    _exchange_name = get_exchange_name(code)
    print(_exchange_name)
    _standard_code = get_standard_code(code)
    print(_standard_code)

    code = "602005"
    _exchange_name = get_exchange_name(code)
    print(_exchange_name)
    _standard_code = get_standard_code(code)
    print(_standard_code)
