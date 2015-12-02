# _*_ coding: utf-8 _*_

import os
   

def genSummary(path, i, pathofSummary):
   i += 1
   contains = os.listdir(path)
   putFiletoHead(contains)
   for c in contains:
      p = path
      if ((not os.path.isdir(p + '/' + c)) and (not c.endswith('.md'))) or c == 'SUMMARY.md':
         continue
      elif c.endswith('.md'):
         if c == 'README.md':
            f.write(' ' * 3 * (i - 1) + '*' + '[' + os.path.split(p)[-1] + ']' + '(' + relativeDir(p, i - 1, c)+ ')\n')
         else:
            f.write(' ' * 3 * i + '*' + '[' + c[0:-3] + ']' + '(' + relativeDir(p, i - 1, c) + ')\n')
      else:
         p = p + '/' + c
         genSummary(p, i, pathofSummary)

# 将文件放到 List 的最前面

def putFiletoHead(dirList):
   dirList.sort()
   j = 0
   for d in dirList:
      if d.endswith('.md'):
         dIndex = dirList.index(d)
         if d ==  'README.md':
            dirList[0], dirList[dIndex] = d, dirList[0]
            j += 1
            break
         dirList[j], dirList[dIndex] = d, dirList[j]
         j += 1
   
# 取文件的相对路径
def relativeDir(path, i, file):
   j = -i
   if i == 0:
      return file
   nonfile = '/'.join(path.split('/')[j:])
   return nonfile + '/' + file

# 判断一个文件是否是目录：使用 os.path.isdir(path)
#path = '/home/helen/workspace/EayunOS-testcase/Function_Test/WebAdmin'

path = '/home/helen/workspace/EayunOS-testcase/EayunOS 4.2 New Feature'
pathofSummary = '/home/helen/workspace/EayunOS-testcase/EayunOS 4.2 New Feature/SUMMARY.md'
f = open(pathofSummary, 'a')
genSummary(path, 0, pathofSummary)
f.close()
