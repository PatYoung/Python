# Python Files

vscode Markdown 实时预览tex公式，需安装插件[Markdown+Math](https://marketplace.visualstudio.com/items?itemName=goessner.mdmath)。

测试直接在vscode中push。

## [collect_all](https://github.com/PatYoung/Python/tree/master/collect_all)计算如下描述:

### 描述

有*total_number*种牌，抽到每种的概率相同，从中挑选出*select_number*种想要的牌，计算抽$n$次牌，收集齐这*select_number*想要的牌的概率$P(T=n)$。 程序见[collect_all.py](https://github.com/PatYoung/Python/blob/master/collect_all/collect_all.py)，且有数值验证与特殊情况。

### 思路

第$n$次抽到牌需为*select_number*种中的一种，且不在前$n-1$次出现。同时前$n-1$次需抽到其他*select_number*$-1$种想要的牌。
这里令*total_number* $=N$，*select_number* $=m$。

假设$A_{i}$表示前$n-1$次为未抽到其余想要的$m-1$中的第$i$种牌。那么同时前$n-1$次需抽到其他$m-1$种想要的牌的概率应为：

$1-P(所有A_{i}的交集)$，利用容斥恒等式，且知，

$$P(A_{1}A_{2}...A_{k}) = (1-\frac{k}{N-1})^{n-1}$$

便可计算$P(T=n)$，即：

$$P(T=n) = P(最后一张在m中,且不出现在前(n-1)次)(1-P(所有A_{i}的交集))$$
$$=\frac{m}{N}(1-\frac{1}{N})^{n-1}\times\sum_{k=1}^{N-1}(-1)^{k+1}C_{m-1}^{k}\left((1-\frac{k}{N-1})^{n-1}\right)$$

### *特殊情况*

*select_number* $=$ *total_number*, 另有如下方法：

同上，令*total_number* $=$ *select_number* $=N$

假设$B_{i}$表示前$n$次为未抽到想要的$N$中的第$i$种牌。

那么$P(T>n)$为$P(所有B_{i}的交集)$，又有，

$$P(B_{1}B_{2}...B_{k}) = (1-\frac{k}{N})^{n}$$

利用容斥恒等式，则，

$$P(T>n) = \sum_{k=1}^{N-1}(-1)^{k+1}C_N^{k}(1-\frac{k}{N})^{n}$$

那么，

$$P(T=n) = P(T>n-1)-P(T>n)$$

上式的值与一般情况下$m=N$时相同，即需满足，

$$\sum_{k=1}^{N-1}(-1)^{k+1}C_N^{k}(1-\frac{k}{N})^{n-1}-\sum_{k=1}^{N-1}(-1)^{k+1}C_N^{k}(1-\frac{k}{N})^{n}=(1-\frac{1}{N})^{n-1}\times\sum_{k=1}^{N-1}(-1)^{k+1}C_{N-1}^{k}\left((1-\frac{k}{N-1})^{n-1}\right)$$

化简如下，即需满足，

$$(N-1)^{n-1}=\sum_{k=1}^{N-1}(-1)^{k+1}C_{N-1}^{k}\left((N-k-1)^{n-1}+k(N-k)^{n-2}\right)$$

对左式$k+1$时有，

$$(-1)^{k+1}C_{N-1}^{k+1}\left(-(N-k-2)^{n-1}-(k+1)(N-k-1)^{n-2}\right)$$

同时利用，

$$C_{N-1}^{k+1} = \frac{N-k-1}{k+1}C_{N-1}^{k}$$

则，

$$C_{N-1}^{k}(N-k-1)^{n-1} = C_{N-1}^{k+1}(k+1)(N-k-1)^{n-2}$$

上式大括号内第$k$个左侧的项与第$k+1$个右侧项抵消，即只剩$k=1$的右侧项与$k=N-1$的左侧项，上述需满足式成立。该特殊情况也数值验证与[1=2.py](https://github.com/PatYoung/Python/blob/master/collect_all/1=2.py)中。

## [2.5](https://github.com/PatYoung/Python/tree/master/2.5)描述:
有黑桃♠、红桃♥、梅花♣、方片♦四个种类的牌。随机抽一张，计算它与当前选中牌为相同花色的平均抽牌次数。
该次数应为：

$$\frac{1}{4}\times(1+2+3+4) = 2.5$$

## [max](https://github.com/PatYoung/Python/tree/master/max)计算描述如下:

包含easyGUI使用，见内部README。附上python2转python3的文件，使用方法如下
```
python 2to3.py -w max.py
```
-w表示转换后的写入到max.py中，并产生一个有.bak后缀的原文件。详见[这里](https://docs.python.org/zh-cn/3/library/2to3.html)。

### 描述
课程分为必修课与选修课。一门课程可由$(x,y)$表示。现有如下评分计算规则，将课程分为两部分A和B，必修课必须在A部分计算，而选修课可在A部分或B部分二选一计算。

另一组课程的成绩为$X=(x_1,x_2,\dots,x_n)$，其对应绩点为$Y=(y_1,y_2,\dots,y_n)$。那么

A部分评分有如下计算公式，

$$point_A=\frac{\sum_{i}^{n}x_i y_i}{\sum_{i}^{n}y_i}, \quad (X,Y) \quad in \quad \text{A} $$

即为A部分课程的加权平均。

B部分评分有如下计算公式，

$$point_B=0.002\sum_{i}^{n}x_i y_i, \quad (X,Y) \quad in \quad \text{B} $$

且，

$$point_tot=point_A+point_B$$

求，应将哪几门选修课加入A部分，从而使总评分最高，该最高分是多少。

### 思路

若选修课有$m$门，那么将这$m$选修课加入A部分共$2^{n}$种可能，穷举计算这$2^{n}$种可能的分数，比较给出最佳方案。

其中需要面对的是如何穷举，一种思路如下:

可以给出这$m$门选修课的所有排列组合，按元素个数分类。第一层循环为选出的元素个数$k$，第二层循环为包含该元素个数可能排列的个数$C_{m}^{k}$。第二层循环中即可计算选出的这$k$个放入A部分的总评分。这样也就包含了所有$2^{n}$中可能。

[1.py](https://github.com/PatYoung/Python/blob/master/max/1.py)给出了一个生成某一列表所有元素所有排列，且不考虑顺序的程序，即共$2^{n}$中，且包含原列表元素个数为$k$个的种类有$C_{m}^{k}$个。