import numpy as np
G2_data = np.array
([
   [np.inf, 2, 0 ],
   [2, np.inf, np.inf],
   [0, np.inf, np.inf]
])
G2_masked = np.ma.masked_invalid(G2_data)
from scipy.sparse.csgraph import csgraph_from_dense
# G2_sparse = csr_matrix(G2_data) would give the wrong result
G2_sparse = csgraph_from_dense(G2_data, null_value=np.inf)
print(G2_sparse.data)
