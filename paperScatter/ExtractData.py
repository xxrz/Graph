import jsonlines
import numpy as np
from sklearn.decomposition import PCA, KernelPCA
from scipy.linalg import svd
import pandas as pd
from sklearn import manifold
from sklearn.preprocessing import scale
from sklearn.random_projection import GaussianRandomProjection, SparseRandomProjection

#这个代码用于从jsonl中提取数据并写入excel

#提取数据
feature = []
label = []
tag = 0
with open("wht/668/RGIN.jsonl", "r+", encoding="utf8") as f:
    for item in jsonlines.Reader(f):
        if "label" in item:
            if "test" in item["label"]:
                tag = 1
                continue
        if tag == 1:
            if "data" in item:
                for i in item["data"]:
                    feature.append(i)
            if "label" in item:
                label.extend(item["label"])

#数据拼接
feature = np.array(feature)
label = np.array(label)
label = label.reshape(label.size,1)

# 降维方式选择
# pca
# pca = PCA(n_components=2)
# newfeature= pca.fit_transform(feature)
# #tsne
# tsne = manifold.TSNE(n_components=2, init='pca', random_state=0)
# newfeature = tsne.fit_transform(feature)
# # #核PCA
# kpca = KernelPCA(kernel='rbf',gamma=10,n_components=2)
# newfeature = kpca.fit_transform(feature)
# #高维随机映射
gauss_proj = GaussianRandomProjection(n_components=2)
newfeature = gauss_proj.fit_transform(feature)
# #稀疏矩阵
# transformer = SparseRandomProjection(n_components=2)
# newfeature = transformer.fit_transform(feature)
# #SVD
# x_s = scale(feature, with_mean=True, with_std=False, axis=0)
# # 没必要缩放数据，full_matrices=False是一定要有的
# U, S, V = svd(x_s, full_matrices=False)
# # 选择最前两个奇异值来近似原始的矩阵
# newfeature = U[:, :2]
#

#数据拼接
data = np.hstack((newfeature,label))

#写入excel
data = pd.DataFrame(data)
writer = pd.ExcelWriter(r'wht/465/RGIN_gauss.xlsx')		# 写入Excel文件
data.to_excel(writer,index=False)		# ‘page_1’是写入excel的sheet名
writer.save()
writer.close()