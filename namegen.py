from itertools import product
import re
# shenmu=['','y','w',
#         'b','p','m','f','d','t','n','l','g','k','h','j','q','x','zh','chi','sh','r','z','c','s']
# yunmu=['i','u','v',
#        'a','ia','ua',
#        'o','uo',
#        'e','ie','ve',
#        'ai','uai',
#        'ei',
#        'ao','iao',
#        'ou',
#        'an','ian','uan',
#        'en','in','un',
#        'ang','iang','uang',
#        'eng','ing',
#        'ong','iong']
firstnames=['jia', 'shu', 'dong', 'bei', 'guan', 'sheng', 'fen', 'cheng', 'guo', 'kang', 'yong', 'gu', 'chen', 'jie', 'an', 'chun', 'hua', 'pei', 'jin', 'ke', 'gang', 'qi', 'kai', 'bin', 'peng', 'di', 'zhen', 'quan', 'ji', 'xin', 'fu', 'ran', 'sen', 'zheng', 'zhi', 'mei', 'chu', 'ru', 'hu', 'jun', 'shi', 'man', 'min', 'rou', 'ying', 'ming', 'lun', 'xia', 'tang', 'ling', 'huo', 'ning', 'tai', 'xu', 'tian', 'yun', 'yi', 'qiang', 'hong', 'he', 'qun', 'deng', 'zhuo', 'xiu', 'gan', 'yao', 'lin', 'le', 'hai', 'de', 'si', 'you', 'nan', 'xue', 'bo', 'zhu', 'rui', 'li', 'yu', 'ting', 'teng', 'huai', 'tong', 'bing', 'xiong', 'dan', 'en', 'ci', 'yue', 'liang', 'xuan', 'yang', 'xi', 'juan', 'han', 'jing', 'chi', 'qing', 'kun', 'zi', 'zhe', 'fan', 'cai', 'rong', 'wei', 'cun', 'qiao', 'wen', 'heng', 'yin', 'lan', 'chang', 'qian', 'da', 'jue', 'tao', 'ze', 'wan', 'huang', 'jian', 'xian', 'zhou', 'zhong', 'long', 'feng', 'zhao', 'hao', 'yuan', 'ni', 'huan', 'xing', 'xun', 'jiang', 'xiang', 'bai', 'ping', 'shao', 'shen', 'yan']
lastnames=['ping', 'xu', 'dong', 'cui', 'cai', 'xiao', 'liang', 'jiang', 'deng', 'liao', 'wan', 'lin', 'su', 'lu', 'mao', 'yao', 'yi', 'bai', 'sun', 'zeng', 'fu', 'wei', 'li', 'shen', 'peng', 'jin', 'hao', 'shang', 'wang', 'tian', 'qiu', 'gao', 'cheng', 'zhong', 'xue', 'duan', 'yan', 'shao', 'gong', 'ding', 'liu', 'huang', 'wu', 'ma', 'hu', 'lai', 'xie', 'xiong', 'fang', 'yuan', 'kang', 'qin', 'wen', 'du', 'zheng', 'dai', 'wo', 'zhu', 'chang', 'zhang', 'tang', 'ren', 'zhen', 'guo', 'cao', 'fan', 'yin', 'qian', 'shi', 'pan', 'hou', 'long', 'dan', 'zhou', 'song', 'feng', 'lv', 'gu', 'chen', 'jia', 'yang', 'zou', 'xia', 'qiao', 'ceng', 'kong', 'yu', 'he', 'zhao', 'meng', 'ye', 'luo', 'tan', 'han']

words=[]

# with open('C:/spamname/words.txt','w') as f:
#     for s in shenmu:
#         for y in yunmu:
#             word=s+y
#             words.append(word)
#             # email=name+'@du.edu'
#             f.write(word+'\n')
# print(len(product(words, repeat=2)))
# [print() for l in lastnames for x in product(words, repeat=2)]
i=0
with open('C:/spamname/names.txt','w') as f:
    for l in lastnames:
        for x in product(firstnames, repeat=2):
            f.write(''.join(x) + '.' + l + '@du.edu \n')
            i+=1
            print(str(i)+''.join(x) + '.' + l + '@du.edu \n')
        for x in firstnames:
            f.write(''.join(x) + '.' + l + '@du.edu \n')
            i+=1
            print(str(i)+''.join(x) + '.' + l + '@du.edu \n')