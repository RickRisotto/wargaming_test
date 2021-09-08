import os


def remove():
    """ func to get rid of redundant symbols"""

    with open('test_file.txt', 'r', encoding='utf-8') as destination:
        temp = destination.read()

        temp = temp.split()

        out = []
        allowed = 'abcdefghijklmnopqrstuvwxyz'
        for i in temp:
            if i[0] == "\\":
                temp.remove(i)
            elif i[0][0] == "{":
                temp.remove(i)
            for it in allowed:
                if i.startswith(it):
                    out.append(i)
        temp = out
        print(type(temp))
        return temp


def clear_write(item):
    """ writes clear text to txt file. Removes primary txt on writing"""

    with open('test_file__.txt', 'w', encoding='utf-8') as destination:
        for i in item:
            destination.write(str(i))
    os.remove("test_file.txt")
    result = count()
    return result


def file_handler(f):
    """ opens a txt and writes data provided to it"""

    clear_list = []
    with open('test_file.txt', 'w', encoding='utf-8') as destination:
        for chunk in f.chunks():
            destination.write(chunk.decode('utf-8'))
    clear_list.append(remove())
    result = clear_write(clear_list)
    return result


def idf(cont):
    """ creates the dict from counted words"""

    count_size = len(cont)
    for k, v in cont.items():
        cont[k] = [v, round((v / count_size), 4)]
    final_count = {k: v for k, v in sorted(cont.items(), key=lambda item: item[1][1], reverse=True)}
    return final_count


def to_pandas_df(dt):
    """ gets dataframe obj from dict and pass it to thml"""

    import pandas as pd
    df = {"word": pd.Series([i for i in dt.keys()]),
          "tf": pd.Series([i[0] for i in dt.values()]),
          "idf": pd.Series([i[1] for i in dt.values()]),
          }
    d_ = pd.DataFrame(df)
    d_ = d_.to_html()

    return d_


def count():
    """ removes the rest of symbols(if any) and counts words appeared in file"""

    from collections import Counter
    with open('test_file__.txt', 'r') as destination:
        temp = destination.read()
        temp = temp.strip('[].}//\\?! '' ')
        temp = temp.split(',')
        out = []
        for i in temp:
            out.append(i.strip("[].}//\\?! ' "))
        c = Counter(out)
        for c_ in c.copy():
            if c_ == '':
                del c[c_]
    res = idf(c)
    final = to_pandas_df(res)
    return final
