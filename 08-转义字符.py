
# 在Python中，print()， 默认⾃带 end="\n" 这个换⾏结束符，所以导致每两个 print 直接会换⾏展示，⽤户可以按需求更改结束符。
print('输出的内容')
# 这一行跟下一行一样的意思
print('输出的内容', end='\n') # \n可以换成任意的符号，这样的话，任意两句话之间就会用这个符号隔开，例子如下

print('输出的内容', end='。。。')
print('输出的内容', end='\n')

print('输出的内容2', end='\t')
print('输出的内容')


print('\n\n输出的内容1\n输出的内容\n\t输出的内容3')
