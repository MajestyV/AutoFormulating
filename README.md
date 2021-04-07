# AutoFormulating
用于计算各种溶液的配方

## `AutoFormulating.Ink.GetSoluteMass()`函数
此函数用于计算固定溶剂体系下，要配制不同质量百分浓度的墨水所需的溶质的质量。

输入为`[溶质1的质量百分浓度,溶质2的质量百分浓度, ......]`，默认的单位是*wt%* （eg. 如果溶质1的质量百分浓度为5 wt%，溶质2为10 wt%，溶质3为73%，则输入为`[5.0, 10.0, 73.0]`）。

此函数的原理为：

假设我们的墨水体系有$[1,2,3,......,N]$这$N$种溶质，以及$[1,2,3,......,M]$这$M$种溶剂组成。那么墨水的总质量可以写为

$$ m_{tot} = {\sum_{i}^{N}}{m_{i}^{solute}}+{\sum_{j}^{M}}{m_{j}^{solvent}} = {\sum_{i}^{N}}{m_{i}^{solute}}+m_{tot}^{solvent} $$

根据质量百分浓度的定义，对于溶质$i$，有${\omega_{i}^{solute}} = \frac{m_{i}^{solute}}{m_{tot}}$，那么我们就可以得到下列方程组

$$\begin{cases}
m_{1}^{solute} = {\omega_{1}^{solute}}({\sum_{i}^{N}}{m_{i}^{solute}}+m_{tot}^{solvent}) \\
m_{2}^{solute} = {\omega_{2}^{solute}}({\sum_{i}^{N}}{m_{i}^{solute}}+m_{tot}^{solvent}) \\
\vdots \\
m_{N}^{solute} = {\omega_{N}^{solute}}({\sum_{i}^{N}}{m_{i}^{solute}}+m_{tot}^{solvent})
\end{cases}
$$

$$
\left \{ 
\begin{array}{c}
m_{1}^{solute} = {\omega_{1}^{solute}}({\sum_{i}^{N}}{m_{i}^{solute}}+m_{tot}^{solvent}) \\
m_{2}^{solute} = {\omega_{2}^{solute}}({\sum_{i}^{N}}{m_{i}^{solute}}+m_{tot}^{solvent}) \\
\vdots \\
m_{N}^{solute} = {\omega_{N}^{solute}}({\sum_{i}^{N}}{m_{i}^{solute}}+m_{tot}^{solvent})
\end{array}
\right. 
$$
