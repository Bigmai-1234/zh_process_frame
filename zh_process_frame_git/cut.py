#分句

import re
import clean
sentence_delimiters = ['?', '!', ';', '？', '！', '。', '；', '……', '…', '\n']


def as_text(v):
    if v is None:
        return None
    elif isinstance(v, bytes):
        return v.decode('utf-8', errors='ignore')
    elif isinstance(v, str):
        return v
    else:
        raise ValueError('Unknown type %r' % type(v))


def sent_cut(article,min_len=1,clean_flag = True):
    #将文本中的回车/换行替换成"。"
    article = re.sub("\n","。",article)
    article = re.sub("\t", "。", article)

    res = [as_text(article)]
    for sep in set(sentence_delimiters):
        article, res = res, []
        for seq in article:
            res += seq.split(sep)
    res = [s.strip() for s in res if len(s.strip()) > min_len]


    if clean_flag:
        res_ = []
        for sent in res:
            res_.append(clean.cleanSentence(sent))
        return res_


    return res

