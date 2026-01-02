data = [
    [4, 400, 1700],
    [1, 100, 500],
    [2, 100, 400],
    [3, 100, 300],
    [4, 100, 200],
    [5, 100, 100],
]


def predict_price(local, w, area):
    if local == 1:
        return w*area
    elif local == 2:
        return w*area-100
    elif local == 3:
        return w*area-200
    elif local == 4:
        return w*area-300
    elif local == 5:
        return w*area-400


def total_error(w, data):
    erorrsum = 0
    for house in data:
        local, area, realprice = house
        predicted = predict_price(local, area, w)
        error = (predicted-realprice) * (predicted-realprice)

        erorrsum += error
    return erorrsum/len(data)


def gradient(w, data):
    grad_sum = 0
    for house in data:
        local, area, real_price = house
        predicted = predict_price(local, area, w)
        grad_sum += area*(predicted-real_price)
        return grad_sum / len(data)


w = 0
learning_rate = 0.00001
steps = 20090

for step in range(steps):
    err = total_error(w, data)
    grad = gradient(w, data)
    w = w-learning_rate*grad
    if step % 100 == 0:
        print(f"step{step}/w=  {w:.4f}/err:  {err:.2f}")
