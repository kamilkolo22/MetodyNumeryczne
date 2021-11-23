import numpy as np
import CalcDet as Det
import PermutaionSign as Sig
import time
import matplotlib.pyplot as plt


def plot_laplace_leibniz_comp(wym=6, seed=123):
    time_laplace = []
    time_leibniz = []
    time_laplace_fast = []
    time_gauss = []

    np.random.seed(seed)
    for i in range(wym):
        A = np.random.rand(i+1, i+1)

        start_time = time.time()
        Det.det_laplace_formula_fast(A.copy())
        time_laplace_fast.append(time.time() - start_time)

        start_time = time.time()
        Det.det_leibniz_formula(A.copy())
        time_leibniz.append(time.time() - start_time)

        start_time = time.time()
        Det.det_laplace_formula(A.copy())
        time_laplace.append(time.time() - start_time)

        start_time = time.time()
        Det.det_gauss_elimination(A.copy())
        time_gauss.append(time.time() - start_time)

    plt.style.use('seaborn-whitegrid')
    fig = plt.figure()
    ax = plt.axes()
    # plt.plot(range(1, wym+1), time_laplace, 'ro',
    #          color="b", label='Laplace')
    plt.plot(range(1, wym + 1), time_gauss, 'ro',
             color="b", label='Gauss')
    plt.plot(range(1, wym+1), time_leibniz, 'ro',
             color="r", label='Leibniz')
    plt.plot(range(1, wym+1), time_laplace_fast, 'ro',
             color="g", label='Laplace Fast')
    plt.legend()
    plt.show()


def leibniz_dif_perm_comp(wym=10):
    time_leibniz1 = []
    time_leibniz2 = []
    time_leibniz3 = []

    for i in range(wym):
        A = np.random.rand(6, 6)

        start_time = time.time()
        Det.det_leibniz_formula(A.copy())
        time_leibniz1.append(time.time() - start_time)

        start_time = time.time()
        Det.det_leibniz_formula2(A.copy())
        time_leibniz2.append(time.time() - start_time)

        start_time = time.time()
        Det.det_leibniz_formula3(A.copy())
        time_leibniz3.append(time.time() - start_time)

    plt.style.use('seaborn-whitegrid')
    fig = plt.figure()
    ax = plt.axes()
    plt.plot(range(1, wym + 1), time_leibniz1, 'ro',
             color="r", label='Leibniz')
    plt.plot(range(1, wym + 1), time_leibniz2, 'ro',
             color="g", label='Leibniz2')
    plt.plot(range(1, wym + 1), time_leibniz3, 'ro',
             color="pink", label='Leibniz3')
    plt.legend()
    plt.show()
