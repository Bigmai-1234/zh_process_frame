# zh_process_frame
编写一个中文预处理的框架。

- clean.py 定义中文数据的清洗模式
- cut.py  定义篇章句子切分和词切分的方法
- pkg_ipt.py 根据不同的文本处理要求，调用不同的处理包。


"""
jieba[github.com/Bigmai-1234/zh_process_frame/blob/master/zh_process_frame_git/lan_proc_pkgs/jieba/jieba.md]
========
基本功能：
1. 分词,并行分词,词性标注
2. 添加自定义词典
3. 关键词提取
4. Tokenize：返回词语在原文的起止位置
5. ChineseAnalyzer for Whoosh 搜索引擎
6. 命令行分词

------------------------------------------------
# FoolNLTK中文处理工具包[github.com/Bigmai-1234/zh_process_frame/blob/master/zh_process_frame_git/lan_proc_pkgs/fool/FoolNLTK.md]
=========
1. 分词，词性标注
2. 实体识别
3. 用户自定义词典
4. 可训练自己的模型
5. 批量处理

------------------------------------------------
# pkuseg：[github.com/Bigmai-1234/zh_process_frame/blob/master/zh_process_frame_git/lan_proc_pkgs/pkuseg/pkuseg.md]
==========
支持细分领域分词

------------------------------------------------
# pyhanlp: Python interfaces for HanLP[github.com/Bigmai-1234/zh_process_frame/blob/master/zh_process_frame_git/lan_proc_pkgs/pyhanlp/pyhanlp.md]
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
pyltp：Python interfaces for LTP[github.com/Bigmai-1234/zh_process_frame/blob/master/zh_process_frame_git/lan_proc_pkgs/pyltp/pyltp.md]
==========
分句
分词
词性标注
命名实体识别
依存句法分析
语义角色标注

------------------------------------------------

# SnowNLP: Simplified Chinese Text Processing[github.com/Bigmai-1234/zh_process_frame/blob/master/zh_process_frame_git/lan_proc_pkgs/snownlp/snownlp.md]
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
# THULAC：一个高效的中文词法分析工具包[github.com/Bigmai-1234/zh_process_frame/blob/master/zh_process_frame_git/lan_proc_pkgs/thulac/thulac.md]
中文分词
词性标注
"""
