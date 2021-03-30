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

## [max](https://github.com/PatYoung/Python/tree/master/max)描述:

详见内部README。附上python2转python3的文件，使用方法如下
```
python 2to3.py -w max.py
```
-w表示转换后的写入到max.py中，并产生一个有.bak后缀的原文件。详见[这里](https://docs.python.org/zh-cn/3/library/2to3.html)。
