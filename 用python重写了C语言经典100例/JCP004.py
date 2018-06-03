'''【程序3】
题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
1.程序分析：在10万以内判断，先将该数加上100后再开方，再将该数加上268后再开方，如果开方后
　　　　　　的结果满足如下条件，即是结果。请看具体分析：
2.程序源代码：

#include "math.h"
main()
{
long int i,x,y,z;
for (i=1;i<100000;i++)
　{ x=sqrt(i+100); 　　/*x为加上100后开方后的结果*/
　　y=sqrt(i+268); 　　/*y为再加上168后开方后的结果*/
　　　if(x*x==i+100&&y*y==i+268)/*如果一个数的平方根的平方等于该数，这说明此数是完全平方数*/
　　　　printf("\n%ld\n",i);
　}
}
'''
year = int(raw_input('year:\n'))
month = int(raw_input('month:\n'))
day = int(raw_input('day:\n'))

months = (0,31,59,90,120,151,181,212,243,273,304,334)
if 0 <= month <= 12:
    sum = months[month - 1]
else:
    print 'data error'
sum += day
leap = 0
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    leap = 1
if (leap == 1) and (month > 2):
    sum += 1
print 'it is the %dth day.' % sum

