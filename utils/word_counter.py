def empty_remover(lst):
    temp = lst.copy()
    for ele in lst:
        if ele == '':
            temp.remove(ele)

    return temp


def ten_column_spliter(lst):
    wrapper = []
    temp = []
    for ele in lst:
        temp.append(ele)
        if len(temp) == 10:
            wrapper.append(temp.copy())
            temp.clear()
    if any(wrapper):
        return wrapper
    else:
        return temp


def str_formatter(s: str):
    ss = s.replace('\n', ' ').replace('\r', ' ')
    lst = ss.split(' ')
    return lst
