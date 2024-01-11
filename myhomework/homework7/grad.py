from micrograd import Tensor

def gradient_descent(f, initial_p, learning_rate, num_iterations):
    p = [Tensor(x) for x in initial_p]

    for i in range(num_iterations):
        # 計算梯度
        gradient = f(p).backward()

        # 更新参数
        for param, grad in zip(p, gradient):
            param.data -= learning_rate * grad.data

        print("選代 {}: p = {}, f(p) = {}".format(i, [param.data for param in p], f(p).data))

    return [param.data for param in p]


def example_function(p):
    return p[0]**2 + p[1]**2 + p[2]**2  

# 初始參數
initial_params = [1.0, 2.0, 3.0]

# 設置學習率與選代參數
learning_rate = 0.1
num_iterations = 100

# 使用梯度下降法尋找谷底
result_params = gradient_descent(example_function, initial_params, learning_rate, num_iterations)

print("最终结果：p = {}, f(p) = {}".format(result_params, example_function(result_params)))

