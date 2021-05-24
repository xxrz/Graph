import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn
from sklearn.linear_model import LogisticRegressionCV
from sklearn.svm import SVC
import numpy as np
from matplotlib.colors import ListedColormap
import seaborn as sb

#用于不同模型的数据分布图（详细注释可以参考paperScatter.py）
#画图

# path = r"pca.xlsx"
# path = r"表\pca.xlsx"
# path = r"表/fun-gauss.xlsx"
path = r"wht/最后/RGCN_gauss.xlsx"

def paint(path,colors):
    df = pd.read_excel(path)
    markers=['8','^']
    a = [0.5, 0.5]
    for index in range(2):
        # 不抖动数据
        x = df.loc[df['label'] == index]['x']
        y = df.loc[df['label'] == index]['y']
        plt.scatter(x, y, c=colors[index], cmap='brg', s=90, marker=markers[index], linewidth=0, alpha=a[index],zorder=10)
        plt.scatter(x, y, c=colors[index], cmap='brg', s=90, marker=markers[index], linewidth=0,alpha=a[index],zorder=10)
        # # 设置抖动
        # sb.regplot(data=df, x=x, y=y, marker=markers[index],fit_reg=False,color=colors[index],
        #            x_jitter=0.001, y_jitter=0.001, scatter_kws={'alpha': 2/3,'s':25})

#设置坐标
#7.5
fig = plt.figure(figsize=(16,7), dpi=80)
ax = fig.add_axes([0.12, 0.05, 0.78, 0.78], zorder=11)
ax.set_xticks([])
ax.set_yticks([])
#手动添加设置图例
font = {'family': 'Arial',
            'weight': 'normal',
            'size': 58.5,
            }
# colors = ['#003f5c','#ffcca8']
# colors = ['#ffcca8','#003f5c']
# colors = ['#ffa600','#003f5c']
colors = ['#d2c4e9','#473192']
# colors = ['b','g']
a = [0.5,0.5]
markers=['8','^']
#legend标签列表
# labels = ['Positive NVD+Sard Samples','Negative NVD+Sard Samples']
# labels = ['Positive GitHub Samples','Negative GitHub Samples']
labels = ['Pos. Samples','Neg. Samples']
# labels = ['CPU','GPU']
#用label和color列表生成mpatches.Patch对象，它将作为句柄来生成legend
patches = [ ax.plot([],[], marker=markers[i], ms=40, ls="", mec=None,alpha=a[i], color=colors[i],
            label="{:s}".format(labels[i]) )[0]  for i in range(len(labels)) ]
# ax.legend(handles=patches,loc='lower left', ncol=1, prop=font,handletextpad=0)
# ax.legend(handles=patches,loc='upper right', ncol=1, prop=font,columnspacing=1,handletextpad=0)
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width, box.height * 0.9])
#-0.032, 1.15
ax.legend(handles=patches,loc='center left', bbox_to_anchor=(-0.032, 1.15), ncol=2, prop=font,columnspacing=0.1,handletextpad=0.05,handlelength=1)

#绘制决策边界
df = pd.read_excel(path)
X = df[['x','y']].values
y = df['label'].values

def plot_svc_decision_function(model, ax=None, plot_support=True):
    """Plot the decision function for a 2D SVC"""
    if ax is None:
        ax = plt.gca()

    # get the range of x
    xlim = ax.get_xlim()
    # get the range of y
    ylim = ax.get_ylim()

    # create grid to evaluate model
    x = np.linspace(xlim[0], xlim[1], 30)
    y = np.linspace(ylim[0], ylim[1], 30)
    Y, X = np.meshgrid(y, x)

    # xy列
    xy = np.vstack([X.ravel(), Y.ravel()]).T
    P = model.decision_function(xy).reshape(X.shape)

    # plot decision boundary and margins
    ax.contour(X, Y, P, colors='k',levels=[-10,0,10],linestyles="--",linewidths=5)
    # ax.contourf(X, Y, P, colors=['lightcyan','honeydew'],levels=[-10,0,10])
    # ax.contour(X, Y, P, colors='k', levels=[-15, 0, 15], linestyles="--", linewidths=5)
    # ax.contourf(X, Y, P, colors=['lightcyan', 'honeydew'], levels=[-15, 0, 15])
    # plot support vectors
    if plot_support:
        ax.scatter(model.support_vectors_[:, 0], model.support_vectors_[:, 1], s=300, linewidth=1, facecolors='none')
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)

clf = SVC(kernel='linear')
clf.fit(X, y)
paint(path,colors)
# plot_svc_decision_function(clf)
plt.savefig(r'wht/最后/RGCN_gauss.pdf')
plt.show()






