## 功課要求
請寫一個梯度下降法程式可以找任何向量函數的谷底

## 提示
用數值偏微分就好
```python
# 函數 f 對變數 p[k] 的偏微分: df / dp[k]
def df(f, p, k):
    p1 = p.copy()
    p1[k] = p[k]+step
    return (f(p1) - f(p)) / step

# 梯度：函數 f 在點 p 上的梯度
def grad(f, p):
    gp = p.copy()
    for k in range(len(p)):
        gp[k] = df(f, p, k)
    return gp
```

## 自作部分
因為不一開始不太理解有使用chatgpt輔助，嘔來有把code重打一次並理解code。
