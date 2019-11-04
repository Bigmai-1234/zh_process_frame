
#定义中文数据清洗模式

"""
:param s: 中文句子
:return:清洗后的句子
"""

def cleanSentence(s):
### 匹配除了数字、英文标点、中文标点、中文字符、中文字符之外符号

    import re
    from string import digits, punctuation
    rule = re.compile(u'[^a-zA-Z.,;《》？！“”‘’@#￥%…&×（）——+【】{};；●，。&～、|\s:：' + digits + punctuation + '\u4e00-\u9fa5]+')
    s = re.sub(rule, '', s)
    ###
    """
    其他清洗规则
    
    """

    return s