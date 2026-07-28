# WaferBalance 示例 v0.3

> v0.3 修正点：第 1 次 Balance 改为按机台 WPH 比例分配 Lot 片数；第 2~5 次仍按上一轮 Weight 分配。  
> Lot 片数均不超过 25；第 5 次 Balance 展示全部 qsort category（0 / 6 / 12 / 24）的结果。

## 1. 示例输入

| 机台 | UPH / WPH | 含义 |
| --- | ---: | --- |
| E1 | 20 | 每小时可作业 20 片 Wafer |
| E2 | 40 | 每小时可作业 40 片 Wafer |
| E3 | 60 | 每小时可作业 60 片 Wafer |

| qsort category | Lot | Lot Qty | 可作业机台 |
| ---: | --- | ---: | --- |
| 0 | LotA | 20 | E1, E2 |
| 6 | LotB | 25 | E2, E3 |
| 12 | LotC | 13 | E1, E3 |
| 24 | LotD | 20 | E1, E2, E3 |

## 2. 计算规则

### 2.1 第 1 次 Balance

第 1 次 Balance 按该 Lot 所有可作业机台的 WPH 比例分配 Lot Qty：

```text
Qty Assign(1, EQP)
= Lot Qty × WPH(EQP) / sum(该 Lot 所有可作业机台 WPH)

Step WIP Time(1) = Qty Assign(1) / WPH
New EQP WIP Time(1) = Pre EQP WIP Time + Step WIP Time(1)
Weight(1) = 1 / New EQP WIP Time(1)
```

### 2.2 第 2 次及以后 Balance

第 2 次及以后，先按上一轮 Weight 重新分配 Lot Qty，再计算本轮累计时间和新 Weight：

```text
Qty Assign(n)
= Lot Qty × Weight(n-1, 当前机台)
  / sum(Weight(n-1, 该 Lot 所有可作业机台))

Step WIP Time(n) = Qty Assign(n) / WPH

New EQP WIP Time(n)
= Pre EQP WIP Time + Step WIP Time(n)

Weight(n)
= (1 / New EQP WIP Time(n)) × Weight(n-1)
```

每一次 Balance 都按 qsort category 从小到大计算：

```text
0 → 6 → 12 → 24
```

后一 category 继承前一 category 结束后的机台累计时间。

## 3. 第 1 次 Balance

### 3.1 category 0：LotA

LotA Qty = 20，可作业机台 E1 / E2。按 WPH 比例分配：

```text
E1 Qty = 20 × 20 / (20 + 40) = 6.667
E2 Qty = 20 × 40 / (20 + 40) = 13.333
```

| Lot | EQP | Qty Assign(1) | Step WIP Time | Pre EQP WIP Time | New EQP WIP Time(1) | Weight(1) |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| LotA | E1 | 6.667 | 0.333 | 0.000 | 0.333 | 3.000 |
| LotA | E2 | 13.333 | 0.333 | 0.000 | 0.333 | 3.000 |

category 0 结束累计：

```text
E1=0.333, E2=0.333, E3=0.000
```

### 3.2 category 6：LotB

继承 category 0：

```text
Pre: E1=0.333, E2=0.333, E3=0.000
```

| Lot | EQP | Qty Assign(1) | Step WIP Time | Pre EQP WIP Time | New EQP WIP Time(1) | Weight(1) |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| LotB | E2 | 10.000 | 0.250 | 0.333 | 0.583 | 1.714 |
| LotB | E3 | 15.000 | 0.250 | 0.000 | 0.250 | 4.000 |

category 6 结束累计：

```text
E1=0.333, E2=0.583, E3=0.250
```

### 3.3 category 12：LotC

继承 category 6：

```text
Pre: E1=0.333, E2=0.583, E3=0.250
```

| Lot | EQP | Qty Assign(1) | Step WIP Time | Pre EQP WIP Time | New EQP WIP Time(1) | Weight(1) |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| LotC | E1 | 3.250 | 0.163 | 0.333 | 0.496 | 2.017 |
| LotC | E3 | 9.750 | 0.163 | 0.250 | 0.412 | 2.424 |

category 12 结束累计：

```text
E1=0.496, E2=0.583, E3=0.412
```

### 3.4 category 24：LotD

继承 category 12：

```text
Pre: E1=0.496, E2=0.583, E3=0.412
```

| Lot | EQP | Qty Assign(1) | Step WIP Time | Pre EQP WIP Time | New EQP WIP Time(1) | Weight(1) |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| LotD | E1 | 3.333 | 0.167 | 0.496 | 0.663 | 1.509 |
| LotD | E2 | 6.667 | 0.167 | 0.583 | 0.750 | 1.333 |
| LotD | E3 | 10.000 | 0.167 | 0.412 | 0.579 | 1.727 |

第 1 次 Balance 结束累计：

```text
E1=0.663, E2=0.750, E3=0.579
```

## 4. 第 2 次 Balance

| category | Lot | EQP | Weight(1) | Qty Assign(2) | Step WIP Time | Pre EQP WIP Time | New EQP WIP Time(2) | Weight(2) |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 0 | LotA | E1 | 3.000 | 10.000 | 0.500 | 0.000 | 0.500 | 6.000 |
| 0 | LotA | E2 | 3.000 | 10.000 | 0.250 | 0.000 | 0.250 | 12.000 |
| 6 | LotB | E2 | 1.714 | 7.500 | 0.187 | 0.250 | 0.438 | 3.918 |
| 6 | LotB | E3 | 4.000 | 17.500 | 0.292 | 0.000 | 0.292 | 13.714 |
| 12 | LotC | E1 | 2.017 | 5.904 | 0.295 | 0.500 | 0.795 | 2.536 |
| 12 | LotC | E3 | 2.424 | 7.096 | 0.118 | 0.292 | 0.410 | 5.914 |
| 24 | LotD | E1 | 1.509 | 6.607 | 0.330 | 0.795 | 1.126 | 1.341 |
| 24 | LotD | E2 | 1.333 | 5.836 | 0.146 | 0.438 | 0.583 | 2.285 |
| 24 | LotD | E3 | 1.727 | 7.557 | 0.126 | 0.410 | 0.536 | 3.222 |

第 2 次 Balance 结束累计：

```text
E1=1.126, E2=0.583, E3=0.536
```

## 5. 第 3 次 Balance 结果

| category | Lot | EQP | Weight(2) | Qty Assign(3) | Step WIP Time | Pre EQP WIP Time | New EQP WIP Time(3) | Weight(3) |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 0 | LotA | E1 | 6.000 | 6.667 | 0.333 | 0.000 | 0.333 | 18.000 |
| 0 | LotA | E2 | 12.000 | 13.333 | 0.333 | 0.000 | 0.333 | 36.000 |
| 6 | LotB | E2 | 3.918 | 5.556 | 0.139 | 0.333 | 0.472 | 8.298 |
| 6 | LotB | E3 | 13.714 | 19.444 | 0.324 | 0.000 | 0.324 | 42.318 |
| 12 | LotC | E1 | 2.536 | 3.902 | 0.195 | 0.333 | 0.528 | 4.800 |
| 12 | LotC | E3 | 5.914 | 9.098 | 0.152 | 0.324 | 0.476 | 12.431 |
| 24 | LotD | E1 | 1.341 | 3.916 | 0.196 | 0.528 | 0.724 | 1.852 |
| 24 | LotD | E2 | 2.285 | 6.674 | 0.167 | 0.472 | 0.639 | 3.576 |
| 24 | LotD | E3 | 3.222 | 9.409 | 0.157 | 0.476 | 0.633 | 5.094 |

第 3 次 Balance 结束累计：

```text
E1=0.724, E2=0.639, E3=0.633
```

## 6. 第 4 次 Balance 结果

| category | Lot | EQP | Weight(3) | Qty Assign(4) | Step WIP Time | Pre EQP WIP Time | New EQP WIP Time(4) | Weight(4) |
| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 0 | LotA | E1 | 18.000 | 6.667 | 0.333 | 0.000 | 0.333 | 54.000 |
| 0 | LotA | E2 | 36.000 | 13.333 | 0.333 | 0.000 | 0.333 | 108.000 |
| 6 | LotB | E2 | 8.298 | 4.098 | 0.102 | 0.333 | 0.436 | 19.041 |
| 6 | LotB | E3 | 42.318 | 20.902 | 0.348 | 0.000 | 0.348 | 121.479 |
| 12 | LotC | E1 | 4.800 | 3.621 | 0.181 | 0.333 | 0.514 | 9.331 |
| 12 | LotC | E3 | 12.431 | 9.379 | 0.156 | 0.348 | 0.505 | 24.632 |
| 24 | LotD | E1 | 1.852 | 3.520 | 0.176 | 0.514 | 0.690 | 2.682 |
| 24 | LotD | E2 | 3.576 | 6.798 | 0.170 | 0.436 | 0.606 | 5.904 |
| 24 | LotD | E3 | 5.094 | 9.682 | 0.161 | 0.505 | 0.666 | 7.648 |

第 4 次 Balance 结束累计：

```text
E1=0.690, E2=0.606, E3=0.666
```

## 7. 第 5 次 Balance：完整 category 展示

### 7.1 category 0：LotA

| Lot | EQP | Weight(4) | Qty Assign(5) | Step WIP Time | Pre EQP WIP Time | New EQP WIP Time(5) | Weight(5) |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| LotA | E1 | 54.000 | 6.667 | 0.333 | 0.000 | 0.333 | 162.000 |
| LotA | E2 | 108.000 | 13.333 | 0.333 | 0.000 | 0.333 | 324.000 |

### 7.2 category 6：LotB

继承第 5 次 category 0：

```text
Pre: E1=0.333, E2=0.333, E3=0.000
```

| Lot | EQP | Weight(4) | Qty Assign(5) | Step WIP Time | Pre EQP WIP Time | New EQP WIP Time(5) | Weight(5) |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| LotB | E2 | 19.041 | 3.388 | 0.085 | 0.333 | 0.418 | 45.549 |
| LotB | E3 | 121.479 | 21.612 | 0.360 | 0.000 | 0.360 | 337.246 |

### 7.3 category 12：LotC

继承第 5 次 category 6：

```text
Pre: E1=0.333, E2=0.418, E3=0.360
```

| Lot | EQP | Weight(4) | Qty Assign(5) | Step WIP Time | Pre EQP WIP Time | New EQP WIP Time(5) | Weight(5) |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| LotC | E1 | 9.331 | 3.572 | 0.179 | 0.333 | 0.512 | 18.227 |
| LotC | E3 | 24.632 | 9.428 | 0.157 | 0.360 | 0.517 | 47.612 |

### 7.4 category 24：LotD

继承第 5 次 category 12：

```text
Pre: E1=0.512, E2=0.418, E3=0.517
```

| Lot | EQP | Weight(4) | Qty Assign(5) | Step WIP Time | Pre EQP WIP Time | New EQP WIP Time(5) | Weight(5) |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| LotD | E1 | 2.682 | 3.304 | 0.165 | 0.512 | 0.677 | 3.961 |
| LotD | E2 | 5.904 | 7.274 | 0.182 | 0.418 | 0.600 | 9.842 |
| LotD | E3 | 7.648 | 9.422 | 0.157 | 0.517 | 0.674 | 11.340 |

第 5 次 Balance 结束累计：

```text
E1=0.677, E2=0.600, E3=0.674
```

## 8. 示例结论

1. qsort category 按 `0 → 6 → 12 → 24` 计算。
2. 第 1 次 Balance 按可作业机台 WPH 比例分配 Lot Qty。
3. WPH / UPH 用于将 Qty Assign 换算为 Step WIP Time。
4. 后一 category 继承前一 category 结束后的 EQP WIP Time。
5. 第 1 次 `Weight(1) = 1 / New EQP WIP Time(1)`。
6. 第 2 次及以后按上一轮 Weight 分配 Lot Qty。
7. 第 2 次及以后 `Weight(n) = (1 / New EQP WIP Time(n)) × Weight(n-1)`。
8. 全部 category 计算完一遍后，才进入下一次 Balance。
9. WaferBalance 共执行 5 次 Balance。
10. 第 5 次 Balance 后，本示例的机台累计作业时间趋近于均衡：E1=0.677、E2=0.600、E3=0.674。
