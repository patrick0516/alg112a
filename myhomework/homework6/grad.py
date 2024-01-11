def gradient_descent(f, initial_p, learning_rate, num_iterations):
    p = initial_p.copy()

    for _ in range(num_iterations):
        # 計算梯度
        gradient = grad(f, p)

        # 更新參數
        for k in range(len(p)):
            p[k] = p[k] - learning_rate * gradient[k]

        # 顯示目前的位置和目標函數值
        print("Iteration {}: p = {}, f(p) = {}".format(_, p, f(p)))

    return p

# 示範使用
def example_function(p):
    return p[0]**2 + p[1]**2 + p[2]**2  # 一個簡單的二次函數

# 初始參數
initial_params = [1.0, 2.0, 3.0]

# 設定學習率和迭代次數
learning_rate = 0.1
num_iterations = 100

# 使用梯度下降法尋找谷底
result_params = gradient_descent(example_function, initial_params, learning_rate, num_iterations)

print("最終結果：p = {}, f(p) = {}".format(result_params, example_function(result_params)))
