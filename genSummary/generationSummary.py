# _*_ coding: utf-8 _*_

import os

def genSummary(path, i, pathofSummary):
   i += 1
   contains = os.listdir(path)
   if 'README.md' not in contains:
      newFile = file((path + '/' + 'README.md'), 'w')
      newFile.close()
   contains = putFiletoHead(contains, path)
   for c in contains:
      p = path
      if ((not os.path.isdir(p + '/' + c)) and (not c.endswith('.md'))) or c == 'SUMMARY.md' or c == '_book' or c == '.git':
         continue
      elif c.endswith('.md'):
         if c == 'README.md':
            f.write(' ' * 3 * (i - 1) + '* ' + '[' + os.path.split(p)[-1] + ']' + '(' + relativeDir(p, i - 1, c)+ ')\n')
         else:
            f.write(' ' * 3 * i + '* ' + '[' + c[0:-3] + ']' + '(' + relativeDir(p, i - 1, c) + ')\n')
      else:
         p = p + '/' + c
         genSummary(p, i, pathofSummary)

# 将文件放到 List 的最前面，README.md 放在第一个位置

def putFiletoHead(dirList, path):
#   print '-----------------------' + path
   dirList.sort()
   # orderList(dirList, 'README.md', 0)
   # newDirList = dirList[1:]
   fileList = []
   nonfileList = []
   for content in dirList:
      if os.path.isdir(path + '/' + content):
         nonfileList.append(content)
      else:
         fileList.append(content)
#   print '~~~~~~~~~~~~~~~~~~~~~'
#   print fileList
#   print '==================='
   orderList(fileList, 'README.md', 0)
   dirList = fileList + nonfileList
   return dirList


   
# 取文件的相对路径
def relativeDir(path, i, file):
   j = -i
   if i == 0:
      return file
   nonfile = '/'.join(path.split('/')[j:])
   return nonfile + '/' + file

# 判断一个文件是否是目录：使用 os.path.isdir(path)
#path = '/home/helen/workspace/EayunOS-testcase/Function_Test/WebAdmin'
# python 冒泡排序
def orderList(dirList, d, n):
   """
   d 是要交换的那个 value
   n 是目的索引
   """
   l = len(dirList)
   dIndex = dirList.index(d)
   i = dIndex
   while i > n:
      dirList[i], dirList[i - 1] = dirList[i - 1], dirList[i]
      i -= 1



def main():
   path = os.getcwd()
   pathofSummary = os.getcwd() + '/' + 'SUMMARY.md'
   global f
   f = open(pathofSummary, 'a')
   genSummary(path, 0, pathofSummary)
   f.close()

if __name__ == '__main__':
   main()
