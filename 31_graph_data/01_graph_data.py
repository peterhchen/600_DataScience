import numpy as np
G_dense = np.array([ [0, 2, 1],
                     [2, 0, 0],
                     [1, 0, 0] ])
                     
G_masked = np.ma.masked_values(G_dense, 0)
from scipy.sparse import csr_matrix

G_sparse = csr_matrix(G_dense)
print(G_sparse.data)