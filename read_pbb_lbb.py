import numpy as np

# pbbPath = '/data/yangqinzhu/ctLung/DeepLung-master/detector/results/res18/retrft969/val150/1.3.6.1.4.1.14519.5.2.1.6279.6001.102681962408431413578140925249_pbb.npy'
pbbPath = '/data/yangqinzhu/ctLung/DeepLung-master/detector/results/res18/retrft969/val150/1.3.6.1.4.1.14519.5.2.1.6279.6001.109882169963817627559804568094_pbb.npy'
pbb = np.load(pbbPath)
print('pbb', pbb, pbb.shape)
# lbbPath = '/data/yangqinzhu/ctLung/DeepLung-master/detector/results/res18/retrft969/val150/1.3.6.1.4.1.14519.5.2.1.6279.6001.102681962408431413578140925249_lbb.npy'
lbbPath = '/data/yangqinzhu/ctLung/DeepLung-master/detector/results/res18/retrft969/val150/1.3.6.1.4.1.14519.5.2.1.6279.6001.109882169963817627559804568094_lbb.npy'
lbb = np.load(lbbPath)
print('lbb', lbb)