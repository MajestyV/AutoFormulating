# AutoFormulating
用于计算各种溶液的配方

## `AutoFormulating.Ink.GetSoluteMass()`函数
此函数用于计算固定溶剂体系下，要配制不同质量百分浓度的墨水所需的溶质的质量。

输入为`[溶质1的质量百分浓度,溶质2的质量百分浓度, ......]`，默认的单位是*wt%* （eg. 如果溶质1的质量百分浓度为5 wt%，溶质2为10 wt%，溶质3为73%，则输入为`[5.0, 10.0, 73.0]`）。

此函数的原理为：

假设我们的墨水体系有$[1,2,3,......,N]$这$N$种溶质，以及$[1,2,3,......,M]$这$M$种溶剂组成。那么墨水的总质量可以写为

$$ m_{tot} = {\sum_{i}^{N}}{m_{i}^{solute}}+{\sum_{j}^{M}}{m_{j}^{solvent}} = {\sum_{i}^{N}}{m_{i}^{solute}}+m_{tot}^{solvent} $$

根据质量百分浓度的定义，对于溶质$i$，有${\omega_{i}^{solute}} = \frac{m_{i}^{solute}}{m_{tot}}$，那么我们就可以得到下列方程组

![微信截图_20210407200946](https://user-images.githubusercontent.com/53797732/113864241-3f453980-97dd-11eb-9227-ba17abd54427.png)

把上面的方程组写成向量形式，则有

![微信截图_20210407200605](https://user-images.githubusercontent.com/53797732/113863875-c80fa580-97dc-11eb-9051-0c150a56a6d5.png)

为了方便运算，我们可以设

![微信截图_20210407200752](https://user-images.githubusercontent.com/53797732/113864017-f8574400-97dc-11eb-994a-1f99a0bb232b.png)

同时设一个N维向量$\hat{\sigma} = [1, 1, 1, \cdots, 1]^{T}$，那么我们可以得到以下关系

$$ {\sum_{i}^{N}}{m_{i}^{solute}} = \hat{M}^{T}·\hat{\sigma} = \hat{\sigma}^{T}·\hat{M} $$

我们就可以把之前的向量方程化简为

$$ \hat{M} = \hat{\Omega}·\hat{\sigma}^{T}·\hat{M}+\hat{\Omega}·m_{tot}^{solvent} \Longrightarrow (\hat{1}-\hat{\Omega}·\hat{\sigma}^{T})·\hat{M} = \hat{\Omega}·m_{tot}^{solvent}$$

只需解上述方程即可解出每个溶剂所需添加的质量。

同时，应注意$\hat{1}-\hat{\Omega}·\hat{\sigma}^{T}$是一个$N\times{N}$的矩阵，其值为

![微信截图_20210407200627](https://user-images.githubusercontent.com/53797732/113864046-03aa6f80-97dd-11eb-8625-14bf01172fa9.png)
