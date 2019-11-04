"""
jieba
========
基本功能：
1. 分词,并行分词,词性标注
2. 添加自定义词典
3. 关键词提取
4. Tokenize：返回词语在原文的起止位置
5. ChineseAnalyzer for Whoosh 搜索引擎
6. 命令行分词

------------------------------------------------
# FoolNLTK
中文处理工具包
=========
1. 分词，词性标注
2. 实体识别
3. 用户自定义词典
4. 可训练自己的模型
5. 批量处理

------------------------------------------------
# pkuseg：
==========
支持细分领域分词

------------------------------------------------
# pyhanlp: Python interfaces for HanLP
========
- 分词
- 自定义词典
- 极速词典分词
- 索引分词
- CRF分词
- 感知机词法分析
- 臺灣正體、香港繁體
- 关键词提取、自动摘要
- 文本分类、情感分析


------------------------------------------------
pyltp：Python interfaces for LTP
==========
分句
分词
词性标注
命名实体识别
依存句法分析
语义角色标注


------------------------------------------------

# SnowNLP: Simplified Chinese Text Processing
==============
* 中文分词
* 词性标注
* 情感分析
* 文本分类（Naive Bayes）
* 转换成拼音（Trie树实现的最大匹配）
* 繁体转简体（Trie树实现的最大匹配）
* 提取文本关键词
* 提取文本摘要
* tf，idf
* Tokenization（分割成句子）
* 文本相似


------------------------------------------------
# THULAC：一个高效的中文词法分析工具包
中文分词
词性标注
"""


#######################定义文本处理使用的包##################################

def pkg_impt(flag,*path):
    flag = str(flag).lower()
    if flag in ["jieba","snownlp","pkuseg","thulac","pyhanlp","fool","pyltp","stanfordcorenlp"]:
        if flag == "jieba":
            import jieba
        elif flag == "snownlp":
            from snownlp import SnowNLP
        elif flag == "pkuseg":
            import pkuseg
            seg = pkuseg.pkuseg(postag=path[0])  # 以默认配置加载模型
            return seg

        elif flag == "thulac":
            import thulac
        elif flag == "pyhanlp":
            from pyhanlp import HanLP
        elif flag == "fool":
            import fool
        elif flag == "pyltp":
            if not isinstance(path[0], str):
                raise ValueError('Unknown type %r' % type(path[0]))
            elif path[0] == "Parser":
                import os
                from pyltp import Parser
                par_model_path = os.path.join(path[1], 'parser.model')
                parser = Parser()  # 初始化实例
                parser.load(par_model_path)  # 加载模型
                return parser


        elif flag == "stanfordcorenlp":
            from stanfordcorenlp import StanfordCoreNLP
            nlp = StanfordCoreNLP(path[0], lang="zh")
            return nlp



    else:
        print("请选择适合python的语言包！")
    return None


