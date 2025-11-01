# Shell

Shell 脚本（shell script），是一种为 shell 编写的脚本程序

业界所说的 shell 通常都是指 shell 脚本，但读者朋友要知道，shell 和 shell script 是两个不同的概念

由于习惯的原因，简洁起见，本文出现的 "shell编程" 都是指 shell 脚本编程，不是指开发 shell 自身

---

#! 告诉系统其后路径所指定的程序即是解释此脚本文件的 Shell 程序

### 运行 Shell 脚本有两种方法：

1、作为可执行程序
将上面的代码保存为 test.sh，并 cd 到相应目录：

```
chmod +x ./test.sh  #使脚本具有执行权限
./test.sh  #执行脚本
```
2、作为解释器参数

这种运行方式是，直接运行解释器，其参数就是 shell 脚本的文件名，如：
```
/bin/sh test.sh
/bin/php test.php
```
这种方式运行的脚本，不需要在第一行指定解释器信息，写了也没用。

### Shell 变量

定义变量时，变量名不加美元符号（$，PHP语言中变量需要）

#### **变量名和等号之间不能有空格，这可能和你熟悉的所有编程语言都不一样**

使用大写字母表示常量： 习惯上，常量的变量名通常使用大写字母，例如 PI=3.14

除了显式地直接赋值，还可以用语句给变量赋值，如：

```
for file in `ls /etc`
或
for file in $(ls /etc)
```

### 使用变量

使用一个定义过的变量，只要在变量名前面加美元符号即可，如：

```
your_name="qinjx"
echo $your_name
echo ${your_name}
```

变量名外面的花括号是可选的，加不加都行，加花括号是为了帮助解释器识别变量的边界，比如下面这种情况：

```
for skill in Ada Coffe Action Java; do
    echo "I am good at ${skill}Script"
done
```

如果不给skill变量加花括号，写成echo "I am good at $skillScript"，解释器就会把$skillScript当成一个变量（其值为空），代码执行结果就不是我们期望的样子了。

#### **推荐给所有变量加上花括号，这是个好的编程习惯**
#### **使用变量的时候才加美元符（$）**

在 Shell中，变量通常被视为字符串。

你可以使用单引号 ' 或双引号 " 来定义字符串，例如：

```
my_string='Hello, World!'

或者

my_string="Hello, World!"
```

### 环境变量
这些是由操作系统或用户设置的特殊变量，用于配置 Shell 的行为和影响其执行环境。

例如，PATH 变量包含了操作系统搜索可执行文件的路径：
```
echo $PATH
```

#### 特殊变量
有一些特殊变量在 Shell 中具有特殊含义，例如 $0 表示脚本的名称，$1, $2, 等表示脚本的参数。

`$#`表示传递给脚本的参数数量，`$? `表示上一个命令的退出状态等。

双引号的优点：

**双引号里可以有变量**
双引号里可以出现转义字符

```
your_name="runoob"
# 使用双引号拼接
greeting="hello, "$your_name" !"
greeting_1="hello, ${your_name} !"
echo $greeting  $greeting_1

# 使用单引号拼接
greeting_2='hello, '$your_name' !'
greeting_3='hello, ${your_name} !'
echo $greeting_2  $greeting_3
```

#### 建议携程 双引号拼接 的第二种

### 数组

使用 @ 符号可以获取数组中的所有元素，例如：

```
echo ${array_name[@]}
```

获取数组的长度
获取数组长度的方法与获取字符串长度的方法相同，例如：

```
# 取得数组元素的个数
length=${#array_name[@]}
# 或者
length=${#array_name[*]}
# 取得数组单个元素的长度
length=${#array_name[n]}
```

### 获取数组中的所有元素

使用 @ 或 * 可以获取数组中的所有元素，例如

```
#!/bin/bash
# author:菜鸟教程
# url:www.runoob.com

my_array[0]=A
my_array[1]=B
my_array[2]=C
my_array[3]=D

echo "数组的元素为: ${my_array[*]}"
echo "数组的元素为: ${my_array[@]}"
```

获取值：echo "数组的元素为: ${site[*]}"
获取键：echo "数组的键为: ${!site[@]}"
这里面*和@都可以使用

### 注释

以 # 开头的行就是注释，会被解释器忽略

### 多行注释

```
:<<EOF
注释内容...
注释内容...
注释内容...
EOF
```

以上例子中，: 是一个空命令，用于执行后面的 Here 文档，<<'EOF' 表示开启 Here 文档，COMMENT 是 Here 文档的标识符，在这两个标识符之间的内容都会被视为注释，不会被执行。
EOF 也可以使用其他符号:

```
: <<'COMMENT'
这是注释的部分。
可以有多行内容。
COMMENT

:<<'
注释内容...
注释内容...
注释内容...
'

:<<!
注释内容...
注释内容...
注释内容...
!
```

我们也可以使用了冒号 : 命令，并用单引号 ' 将多行内容括起来。由于冒号是一个空命令，这些内容不会被执行。

格式为：: + 空格 + 单引号。

```
: '
这是注释的部分。
可以有多行内容。
'
```

### 传递参数

我们可以在执行 Shell 脚本时，向脚本传递参数，脚本内获取参数的格式为 `$n`，n 代表一个数字，1 为执行脚本的第一个参数，2 为执行脚本的第二个参数。

例如可以使用 `$1、$2 `等来引用传递给脚本的参数，其中 `$1` 表示第一个参数，`$2` 表示第二个参数，依此类推。

`$*`：以一个单字符串显示所有向脚本传递的参数。
如`"$*"`用「"」括起来的情况、以`"$1 $2 … $n"`的形式输出所有参数。

`$@`：与`$*`相同，但是使用时加引号，并在引号中返回每个参数。
如`"$@"`用「"」括起来的情况、以`"$1" "$2" … "$n"` 的形式输出所有参数。

```
#!/bin/bash
# author:菜鸟教程
# url:www.runoob.com

echo "-- \$* 演示 ---"
for i in "$*"; do
    echo $i
done

echo "-- \$@ 演示 ---"
for i in "$@"; do
    echo $i
done
```

```
$ chmod +x test.sh 
$ ./test.sh 1 2 3
-- $* 演示 ---
1 2 3
-- $@ 演示 ---
1
2
3

```

### 运算符

原生bash不支持简单的数学运算，但是可以通过其他命令来实现，例如 awk 和 expr，expr 最常用。

例如，两个数相加(注意使用的是反引号 ` 而不是单引号 ')：

```
#!/bin/bash

val=`expr 2 + 2`
echo "两数之和为 : $val"
```

#### 表达式和运算符之间要有空格，例如 2+2 是不对的，必须写成 2 + 2，这与我们熟悉的大多数编程语言不一样

#### 完整的表达式要被 ` ` 包含，注意这个字符不是常用的单引号，在 Esc 键下边

#### 注意：条件表达式要放在方括号之间，并且要有空格，例如: [$a==$b] 是错误的，必须写成 [ $a == $b ]

```
#!/bin/bash
# author:菜鸟教程
# url:www.runoob.com

a=10
b=20

val=`expr $a + $b`
echo "a + b : $val"

val=`expr $a - $b`
echo "a - b : $val"

val=`expr $a \* $b`
echo "a * b : $val"

val=`expr $b / $a`
echo "b / a : $val"

val=`expr $b % $a`
echo "b % a : $val"

if [ $a == $b ]
then
   echo "a 等于 b"
fi
if [ $a != $b ]
then
   echo "a 不等于 b"
fi
```

#### 乘号(*)前边必须加反斜杠(\)才能实现乘法运算

#### if...then...fi 是条件语句，后续将会讲解

#### 在 MAC 中 shell 的 expr 语法是：$((表达式))，此处表达式中的 "*" 不需要转义符号 "\" 

### 文件测试运算符

文件测试运算符用于检测 Unix 文件的各种属性

### 使用 $(( )) 进行算术运算

使用 `$(( ))` 进行算术运算
`$(( )) `语法也是进行算术运算的一种方式。

```
#!/bin/bash

# 初始化变量
num=5

# 自增
num=$((num + 1))

# 自减
num=$((num - 1))

echo $num
```

### echo

-n 选项：不换行输出

默认情况下，echo 会在输出后添加换行符。使用 -n 可以禁止这种行为：

```
echo -n "Loading..."
echo " Done!"
```

-e 选项：启用转义字符解释
启用对反斜杠转义的解释：
```
echo -e "First line\nSecond line"
```

### echo高级用法

1. 输出到文件

使用重定向将输出保存到文件：

```
echo "This will be saved to file" > output.txt
```

追加内容到文件：

```
echo "Additional line" >> output.txt
```

2. 彩色输出

使用 ANSI 转义码实现彩色文本：

```
echo -e "\033[31mRed Text\033[0m"
echo -e "\033[42;31mGreen Background with Red Text\033[0m"
```

3. 输出命令执行结果

使用命令替换输出命令结果：

```
echo "Today is $(date)"
```

### 实际应用示例

1. 创建简单菜单
实例
```
echo -e "\n\033[1mSystem Menu\033[0m"
echo "1. Check disk space"
echo "2. List running processes"
echo "3. Show system info"
echo -n "Please enter your choice [1-3]: "
```

2. 进度条模拟
实例
```
echo -n "Progress: ["
for i in {1..20}; do
    echo -n "#"
    sleep 0.1
done
echo "] Done!"
```

3. 生成配置文件
实例
```
cat <<EOF | sudo tee /etc/myapp.conf
# Generated by script on $(date)
[Database]
host = localhost
port = 3306
user = appuser
password = secret123
EOF
```

### 注意事项

1、引号的重要性

2、特殊字符处理：

```
echo "Cost: \$100"  # 输出 $ 符号
echo "Path: /usr/local/bin"  # 斜杠不需要转义
```

#### 总结要点
基本语法 echo [选项] [字符串]
常用选项 -n 不换行，-e 启用转义
变量输出 使用 $变量名，用双引号包裹
输出重定向 > 覆盖文件，>> 追加到文件

### printf 命令的语法：

```
printf  format-string  [arguments...]
```

参数说明：

- format-string：包含普通字符和格式说明符的字符串
- arguments...：与格式说明符对应的变量或值


实践示例

```
# 简单字符串输出
printf "Hello, World!\n"

# 带变量的输出
name="Alice"
printf "Hello, %s\n" "$name"
```

执行与输出：

```
$ bash script.sh
Hello, World!
Hello, Alice
```

#### 格式化控制

```
# 字段宽度和对齐
printf "|%10s|\n|%-10s|\n" "right" "left"

# 数字前导零
printf "Year: %04d\n" 23

# 浮点数精度
printf "Pi: %.2f\n" 3.14159
```

### if else

```
if condition
then
    command1 
    command2
    ...
    commandN 
fi

```
末尾的 fi 就是 if 倒过来拼写，后面还会遇到类似的

### if else-if else

```
if condition1
then
    command1
elif condition2 
then 
    command2
else
    commandN
fi

```

if else 的 [...] 判断语句中大于使用 -gt，小于使用 -lt

```
if [ "$a" -gt "$b" ]; then
    ...
fi
```

如果使用 ((...)) 作为判断语句，大于和小于可以直接使用 > 和 <。

```
if (( a > b )); then
    ...
fi
```

### for循环

for循环一般格式为：
```
for var in item1 item2 ... itemN
do
    command1
    command2
    ...
    commandN
done

```

写成一行：

```
for var in item1 item2 ... itemN; do command1; command2… done;
```

### while语句

while 循环用于不断执行一系列命令，也用于从输入文件中读取数据。其语法格式为：

```
while condition
do
    command
done
```

### until 循环

```
until condition
do
    command
done
```

### case ... esac

case ... esac 为多选择语句，与其他语言中的 switch ... case 语句类似，是一种多分支选择结构，每个 case 分支用右圆括号开始，用两个分号 ;; 表示 break，即执行结束，跳出整个 case ... esac 语句，esac（就是 case 反过来）作为结束标记。

可以用 case 语句匹配一个值与一个模式，如果匹配成功，执行相匹配的命令。
case ... esac 语法格式如下：
```
case 值 in
模式1)
    command1
    command2
    ...
    commandN
    ;;
模式2)
    command1
    command2
    ...
    commandN
    ;;
esac

```
case 工作方式如上所示，取值后面必须为单词 in，每一模式必须以右括号结束。取值可以为变量或常数，匹配发现取值符合某一模式后，其间所有命令开始执行直至 ;;

### Shell 函数
函数返回值在调用该函数后通过 `$? `来获得

### Shell 输入/输出重定向

| 命令 | 说明 |
| --- | --- |
| command > file | 将输出重定向到 file |
| command < file | 将输入重定向到 file |
| command >> file | 将输出以追加的方式重定向到 file |
| n > file | 将文件描述符为 n 的文件重定向到 file |
| n >> file | 将文件描述符为 n 的文件以追加的方式重定向到 file |
| n >& m | 将输出文件 m 和 n 合并 |
| n <& m | 将输入文件 m 和 n 合并 |
| << tag | 将开始标记 tag 和结束标记 tag 之间的内容作为输入 |

### 输出重定向
重定向一般通过在命令间插入特定的符号来实现。特别的，这些符号的语法如下所示:

```
command1 > file1
```

实例

执行下面的 who 命令，它将命令的完整的输出重定向在用户文件中(users):

```
$ who > users
```

执行后，并没有在终端输出信息，这是因为输出已被从默认的标准输出设备（终端）重定向到指定的文件。

你可以使用 cat 命令查看文件内容：

```
$ cat users
_mbsetupuser console  Oct 31 17:35 
tianqixin    console  Oct 31 17:35 
tianqixin    ttys000  Dec  1 11:33 
```

输出重定向会覆盖文件内容，请看下面的例子：


```
$ echo "菜鸟教程：www.runoob.com" > users
$ cat users
菜鸟教程：www.runoob.com
$
```

如果不希望文件内容被覆盖，可以使用 >> 追加到文件末尾，例如：

```
$ echo "菜鸟教程：www.runoob.com" >> users
$ cat users
菜鸟教程：www.runoob.com
菜鸟教程：www.runoob.com
$
```

### 输入重定向
和输出重定向一样，Unix 命令也可以从文件获取输入，语法为：
```
command1 < file1
```

这样，本来需要从键盘获取输入的命令会转移到文件读取内容。

注意：输出重定向是大于号(>)，输入重定向是小于号(<)。

实例

接着以上实例，我们需要统计 users 文件的行数,执行以下命令：

```
$ wc -l users
       2 users
```

也可以将输入重定向到 users 文件：

```
$  wc -l < users
       2 
```

注意：上面两个例子的结果不同：第一个例子，会输出文件名；第二个不会，因为它仅仅知道从标准输入读取内容。

command1 < infile > outfile

同时替换输入和输出，执行command1，从文件infile读取内容，然后将输出写入到outfile中

2 表示标准错误文件(stderr)

如果希望将 stdout 和 stderr 合并后重定向到 file，可以这样写：

```
$ command > file 2>&1

或者

$ command >> file 2>&1
```

### Here Document

Here Document 是 Shell 中的一种特殊的重定向方式，用来将输入重定向到一个交互式 Shell 脚本或程序

说白了就是把当前脚本中写下的几行文本当成是它的输入文件

它的基本的形式如下：
```
command << delimiter
    document
delimiter
```
它的作用是将两个 delimiter 之间的内容(document) 作为输入传递给 command

注意：

- 结尾的delimiter 一定要顶格写，前面不能有任何字符，后面也不能有任何字符，包括空格和 tab 缩进
- 开始的delimiter前后的空格会被忽略掉

### /dev/null 文件

如果希望执行某个命令，但又不希望在屏幕上显示输出结果，那么可以将输出重定向到 /dev/null：

```
$ command > /dev/null

```

/dev/null 是一个特殊的文件，写入到它的内容都会被丢弃；如果尝试从该文件读取内容，那么什么也读不到。但是 /dev/null 文件非常有用，将命令的输出重定向到它，会起到"禁止输出"的效果。

如果希望屏蔽 stdout 和 stderr，可以这样写：

```
$ command > /dev/null 2>&1

```
- 注意：0 是标准输入（STDIN），1 是标准输出（STDOUT），2 是标准错误输出（STDERR）

- 这里的 2 和 > 之间不可以有空格，2> 是一体的时候才表示错误输出

- 这里的&1中的&是为了说明1不是普通文件，而是标准输出的那个文件

### Shell 文件包含

和其他语言一样，Shell 也可以包含外部脚本。这样可以很方便的封装一些公用的代码作为一个独立的文件。

Shell 文件包含的语法格式如下：

```
. filename   # 注意点号(.)和文件名中间有一空格

或

source filename
```

实例
创建两个 shell 脚本文件。

test1.sh 代码如下：

```
#!/bin/bash
# author:菜鸟教程
# url:www.runoob.com

url="http://www.runoob.com"

```

test2.sh 代码如下：

```
#!/bin/bash
# author:菜鸟教程
# url:www.runoob.com

#使用 . 号来引用test1.sh 文件
. ./test1.sh

# 或者使用以下包含文件代码
# source ./test1.sh

echo "菜鸟教程官网地址：$url"

```

接下来，我们为 test2.sh 添加可执行权限并执行：

```
$ chmod +x test2.sh 
$ ./test2.sh 
菜鸟教程官网地址：http://www.runoob.com
```

- 注：被包含的文件 test1.sh 不需要可执行权限。

. filename / source filename：在当前 Shell 环境中执行文件中的命令，修改会保留到父 Shell

./filename：创建一个新的子 Shell 来执行文件，修改不会保留到父 Shell

最常见的用途是： 在登录时加载配置文件（如 .bashrc, .profile）或在脚本中“导入”其他包含函数或变量定义的脚本