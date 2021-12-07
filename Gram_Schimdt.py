import numpy as np
from copy import deepcopy


def orthonormalization(A):
    A = deepcopy(A).T
    Q = np.array([A[0] / np.linalg.norm(A[0])])
    for k in range(1, len(A)):
        q_k = A[k] - np.sum([np.dot(A[i], Q[i]) * Q[i] for i in range(k-1)], axis=0)
        q_k = q_k / np.linalg.norm(q_k)
        Q = np.append(Q, [q_k], axis=0)
    return Q.T
