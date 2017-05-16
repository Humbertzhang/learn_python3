'''
任一个英文的纯文本文件，统计其中的单词出现的个数。
1,文件read:
file = open('filepath','模式') ,　模式包括r,w等
read 得到的为一个str对象
2,文件分割:content.split()
  得到一个list对象
3,友好输出　使用print来输出map很难看
　from pprint import pprint 之后，pprint(wordmap)较美观
'''
from pprint import pprint

def countwords(docpath):
	f = open("%s"%(docpath),'r')
	content = f.read()
	wordlist = [word for word in (content.split())]
	wordmap = dict()
	for word in wordlist:
		if word in wordmap:
			wordmap[word] +=1
		else:
			wordmap[word] = 1
	pprint(wordmap) 

if __name__ == '__main__':
	path = input("Input the path:")
	countwords(path)
