#coding:utf-8

import cPickle

class Pinyin():
    def __init__(self):
        f = file('./tools/zzlib/pinyin/pinyin.dat')
        self.dict = cPickle.load(f)
        f.close()

    def pinyin(self, chars, capital=True, splitter=''):
        ''' 取得字符串的拼音
        @params: chars 需要转换的中文字符串
        @params: splitter 字符拼音之间的分隔符，缺省为不分隔
        @retuns: 使用分隔符链接起来的拼音字符串，不能转换的汉字将原样返回
        '''
        result = []
        for char in chars:
            key = "%X" % ord(char)
            try:
                py = self.dict[key].split("\t")[0].split(" ")[0].strip()[:-1]
                if capital:
                    result.append(py.capitalize())
                else:
                    result.append(py)
            except:
                result.append(char)
        return splitter.join(result)

    def zimu(self, chars, upper=True, splitter=''):
        ''' 取得字符串各字符拼音的首个字母
        @params: chars 需要转换的中文字符串
        @params: splitter 字符拼音首位字母之间的分隔符，缺省为不分隔
        @retuns: 使用分隔符链接起来的拼音字符串，不能转换的汉字将半角的“?”代替
        '''
        result = []
        for char in chars:
            key = "%X" % ord(char)
            try:
                py = self.dict[key].split("\t")[0].split(" ")[0].strip()[:-1]
                if upper:
                    result.append(py[:1].upper())
                else:
                    result.append(py[:1])
            except:
                result.append('?')
        return splitter.join(result)

    def wb(self, char, splitter=','):
        ''' 取得一个汉字的五笔写法
        @params char 需查询的汉字（单字）
        @params splitter 如果一个汉字有多种输入方案，则在各方案之间使用的分隔符，缺省为半角逗号
        @returns 返回一个字符串，包含一个或多个输入方案，查询不到则返回原字符
        '''
        key = "%X" % ord(char)
        try:
            result = self.dict[key].split("\t")[1].strip()
            result = splitter.join(result.split(" "))
        except:
            result = char
        return result

if __name__ == "__main__":
    p = Pinyin()
    print p.pinyin(u"钓鱼岛是中国的")
    print p.zimu(u'灭了小日本')
    print p.wb(u"国")
