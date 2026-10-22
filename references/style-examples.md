# Paired slide and spoken-supplement examples

Read these four short pairs before a first draft; revisit the relevant pair for a revision. These are self-contained style samples distilled from the validated longitudinal-data report. They teach explanation patterns, not a required topic, model, number of pages, or speaking voice for every study.

Adapt the reasoning to the new source and speaker role. Do not copy names, sample sizes, metrics, or findings into an unrelated report.

## 1. Motivation: from a concrete difficulty to the idea

### Slide content

**观测特征之外仍有共同的个体差异**

基线、收入和家庭规模解释了一部分购买差异。剩余差异仍可能在多个商品和多个时期反复出现。

家庭 i 的潜在特征 theta_i，通过各商品的系数 a_j，对应不同商品的购买倾向。同一个家庭在各期共用这组特征。

### Spoken supplement

前面的模型已经考虑了收入、家庭规模和各期基线，但一个家庭仍可能有一些持续的购买倾向，而且这些倾向会同时体现在多个商品上。作者假设，这些共同变化可以用少量个人特征来描述。

图中，theta_i 属于家庭，表示它的潜在特征；a_j 属于商品，表示这个商品如何对应这些特征。两者的内积描述这个家庭在观测协变量之外，对该商品的购买倾向。

虽然这些特征没有被直接记录，但同一个家庭购买多种商品、经历多个时期，就相当于从不同方面反复观察它们。因此，可以把它们也作为未知量，从整套购买记录中共同估计。这就是引入潜变量的思路。

### Failure and lesson

"引入低维潜变量刻画复杂依赖结构，突出方法创新。" is a compressed description plus an editorial instruction. The useful version establishes whose characteristics are modeled, what observations inform them, and why the construction addresses the difficulty.

## 2. Formula: establish the common object and show the steps

### Slide content

**联合估计潜变量与模型参数**

传统边际对数似然：先对每个个体的条件似然关于潜变量分布积分，再取对数并求和。

联合估计目标：保留每个个体的潜变量取值，将各个体的条件对数似然相加，与结构参数一起优化。

### Spoken supplement

两个式子从同一个条件模型出发。用 U 表示结构参数，用 theta 表示某个家庭的潜变量。先把这个家庭所有可见记录的条件密度相乘，记为 L_i(U,theta)。取对数后，乘积变成求和，记为 h_i(U,theta)。

传统方法先给潜变量指定分布 G。对 L_i 积分，得到不再包含该家庭未知潜变量的边际似然，再取对数。不同家庭相互独立，所以总对数似然是各家庭这一项的和。

本文保留每个家庭的 theta_i，直接把 h_i(U,theta_i) 相加，并把 theta_i 与 U 一起估计。共同的起点是同一个条件似然；两种方法对潜变量采用了不同处理。这样避开了高维积分，但也增加了要估计的未知量。后面的理论就要解释，回归推断是否仍然有效。

### Supporting derivation for this pair

When the formulas themselves are needed, show the corresponding steps:

    L_i(U,theta) = product of conditional densities for visible records
    h_i(U,theta) = log L_i(U,theta)
    marginal objective = sum_i log integral exp{h_i(U,theta)} dG(theta)
    joint objective = sum_i h_i(U,theta_i)

### Failure and lesson

"一个积分，一个不积分。" is too short to establish what is integrated or optimized. Define the common conditional likelihood, explain the operations, and connect the new unknowns to the next theoretical question. Preserve conditioning and any outcome-specific scale terms in an actual derivation.

## 3. Algorithm: explain each update through its data and unknowns

### Slide content

**结局参数与个体特征交替更新**

先固定当前的个体特征，逐商品更新基线、协变量系数和商品系数。

再固定商品参数，汇总每个家庭可见的商品和时期，更新该家庭的特征。

参数更新采用 Newton 法，并进行步长选择和约束处理。

### Spoken supplement

商品系数和潜变量以乘积形式出现，所以不能把所有未知量一次当作普通线性参数来求解。交替更新可以理解为轮流做两类回归，二元结局时就是 Logistic 回归。

先固定当前的潜变量。对某个商品，汇总所有家庭的可见时期，把时间虚拟变量、观测协变量和当前潜变量作为解释变量，更新这个商品的参数。此时潜变量的当前值充当已知的解释变量。

再固定商品参数。对某个家庭，汇总它所有可见商品和时期，用商品系数作为解释变量，更新这个家庭的潜变量；已经确定的时间基线和协变量项组成偏置项。

多个家庭帮助估计商品，多个商品帮助估计个人。两类更新都利用 Newton 法计算方向、选择步长，并满足相应约束，再重复交替更新。

### Failure and lesson

"第二步做GLM，第三步也做GLM。" leaves the listener unsure about the responses, predictors, offsets, and unknowns. Explain these roles for each update. Check the actual source algorithm before reusing any optimizer or convergence claim.

## 4. Results: connect the comparison to the mechanism

Author context: pair this sample with the actual source error plot. This is an asset-selection note, not slide text.

### Slide content

**共享信息如何改善回归系数估计**

横轴：结局数 J，同时取 N=10J。纵轴：回归系数矩阵的归一化误差。两个面板分别对应真实潜变量维数3和8。

### Spoken supplement

两幅图分别对应真实潜变量维数3和8。横轴是结局数 J，同时取 N=10J；纵轴是回归系数矩阵的归一化误差，越低越好。这里先看相同样本规模下，几种方法之间的差异。

逐结局随机截距模型能够表示某个家庭在一个商品上的长期偏好，但拟合这个商品时，没有利用该家庭对其他商品的购买记录。

本文中，同一个家庭的 theta_i 出现在所有商品的模型里。估计它时，可以汇总各商品的可见记录；估计某个商品的回归系数时，再使用这组共同估计的特征。模拟中每人只有四期记录，部分期次还缺失，其他商品就为估计这个家庭的特征提供了额外信息。

结局较多时，图中本文方法的误差低于逐结局随机截距模型。例如右图 J=400 时，两者误差分别为0.18和0.238，相对降低约24%。在这些模拟设置中，多个结局共同帮助估计个人特征，与回归系数估计的改善相一致。

### Failure and lesson

"红线最低，因此全面验证了本文的优越性。" overstates the evidence and does not explain the mechanism. Give the metric and fair comparison, connect it to the idea, and scope the finding to the displayed evidence.

## How to use these pairs

The good supplements contain full explanation, necessary repetition, and natural connectives. They are not meant to be read as a separate manuscript independent of the slide.

For each new page, choose the reasoning pattern that helps its audience. Do not mechanically reproduce the same introductory and concluding phrases on every page. For empirical work, apply the same care to variables, design choices, evidence, and interpretation even when no formula or algorithm is needed.
