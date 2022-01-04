import numpy as np
from copy import deepcopy


def orthonormalization(A):
    B = deepcopy(A).T
    Q = np.array([B[0] / np.linalg.norm(B[0])])
    for k in range(1, len(B)):
        q_k = B[k] - np.sum([np.dot(B[k], Q[i]) * Q[i] for i in range(k-1)], axis=0)
        q_k = q_k / np.linalg.norm(q_k)
        Q = np.append(Q, [q_k], axis=0)
    return Q.T
