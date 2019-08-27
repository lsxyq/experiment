#!/usr/bin/env bash
awk '{print $1 $7}' access.log | tail -n 10 #获取日志最后十行

#awk 'BEGIN{ commands } pattern{ commands } END{ commands }'
#第一步：运行BEGIN{ commands }语句块中的语句。
#第二步：从文件或标准输入(stdin)读取一行。然后运行pattern{ commands }语句块，它逐行扫描文件，从第一行到最后一行反复这个过程。直到文件所有被读取完成。
#第三步：当读至输入流末尾时。运行END{ commands }语句块。

ls -lh | awk '{print $5}' #打印文件大小
#$0 当前记录（这个变量中存放着整个行的内容）
#$1~$n 当前记录的第n个字段，字段间由FS分隔
#FS 输入字段分隔符 默认是空格或Tab
#NF 当前记录中的字段个数，就是有多少列
#NR 已经读出的记录数，就是行号，从1开始，如果有多个文件话，这个值也是不断累加中。
#FNR 当前记录数，与NR不同的是，这个值会是各个文件自己的行号
#RS 输入的记录分隔符， 默认为换行符
#OFS 输出字段分隔符， 默认也是空格
#ORS 输出的记录分隔符，默认为换行符
#FILENAME 当前输入文件的名字

awk  -F ':'  '{printf("filename:%12s,linenumber:%s,columns:%s,linecontent:%s\n",FILENAME,NR,NF,$0)}' /etc/passwd
awk  -F ':'  '{printf("filename:%5s,linenumber:%s,columns:%s,linecontent:%s\n",FILENAME,NR,NF,$0)}' /etc/passwd


ls -l  *.py | awk '{sum+=$5} END {print sum}'


#if (expression) {
#    statement;
#    statement;
#    ... ...
#}
#
#if (expression) {
#    statement;
#} else {
#    statement2;
#}
#
#if (expression) {
#    statement1;
#} else if (expression1) {
#    statement2;
#} else {
#    statement3;
#}
#awk中的循环语句同样借鉴于C语言，支持while、do/while、for、break、continue，这些关键字的语义和C语言中的语义完全相同。


#[root@localhost cc]# cat test.txt
#a 00
#b 01
#c 00
#d 02
[root@localhost cc]# awk '{sum[$2]+=1}END{for(i in sum)print i"\t"sum[i]}' test.txt
#00 2
#01 1
#02 1


#shell中的管道|
#command 1 | command 2 #他的功能是把第一个命令command 1运行的结果作为command 2的输入传给command 2
#
#wc -l #统计行数
#
#uniq -c #在输出行前面加上每行在输入文件里出现的次数
#
#uniq -u #仅显示不反复的行
#
#sort -nr
#-n：按照数值的大小排序
#-r：以相反的顺序来排序
#-k：按照哪一列进行排序
#
#head -3 #取前三名