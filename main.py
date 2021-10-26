import numpy as np
import CalcDet as Det
import PermutaionSign as Sig
import time
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')


if __name__ == '__main__':

    wym = 7
    time_laplace = []
    time_leibniz = []

    # np.random.seed(1234)
    # for i in range(wym):
    #     A = np.random.rand(i+1, i+1)
    #
    #     start_time = time.time()
    #     Det.det_laplace_formula(A.copy())
    #     time_laplace.append(time.time() - start_time)
    #
    #     start_time = time.time()
    #     Det.det_leibniz_formula(A.copy())
    #     time_leibniz.append(time.time() - start_time)

    for i in range(10):
        A = np.random.rand(wym, wym)

        start_time = time.time()
        Det.det_leibniz_formula(A.copy())
        time_leibniz.append(time.time() - start_time)

        start_time = time.time()
        Det.det_laplace_formula(A.copy())
        time_laplace.append(time.time() - start_time)

    print("Leibniz:\n")
    print(time_leibniz)
    print("Laplace:\n")
    print(time_laplace)

    fig = plt.figure()
    ax = plt.axes()
    # ax.plot(range(1, wym+1), time_laplace, color="blue")
    # ax.plot(range(1, wym+1), time_leibniz, color="red")
    plt.plot(time_laplace, 'ro', color="blue")
    plt.plot(time_leibniz, 'ro', color="red")
    plt.show()