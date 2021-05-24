import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn
from sklearn.metrics import roc_curve, auc  ###计算roc和auc
import matplotlib.patches as patches

"""
此代码用于画CCS论文的折线图
注释掉的代码部分不用管
每个方法前都写明了功能
代码具体注释可以看roc11函数（详细）
"""

# def linechart(path,name):
#     """画折线图"""
#
#     #读取数据
#     df = pd.read_excel(path)
#     x = df['num']
#     y1 = df['uvuldeepecker'].values
#     y2 = df['vuldeepecker'].values
#     y3 = df['GraphDNN'].values
#
#     #设置画布大小以及x轴和y轴
#     fig = plt.figure(figsize=(16,8),dpi=80)
#     #这步很关键
#     x = np.arange(len(x))
#     plt.xticks(np.arange(6), ('200', '400', '600', '800', '1000','max'), fontsize=18,weight =700)
#     plt.yticks([0,0.5,0.6,0.7,0.8,0.9,1,1.0], fontsize=18,weight =700)
#     plt.xlabel('sampleSize', fontsize=18,weight=700)
#     plt.ylabel('f1', fontsize=18,weight=700)
#
#     #画图
#     plt.plot(x,y1,linewidth=3,label='uvuldeepecker',marker='o',markersize=8)
#     plt.plot(x, y2, linewidth=3, label='vuldeepecker', marker='o', markersize=8)
#     plt.plot(x,y3,linewidth=3,label='GraphDNN',marker='o',markersize=8)
#
#     # 设置数字标签
#     # for a, b in zip(x, y1):
#     #     if b < 0.5:
#     #         plt.text(a, b,"fail", ha='left', va='top', fontsize=15)
#     #     else:
#     #         plt.text(a, b, b, ha='left', va='top', fontsize=15)
#     # for a, b in zip(x, y2):
#     #     if b < 0.5:
#     #         plt.text(a, b, "fail", ha='right', va='bottom', fontsize=15)
#     #     else:
#     #         plt.text(a, b, b, ha='right', va='bottom', fontsize=15)
#     # for a, b in zip(x, y3):
#     #     if b < 0.5:
#     #         plt.text(a, b,"fail", ha='center', va='center', fontsize=15)
#     #     else:
#     #         plt.text(a, b, b, ha='center', va='center', fontsize=15)
#
#     #设置图例
#     font = {'family': 'Arial',
#              'weight': 'normal',
#              'size': 15,
#              }
#     plt.legend(loc='best',prop=font)
#     plt.grid(alpha=0.8, linestyle=':')
#
#     #可以保存为svg这种矢量图片的格式,放大不会有锯齿
#     plt.savefig(str(name)+'.pdf')
#
#     #对保存的图片进行显示
#     #plt.show()
#
# ##===========================折线图：model outdated===========================
# def linechart5(path,name):
#     #读取数据
#     df = pd.read_excel(path)
#     x = df['date']
#     y1 = df['p=0'].values
#     y2 = df['p=0.05'].values
#     y3 = df['p=0.1'].values
#     y4 = df['p=0.2'].values
#
#     #设置画布大小以及x轴和y轴
#     # fig = plt.figure(figsize=(16,7.5),dpi=80)
#     fig = plt.figure(figsize=(16, 5), dpi=80)
#     ax = fig.add_axes([0.12, 0.2, 0.7, 0.7], zorder=11)
#     # ax =  fig.add_subplot(zorder=11)
#
#     ax.set_xticks(np.arange(0, 5))
#     ax.set_xticklabels(x, fontdict={'horizontalalignment': 'center', 'size': 25})
#     ax.set_yticks(np.arange(0.4, 0.92, 0.1))
#     ax.set_yticklabels([0.4,0.5,0.6,0.7,0.8,0.9],
#                        fontdict={'horizontalalignment': 'right', 'size': 25})
#     ax.set_xlabel('Testing period(year)',fontsize=28)
#     ax.set_ylabel('F1 SCORE', fontsize=28)
#     ax.set_xlim((-0.5, 4.5))
#     ax.set_ylim((0.4,0.92))
#
#     #画图
#     #linestyle：'-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'
#     ax.plot(x,y1,linestyle="--",linewidth=5,label='Ratio=0',marker='^',markersize=18,color=seaborn.xkcd_rgb['grey blue'])
#     ax.plot(x,y2, linestyle="-",linewidth=5, label='Ratio=0.05', marker='X', markersize=18,color=seaborn.xkcd_rgb['grey green'])
#     ax.plot(x,y3,linestyle="-.",linewidth=5,label='Ratio=0.1',marker='p',markersize=18,color=seaborn.xkcd_rgb['pale purple'])
#     ax.plot(x, y4, linestyle=":",linewidth=5, label='Ratio=0.2', marker='*', markersize=18,color=seaborn.xkcd_rgb['tan'])
#
#     # for a, b in zip(x, y1):
#     #     #显示数字标签为百分数
#     #     plt.text(a, b, '%.0f%%' % (b * 100), ha='right', va='bottom', fontsize=20)      #ha为水平位置，va为垂直位置
#     # for a, b in zip(x, y2):
#     #     plt.text(a, b, '%.0f%%' % (b * 100), ha='right', va='bottom', fontsize=20)
#     # for a, b in zip(x, y3):
#     #     plt.text(a, b, '%.0f%%' % (b * 100), ha='left', va='top', fontsize=20)
#     # for a, b in zip(x, y4):
#     #     plt.text(a, b, '%.0f%%' % (b * 100), ha='left', va='top', fontsize=20)
#
#
#     # 设置图例
#     font = {'family': 'Times New Roman',
#             'weight': 'normal',
#             'size': 27,
#             }
#     plt.legend(loc='lower left', prop=font)
#     plt.grid(axis="y",alpha=0.8, linestyle=':')
#
#     # 可以保存为svg这种矢量图片的格式,放大不会有锯齿
#     plt.savefig(str(name) + '.pdf')
#
#     # 对保存的图片进行显示
#     plt.show()
#
# ##===========================折线图：training set===========================
# def linechart6(path,name):
#     #读取数据
#     df = pd.read_excel(path)
#     x = df['ratio'].values
#     y1 = df['SAP_precision'].values
#     y2 = df['SAP_Recall'].values
#     y3 = df['SAP_F1'].values
#     y4 = df['Ours_precision'].values
#     y5 = df['Ours_Recall'].values
#     y6 = df['Ours_F1'].values
#
#     #设置画布大小以及x轴和y轴
#     # fig = plt.figure(figsize=(16,7.5),dpi=80)
#     fig = plt.figure(figsize=(16, 5), dpi=80)
#     ax = fig.add_axes([0.1, 0.2, 0.8, 0.8],zorder=11)
#     ax.set_xticks(np.arange(0.1,0.87,0.1))
#     ax.set_xticklabels([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8], fontdict={'horizontalalignment': 'center', 'size': 28})
#     ax.set_yticks(np.arange(0, 1.02, 0.2))
#     ax.set_yticklabels([0, 0.2, 0.4, 0.6,0.8,1],
#                        fontdict={'horizontalalignment': 'right', 'size': 28})
#     plt.xlabel('Positive rate in training set', fontsize=30)
#     # ax.set_ylabel('SCORE', fontsize=30, weight=700)
#     # ax.set_xlim((-0.5, 16))
#     ax.set_ylim((0,1.02))
#
#     #画图
#     #linestyle：'-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'
#     ax.plot(x, y1, linestyle=":", linewidth=5, label='45%_Precision', marker='^', markersize=18,
#             color=seaborn.xkcd_rgb['warm grey'])
#     ax.plot(x, y4, linestyle="-", linewidth=5, label='10%_Precision', marker='$o$', markersize=22,
#             color=seaborn.xkcd_rgb['wisteria'])
#     ax.plot(x, y2, linestyle=":", linewidth=5, label='45%_Recall', marker='p', markersize=18,
#             color=seaborn.xkcd_rgb['grey blue'])
#     ax.plot(x, y5, linestyle="-", linewidth=5, label='10%_Recall', marker='*', markersize=22,
#             color=seaborn.xkcd_rgb['tan'])
#     ax.plot(x, y3, linestyle=":", linewidth=5, label='45%_F1', marker='X', markersize=20,
#             color=seaborn.xkcd_rgb['dirty pink'])
#     ax.plot(x, y6, linestyle="-", linewidth=5, label='10%_F1', marker='D', markersize=14,
#             color=seaborn.xkcd_rgb['flat green'])
#     # 设置图例
#     font = {'family': 'Times New Roman',
#             'weight': 'normal',
#             'size': 17
#             }
#     # plt.legend(loc='lower left', prop=font)
#     # plt.grid(axis="y",alpha=0.8, linestyle=':')
#
#     box = ax.get_position()
#     ax.set_position([box.x0, box.y0, box.width, box.height * 0.8])
#     ax.legend(loc='center left', bbox_to_anchor=(-0.07, 1.09), ncol=6, prop=font)
#     # ax.legend(loc='center left', bbox_to_anchor=(0.12, 0.18), ncol=2, prop=font)
#     plt.grid(axis="y", alpha=0.8, linestyle=':')
#
#     # 可以保存为svg这种矢量图片的格式,放大不会有锯齿
#     plt.savefig(str(name) + '.pdf')
#
#     # 对保存的图片进行显示
#     plt.show()
#
# def linechart61(path,name):
#     #读取数据
#     df = pd.read_excel(path)
#     x = df['ratio'].values
#     # y1 = df['Accuracy'].values
#     y2 = df['Precision'].values
#     y3 = df['Recall'].values
#     y4 = df['F1 Score'].values
#
#     #设置画布大小以及x轴和y轴
#     fig = plt.figure(figsize=(16, 4), dpi=80)
#     ax = fig.add_axes([0.12, 0.22, 0.7, 0.8],zorder=11)
#     # fig = plt.figure(figsize=(16, 4), dpi=80)
#     # ax = fig.add_axes([0.12, 0.22, 0.7, 0.9], zorder=11)
#     ax.set_xticks(np.arange(0.1,0.87,0.1))
#     ax.set_xticklabels([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8], fontdict={'horizontalalignment': 'center', 'size': 28})
#     ax.set_yticks(np.arange(0.2, 1.02, 0.2))
#     ax.set_yticklabels([0.2,0.4,0.6,0.8,1],
#                        fontdict={'horizontalalignment': 'right', 'size': 28})
#     plt.xlabel('Positive-negative ratio', fontsize=30)
#     # ax.set_ylabel('SCORE', fontsize=30, weight=700)
#     # ax.set_xlim((-0.5, 16))
#     ax.set_ylim((0.2,1.02))
#
#     # ax.plot(x, y1, linestyle=":", linewidth=5, label='Accuracy', marker='^', markersize=18,
#     #         color=seaborn.xkcd_rgb['grey green'])
#     ax.plot(x, y2, linestyle="-", linewidth=5, label='Precision', marker='$o$', markersize=22,
#             color=seaborn.xkcd_rgb['grey green'])
#     ax.plot(x, y3, linestyle=":", linewidth=5, label='Recall', marker='p', markersize=18,
#             color=seaborn.xkcd_rgb['grey blue'])
#     ax.plot(x, y4, linestyle="-", linewidth=5, label='F1 score', marker='*', markersize=22,
#             color=seaborn.xkcd_rgb['tan'])
#
#     # 设置图例
#     font = {'family': 'Times New Roman',
#             'weight': 'normal',
#             'size': 27
#             }
#     # plt.legend(loc='lower right', prop=font)
#     # plt.grid(axis="y",alpha=0.8, linestyle=':')
#
#     box = ax.get_position()
#     ax.set_position([box.x0, box.y0, box.width, box.height * 0.8])
#     ax.legend(loc='center left', bbox_to_anchor=(0.48, 0.35), ncol=1, prop=font)
#     # ax.legend(loc='center left', bbox_to_anchor=(0.12, 0.18), ncol=2, prop=font)
#     plt.grid(axis="y", alpha=0.8, linestyle=':')
#
#     # 可以保存为svg这种矢量图片的格式,放大不会有锯齿
#     plt.savefig(str(name) + '.pdf')
#
#     # 对保存的图片进行显示
#     plt.show()
#
# ##===========================折线图：training set===========================
# def linechart7(path,name):
#     #读取数据
#     df = pd.read_excel(path)
#     x = df['p-value'].values
#     y1 = df['SAP_precision'].values
#     y2 = df['SAP_recall'].values
#     y3 = df['SAP_f1'].values
#     y4 = df['Ours_precision'].values
#     y5 = df['Ours_recall'].values
#     y6 = df['Ours_f1'].values
#
#     #设置画布大小以及x轴和y轴
#     # fig = plt.figure(figsize=(16, 5), dpi=80)
#     # ax = fig.add_axes([0.12, 0.18, 0.7, 0.9], zorder=11)
#     fig = plt.figure(figsize=(16, 4), dpi=80)
#     ax = fig.add_axes([0.12, 0.24, 0.7, 0.6], zorder=11)
#     ax.set_xticks(np.arange(0.1,0.7,0.1))
#     ax.set_xticklabels([0.1,0.2,0.3,0.4,0.5,0.6], fontdict={'horizontalalignment': 'center', 'size': 28})
#     ax.set_yticks(np.arange(0.5, 1.01, 0.1))
#     ax.set_yticklabels([0.5,0.6,0.7,0.8,0.9,1],
#                        fontdict={'horizontalalignment': 'right', 'size': 27})
#     plt.xlabel('Non-conformity Score', fontsize=28)
#     # ax.set_ylabel('SCORE', fontsize=30, weight=700)
#     # ax.set_xlim((-0.5, 16))
#     ax.set_ylim((0.49,1.01))
#
#     #画图
#     #linestyle：'-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'
#     ax.plot(x, y1, linestyle=":",linewidth=5,label='SAP_Pr',marker='^',markersize=18,color=seaborn.xkcd_rgb['warm grey'],zorder=12)
#     ax.plot(x, y2, linestyle=":", linewidth=5, label='SAP_Re', marker='p', markersize=18,
#             color=seaborn.xkcd_rgb['grey blue'], zorder=12)
#     ax.plot(x, y3, linestyle=":", linewidth=5, label='SAP_F1', marker='X', markersize=20,
#             color=seaborn.xkcd_rgb['dirty pink'], zorder=12)
#     ax.plot(x, y4, linestyle="-",linewidth=5, label='GitHub_Pr', marker='$o$', markersize=22,color=seaborn.xkcd_rgb['wisteria'],zorder=12)
#     ax.plot(x, y5, linestyle="-",linewidth=5, label='GitHub_Re', marker='*', markersize=22,color=seaborn.xkcd_rgb['tan'],zorder=12)
#     ax.plot(x, y6, linestyle="-", linewidth=5, label='GitHub_F1', marker='D', markersize=14, color=seaborn.xkcd_rgb['flat green'],zorder=12)
#     # ax.plot(x, y1, linestyle=":", linewidth=5, label='SAP_Precision', marker='^', markersize=18,
#     #         color=seaborn.xkcd_rgb['pale purple'])
#     # ax.plot(x, y4, linestyle="-", linewidth=5, label='Ours_Precision', marker='X', markersize=18,
#     #         color=seaborn.xkcd_rgb['grey blue'])
#     # ax.plot(x, y2, linestyle=":", linewidth=5, label='SAP_Recall', marker='p', markersize=18,
#     #         color=seaborn.xkcd_rgb['warm grey'])
#     # ax.plot(x, y5, linestyle="-", linewidth=5, label='Ours_Recall', marker='$o$', markersize=19,
#     #         color=seaborn.xkcd_rgb['tan'])
#     # ax.plot(x, y3, linestyle=":", linewidth=5, label='SAP_F1', marker='*', markersize=22,
#     #         color=seaborn.xkcd_rgb['dirty pink'])
#     # ax.plot(x, y6, linestyle="-", linewidth=5, label='Ours_F1', marker='D', markersize=14,
#     #         color=seaborn.xkcd_rgb['grey green'])
#
#     # 设置图例
#     font = {'family': 'Times New Roman',
#             'weight': 'normal',
#             'size': 22       }
#     # plt.legend(loc='lower left', prop=font)
#     # plt.grid(axis="y",alpha=0.8, linestyle=':')
#
#     box = ax.get_position()
#     ax.set_position([box.x0, box.y0, box.width, box.height * 0.8])
#     #0.22
#     # ax.legend(loc='center left', bbox_to_anchor=(0.22, 0.20), ncol=2, prop=font,columnspacing=0.8)
#     ax.legend(loc='center left', bbox_to_anchor=(-0.07, 1.16), ncol=6, prop=font,columnspacing=1,handletextpad=0.1,handlelength=1.2)
#     plt.grid(axis="y", alpha=0.8, linestyle=':')
#
#     # 可以保存为svg这种矢量图片的格式,放大不会有锯齿
#     plt.savefig(str(name) + '.pdf')
#
#     # 对保存的图片进行显示
#     plt.show()
#
# def linechart1(path,name):
#     data = pd.read_csv(path,error_bad_lines=False)
#     f1 = data.loc[0]
#     t1 = data.loc[1]
#     f2 = data.loc[2]
#     t2 = data.loc[3]
#     f3 = data.loc[4]
#     t3 = data.loc[5]
#     f4 = data.loc[6]
#     t4 = data.loc[7]
#     f5 = data.loc[8]
#     t5 = data.loc[9]
#     f6 = data.loc[10]
#     t6 = data.loc[11]
#     # p7 = data.loc[12]
#     # r7 = data.loc[13]
#
#     # fig = plt.figure(figsize=(16, 6.5), dpi=80)
#     # ax = fig.add_axes([0.1, 0.15, 0.8, 0.8], zorder=11)
#     fig = plt.figure(figsize=(10, 3), dpi=80)
#     ax = fig.add_axes([0.15, 0.25, 0.7, 0.5], zorder=11)
#
#     plt.gca().invert_xaxis()
#     ax.set_xticks(np.arange(0, 1.01, 0.2))
#     ax.set_xticklabels([0, 0.2, 0.4, 0.6, 0.8, 1],
#                        fontdict={'horizontalalignment': 'center', 'size': 15})
#     ax.set_yticks(np.arange(0, 1.02, 0.2))
#     ax.set_yticklabels([0,0.2,0.4,0.6,0.8,1],
#                        fontdict={'horizontalalignment': 'right', 'size': 15})
#     ax.set_xlabel('FPR:24', fontsize=18)
#     ax.set_ylabel('Recall', fontsize=18)
#
#     ax.plot(f1, t1, linestyle="-.", linewidth=3, alpha=0.9, label='FUND', color=seaborn.xkcd_rgb['muddy yellow'],
#             zorder=12)
#     ax.plot(f2,t2, linestyle="-",linewidth=3, alpha=0.9,label='SABETTA et al.',color=seaborn.xkcd_rgb['dark brown'],zorder=12)
#     ax.plot(f3,t3, linestyle="--",marker='.',markersize=10,linewidth=3, alpha=0.9,label='ZHOU et al.',color=seaborn.xkcd_rgb['lighter purple'],zorder=12)
#     ax.plot(f4,t4, linestyle="--",linewidth=3, alpha=0.9,label='VCCFINDER',color=seaborn.xkcd_rgb['apple'],zorder=12)
#     ax.plot(f5, t5, linestyle=":", linewidth=3,alpha=0.9, label='ZvD', color=seaborn.xkcd_rgb['water blue'],zorder=12)
#     ax.plot(f6, t6, linestyle=(45, (6, 3)), linewidth=3, alpha=0.9, label='VULPECKER',
#             color=seaborn.xkcd_rgb['orange pink'], zorder=12)
#
#     # ax.plot(p7, r7,linestyle="-.",  linewidth=3,alpha=0.9, label='Ⅶ ',color=seaborn.xkcd_rgb['cherry'])
#
#     # 设置图例
#     font = {'family': 'Times New Roman',
#             'weight': 'light',
#             'size': 13
#             }
#     #18
#     # plt.legend(loc='upper left', prop=font)
#
#     box = ax.get_position()
#     ax.set_position([box.x0, box.y0, box.width, box.height * 0.8])
#     ax.legend(loc='center left', bbox_to_anchor=(-0.12, 1.15), ncol=6, prop=font,columnspacing=1,handletextpad=0.1,handlelength=1)
#     # ax.legend(loc='center left', bbox_to_anchor=(0.59, 0.24), ncol=2, prop=font,columnspacing=0)
#
#     plt.grid(axis="y", alpha=0.8, linestyle=':')
#
#     plt.savefig(str(name) + '.pdf')
#     plt.show()
#
# def linechart4(path,name):
#     data = pd.read_csv(path,error_bad_lines=False)
#     p1 = data.loc[0]
#     r1 = data.loc[1]
#     p2 = data.loc[2]
#     r2 = data.loc[3]
#     p3 = data.loc[4]
#     r3 = data.loc[5]
#     p4 = data.loc[6]
#     r4 = data.loc[7]
#     p5 = data.loc[8]
#     r5 = data.loc[9]
#     p6 = data.loc[10]
#     r6 = data.loc[11]
#     p7 = data.loc[12]
#     r7 = data.loc[13]
#
#     # fig = plt.figure(figsize=(16, 5), dpi=80)
#     # ax = fig.add_axes([0.12, 0.22, 0.69, 0.9], zorder=11)
#     fig = plt.figure(figsize=(16, 4), dpi=80)
#     ax = fig.add_axes([0.12, 0.24, 0.7, 0.8], zorder=11)
#     plt.gca().invert_xaxis()
#     ax.set_xticks(np.arange(0, 1.01, 0.2))
#     ax.set_xticklabels([0, 0.2, 0.4, 0.6, 0.8, 1],
#                        fontdict={'horizontalalignment': 'center', 'size': 28})
#     ax.set_yticks(np.arange(0.5, 1.02, 0.1))
#     ax.set_yticklabels([0.5,0.6,0.7,0.8,0.9,1],
#                        fontdict={'horizontalalignment': 'right', 'size': 28})
#     ax.set_xlabel('Recall', fontsize=30)
#     ax.set_ylabel('Precision', fontsize=30)
#
#     ax.plot(r1,p1,linestyle="-",linewidth=3,alpha=0.9, label='LR',color=seaborn.xkcd_rgb['orange pink'],zorder=12)
#     ax.plot(r2,p2, linestyle=":", marker='.',markersize=10,linewidth=3, alpha=0.9,label='RF',color=seaborn.xkcd_rgb['dark brown'],zorder=12)
#     ax.plot(r3,p3, linestyle=':',linewidth=3, alpha=0.9,label='GB',color=seaborn.xkcd_rgb['lighter purple'],zorder=12)
#     ax.plot(r4,p4, linestyle="--",  linewidth=3, alpha=0.9,label='SVM',color=seaborn.xkcd_rgb['apple'],zorder=12)
#     ax.plot(r5, p5, linestyle=":", marker='$o$',markersize=10,linewidth=3,alpha=0.9, label='KNN', color=seaborn.xkcd_rgb['water blue'],zorder=12)
#     ax.plot(r6, p6, linestyle=(45,(10,5)), linewidth=3,alpha=0.9, label='Ada', color=seaborn.xkcd_rgb['muddy yellow'],zorder=12)
#     ax.plot(r7, p7,linestyle="-.",  linewidth=3,alpha=0.9, label='FENCED',color=seaborn.xkcd_rgb['cherry'],zorder=12)
#
#     # 设置图例
#     font = {'family': 'Times New Roman',
#             'weight': 'light',
#             'size': 21.8,
#             }
#     box = ax.get_position()
#     ax.set_position([box.x0, box.y0, box.width, box.height * 0.8])
#     ax.legend(loc='center left', bbox_to_anchor=(0.65, 0.352), ncol=2, prop=font,columnspacing=1,handletextpad=0.1,handlelength=2)
#     # ax.legend(loc='lower right', ncol=2, prop=font)
#
#     plt.grid(axis="y", alpha=0.8, linestyle=':')
#
#     plt.savefig(str(name) + '.pdf')
#     plt.show()
#
# def linchart3_1(path,name):
# #读取数据
#     df = pd.read_excel(path)
#     x = df['model'].values
#     y1 = df['precision'].values
#     y2 = df['fpr'].values
#
#     #设置画布大小以及x轴和y轴
#     fig = plt.figure(figsize=(16,6.5),dpi=80)
#     ax = fig.add_axes([0.1, 0.27, 0.8, 0.8],zorder=11)
#     ax.set_xticks(np.arange(0, 7))
#     ax.set_xticklabels(x, fontdict={'horizontalalignment': 'center', 'size': 25,'rotation':15})
#     ax.set_yticks(np.arange(0, 1.02, 0.2))
#     ax.set_yticklabels([0, 0.2, 0.4,0.6,0.8,1],
#                        fontdict={'horizontalalignment': 'right', 'size': 30})
#     plt.xlabel('SAP dataset', fontsize=30, weight=700)
#     # ax.set_ylabel('SCORE', fontsize=30, weight=700)
#     # ax.set_xlim((-0.5, 6))
#     ax.set_ylim((0,1.02))
#
#     ax.plot(x, y1, linestyle=":", linewidth=5, label='Precision', marker='^', markersize=18,
#             color=seaborn.xkcd_rgb['grey blue'])
#     ax.plot(x, y2, linestyle="-", linewidth=5, label='FPR', marker='$o$', markersize=22,
#             color=seaborn.xkcd_rgb['flat green'])
#
#     # for a, b in zip(x, y1):
#     #     #显示数字标签为百分数
#     #     plt.text(a, b, '%.0f%%' % (b * 100), ha='center', va='bottom', fontsize=25,weight=700)      #ha为水平位置，va为垂直位置
#     # for a, b in zip(x, y2):
#     #     plt.text(a, b, '%.0f%%' % (b * 100), ha='center', va='bottom', fontsize=25,weight=700)
#
#     # 设置图例
#     font = {'family': 'Times New Roman',
#             'weight': 'normal',
#             'size': 32,
#             }
#     # plt.legend(loc='lower left', prop=font)
#     # plt.grid(axis="y",alpha=0.8, linestyle=':')
#
#     box = ax.get_position()
#     ax.set_position([box.x0, box.y0, box.width, box.height * 0.8])
#     ax.legend(loc='center left', bbox_to_anchor=(0.23, 0.85), ncol=2, prop=font)
#     plt.grid(axis="y", alpha=0.8, linestyle=':')
#
#     # 可以保存为svg这种矢量图片的格式,放大不会有锯齿
#     plt.savefig(str(name) + '.pdf')
#
#     # 对保存的图片进行显示
#     plt.show()
#
# #修改了图例的位置
# def linchart3_2(path,name):
# #读取数据
#     df = pd.read_excel(path)
#     x = df['model'].values
#     y1 = df['precision'].values
#     y2 = df['fpr'].values
#
#     #设置画布大小以及x轴和y轴
#     fig = plt.figure(figsize=(16,6.5),dpi=80)
#     ax = fig.add_axes([0.1, 0.27, 0.8, 0.8],zorder=11)
#     ax.set_xticks(np.arange(0, 7))
#     ax.set_xticklabels(x, fontdict={'horizontalalignment': 'center', 'size': 25, 'weight': 600,'rotation':15})
#     ax.set_yticks(np.arange(0, 1.02, 0.2))
#     ax.set_yticklabels([0, 0.2, 0.4,0.6,0.8,1],
#                        fontdict={'horizontalalignment': 'right', 'size': 30, 'weight': 700})
#     plt.xlabel('GitHub dataset', fontsize=30, weight=700)
#     # ax.set_ylabel('SCORE', fontsize=30, weight=700)
#     # ax.set_xlim((-0.5, 6))
#     ax.set_ylim((0,1.02))
#
#     ax.plot(x, y1, linestyle=":", linewidth=5, label='Precision', marker='^', markersize=18,
#             color=seaborn.xkcd_rgb['grey blue'])
#     ax.plot(x, y2, linestyle="-", linewidth=5, label='FPR', marker='$o$', markersize=22,
#             color=seaborn.xkcd_rgb['flat green'])
#
#     # for a, b in zip(x, y1):
#     #     #显示数字标签为百分数
#     #     plt.text(a, b, '%.0f%%' % (b * 100), ha='center', va='bottom', fontsize=25,weight=700)      #ha为水平位置，va为垂直位置
#     # for a, b in zip(x, y2):
#     #     plt.text(a, b, '%.0f%%' % (b * 100), ha='center', va='bottom', fontsize=25,weight=700)
#
#     # 设置图例
#     font = {'family': 'Times New Roman',
#             'weight': 'normal',
#             'size': 40,
#             }
#     # plt.legend(loc='best', prop=font)
#     # plt.grid(axis="y",alpha=0.8, linestyle=':')
#
#     box = ax.get_position()
#     ax.set_position([box.x0, box.y0, box.width, box.height * 0.8])
#     ax.legend(loc='center left', bbox_to_anchor=(0.62, 0.5), ncol=1, prop=font)
#     plt.grid(axis="y", alpha=0.8, linestyle=':')
#
#     # 可以保存为svg这种矢量图片的格式,放大不会有锯齿
#     plt.savefig(str(name) + '.pdf')
#
#     # 对保存的图片进行显示
#     plt.show()
#
# def linchart3_3(path,name):
# #读取数据
#     df = pd.read_excel(path)
#     x = df['model'].values
#     y1 = df['precision'].values
#     y2 = df['fpr'].values
#
#     #设置画布大小以及x轴和y轴
#     fig = plt.figure(figsize=(16,6.5),dpi=80)
#     ax = fig.add_axes([0.1, 0.27, 0.8, 0.8],zorder=11)
#     ax.set_xticks(np.arange(0, 7))
#     ax.set_xticklabels(x, fontdict={'horizontalalignment': 'center', 'size': 25, 'weight': 600,'rotation':15})
#     ax.set_yticks(np.arange(0, 1.02, 0.2))
#     ax.set_yticklabels([0, 0.2, 0.4,0.6,0.8,1],
#                        fontdict={'horizontalalignment': 'right', 'size': 30, 'weight': 700})
#     plt.xlabel('ZvD dataset', fontsize=30, weight=700)
#     # ax.set_ylabel('SCORE', fontsize=30, weight=700)
#     # ax.set_xlim((-0.5, 6))
#     ax.set_ylim((0,1.02))
#
#     ax.plot(x, y1, linestyle=":", linewidth=5, label='Precision', marker='^', markersize=18,
#             color=seaborn.xkcd_rgb['grey blue'])
#     ax.plot(x, y2, linestyle="-", linewidth=5, label='FPR', marker='$o$', markersize=22,
#             color=seaborn.xkcd_rgb['flat green'])
#
#     # for a, b in zip(x, y1):
#     #     #显示数字标签为百分数
#     #     plt.text(a, b, '%.0f%%' % (b * 100), ha='center', va='bottom', fontsize=25,weight=700)      #ha为水平位置，va为垂直位置
#     # for a, b in zip(x, y2):
#     #     plt.text(a, b, '%.0f%%' % (b * 100), ha='center', va='bottom', fontsize=25,weight=700)
#
#     # 设置图例
#     font = {'family': 'Times New Roman',
#             'weight': 'normal',
#             'size': 32,
#             }
#     # plt.legend(loc='lower left', prop=font)
#     # plt.grid(axis="y",alpha=0.8, linestyle=':')
#
#     box = ax.get_position()
#     ax.set_position([box.x0, box.y0, box.width, box.height * 0.8])
#     ax.legend(loc='center left', bbox_to_anchor=(0.23, 0.85), ncol=2, prop=font)
#     plt.grid(axis="y", alpha=0.8, linestyle=':')
#
#     # 可以保存为svg这种矢量图片的格式,放大不会有锯齿
#     plt.savefig(str(name) + '.pdf')
#
#     # 对保存的图片进行显示
#     plt.show()
#
# def roc1(path,name):
#     data = pd.read_csv(path, error_bad_lines=False)
#     f1 = data.loc[0]
#     t1 = data.loc[1]
#     f2 = data.loc[2]
#     t2 = data.loc[3]
#     f3 = data.loc[4]
#     t3 = data.loc[5]
#     f4 = data.loc[6]
#     t4 = data.loc[7]
#     f5 = data.loc[8]
#     t5 = data.loc[9]
#     f6 = data.loc[10]
#     t6 = data.loc[11]
#
#     roc_auc1 = auc(f1, t1)  ###计算auc的值
#     roc_auc2 = auc(f2, t2)  ###计算auc的值
#     roc_auc3 = auc(f3, t3)  ###计算auc的值
#     roc_auc4 = auc(f4, t4)  ###计算auc的值
#     roc_auc5 = auc(f5, t5)  ###计算auc的值
#     roc_auc6 = auc(f6, t6)  ###计算auc的值
#
#     fig = plt.figure(figsize=(6, 6), dpi=80)
#     ax = fig.add_axes([0.2, 0.15, 0.7, 0.7], zorder=11)
#
#     ax.set_xticks(np.arange(0, 1.01, 0.2))
#     ax.set_xticklabels([0, 0.2, 0.4, 0.6, 0.8, 1],
#                        fontdict={'horizontalalignment': 'center', 'size': 25})
#     ax.set_yticks(np.arange(0, 1.02, 0.2))
#     ax.set_yticklabels([0, 0.2, 0.4, 0.6, 0.8, 1],
#                        fontdict={'horizontalalignment': 'right', 'size': 25})
#     ax.set_xlabel('FPR', fontsize=30)
#     ax.set_ylabel('TPR', fontsize=30)
#
#     # lw = 2
#     # ax.plot(f1, t1, lw=lw, label='FUNDED')
#     # ax.plot(f2, t2, lw=lw, label='SABETTA et al.')
#     # ax.plot(f3, t3, lw=lw, label='ZHOU et al.')
#     # ax.plot(f4, t4, lw=lw, label='VCCFINDER')
#     # ax.plot(f5, t5, lw=lw, label='ZvD' )
#     # ax.plot(f6, t6, lw=lw, label='VULPECKER')
#     # ax.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
#
#     ax.plot(f1, t1, linestyle=":", marker='.',markersize=5, linewidth=3, alpha=0.9, label='FUNDED', color=seaborn.xkcd_rgb['orange pink'], zorder=12)
#     ax.plot(f2, t2,  linestyle="-", markersize=10, linewidth=3, alpha=0.9, label='SABETTA et al.',
#             color=seaborn.xkcd_rgb['dark brown'], zorder=12)
#     ax.plot(f3, t3, linestyle="-.", linewidth=3, alpha=0.9, label='ZHOU et al.', color=seaborn.xkcd_rgb['lighter purple'],
#             zorder=12)
#     ax.plot(f4, t4, linestyle="--", linewidth=3, alpha=0.9, label='VCCFINDER', color=seaborn.xkcd_rgb['apple'], zorder=12)
#     ax.plot(f5, t5, linestyle=(50, (8, 4)), markersize=10, linewidth=3, alpha=0.9, label='ZvD',
#             color=seaborn.xkcd_rgb['water blue'], zorder=12)
#     ax.plot(f6, t6,  linestyle=':',linewidth=3, alpha=0.9, label='VULPECKER',
#             color=seaborn.xkcd_rgb['muddy yellow'], zorder=12)
#     ax.plot([0, 1], [0, 1], linestyle=":", marker='$o$', linewidth=3, alpha=0.9, color=seaborn.xkcd_rgb['cherry'], zorder=12)
#
#
#     # 设置图例
#     font = {'family': 'Times New Roman',
#             'weight': 'light',
#             'size': 16
#             }
#     # 18
#     plt.legend(loc='lower right', prop=font)
#
#     # box = ax.get_position()
#     # ax.set_position([box.x0, box.y0, box.width, box.height * 0.8])
#     # ax.legend(loc='center left', bbox_to_anchor=(-0.12, 1.15), ncol=6, prop=font, columnspacing=1, handletextpad=0.1,
#     #           handlelength=1)
#     # ax.legend(loc='center left', bbox_to_anchor=(0.59, 0.24), ncol=2, prop=font,columnspacing=0)
#
#     plt.grid(axis="y", alpha=0.8, linestyle=':')
#
#     plt.savefig(str(name) + '.pdf')
#
#     plt.show()
#
# def roc10(path,name):
#     data = pd.read_csv(path, error_bad_lines=False)
#     f1 = data.loc[0]
#     t1 = data.loc[1]
#     f2 = data.loc[2]
#     t2 = data.loc[3]
#     f3 = data.loc[4]
#     t3 = data.loc[5]
#     f4 = data.loc[6]
#     t4 = data.loc[7]
#     f5 = data.loc[8]
#     t5 = data.loc[9]
#     f6 = data.loc[10]
#     t6 = data.loc[11]
#
#     f1=np.array(f1)
#     t1=np.array(t1)
#
#     roc_auc1 = auc(f1, t1)  ###计算auc的值
#     roc_auc2 = auc(f2, t2)  ###计算auc的值
#     roc_auc3 = auc(f3, t3)  ###计算auc的值
#     roc_auc4 = auc(f4, t4)  ###计算auc的值
#     roc_auc5 = auc(f5, t5)  ###计算auc的值
#     roc_auc6 = auc(f6, t6)  ###计算auc的值
#
#     fig = plt.figure(figsize=(6, 6), dpi=80)
#     ax = fig.add_axes([0.2, 0.15, 0.7, 0.7], zorder=11)
#
#     ax.set_xticks(np.arange(0, 1.01, 0.2))
#     ax.set_xticklabels([0, 0.2, 0.4, 0.6, 0.8, 1],
#                        fontdict={'horizontalalignment': 'center', 'size': 25})
#     ax.set_yticks(np.arange(0, 1.02, 0.2))
#     ax.set_yticklabels([0, 0.2, 0.4, 0.6, 0.8, 1],
#                        fontdict={'horizontalalignment': 'right', 'size': 25})
#     ax.set_xlabel('FPR', fontsize=30)
#     ax.set_ylabel('TPR', fontsize=30)
#
#     # lw = 2
#
#     # ax.plot(f1, t1, lw=lw, label='FUNDED',linestyle="-")
#     # ax.plot(f2, t2, lw=lw, label='LR', linestyle=":")
#     # ax.plot(f3, t3, lw=lw, label='RF',linestyle="--")
#     # ax.plot(f4, t4, lw=lw, label='GB',linestyle=":")
#     # ax.plot(f5, t5, lw=lw, label='SVM' )
#     # ax.plot(f6, t6, lw=lw, label='KNN')
#     # ax.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
#
#     ax.plot(f1, t1, linestyle=":", marker='.',linewidth=3, alpha=0.9, label='FUNDED', color=seaborn.xkcd_rgb['orange pink'], zorder=12)
#     ax.plot(f2, t2,  linestyle="-", markersize=10, linewidth=3, alpha=0.9, label='LR',
#             color=seaborn.xkcd_rgb['dark brown'], zorder=12)
#     ax.plot(f3, t3, linestyle=':', linewidth=3, alpha=0.9, label='RF', color=seaborn.xkcd_rgb['lighter purple'],
#             zorder=12)
#     ax.plot(f4, t4, linestyle="--", linewidth=3, alpha=0.9, label='GB', color=seaborn.xkcd_rgb['apple'], zorder=12)
#     ax.plot(f5, t5, linestyle=(50, (7, 5)), markersize=10, linewidth=3, alpha=0.9, label='SVM',
#             color=seaborn.xkcd_rgb['water blue'], zorder=12)
#     ax.plot(f6, t6, linestyle=":", marker='$o$', linewidth=3, alpha=0.9, label='KNN',
#             color=seaborn.xkcd_rgb['muddy yellow'], zorder=12)
#     ax.plot([0, 1], [0, 1], linestyle="-.", linewidth=3, alpha=0.9, color=seaborn.xkcd_rgb['cherry'], zorder=12)
#
#
#     # 设置图例
#     font = {'family': 'Times New Roman',
#             'weight': 'light',
#             'size': 18
#             }
#     # 18
#     plt.legend(loc='lower right', prop=font)
#
#     # box = ax.get_position()
#     # ax.set_position([box.x0, box.y0, box.width, box.height * 0.8])
#     # ax.legend(loc='center left', bbox_to_anchor=(-0.12, 1.15), ncol=6, prop=font, columnspacing=1, handletextpad=0.1,
#     #           handlelength=1)
#     # ax.legend(loc='center left', bbox_to_anchor=(0.59, 0.24), ncol=2, prop=font,columnspacing=0)
#
#     plt.grid(axis="y", alpha=0.8, linestyle=':')
#
#     plt.savefig(str(name) + '.pdf')
#
#     plt.show()
#
# def sard_code(path,name):
# #读取数据
#     df = pd.read_excel(path)
#     x = df['x'].values
#     y = df['y'].values
#
#     #设置画布大小以及x轴和y轴
#     fig = plt.figure(figsize=(8,4),dpi=80)
#     ax = fig.add_axes([0.2, 0.25, 0.6, 0.6],zorder=11)
#     ax.set_xticks(np.arange(0,301,50))
#     ax.set_xticklabels(np.arange(0,301,50), fontdict={'horizontalalignment': 'center', 'size': 22})
#     ax.set_yticks(np.arange(0, 1.02, 0.2))
#     ax.set_yticklabels([0, 0.2, 0.4,0.6,0.8,1],
#                        fontdict={'horizontalalignment': 'right', 'size': 22})
#     ax.set_xlabel('code_num', fontsize=24)
#     ax.set_ylabel('CDF', fontsize=24)
#     # ax.set_xlim((0, 300))
#     ax.set_ylim((0,1.02))
#
#     ax.plot(x, y, linestyle="-",linewidth=3,color=seaborn.xkcd_rgb['grey blue'])
#
#     plt.grid(axis="y", alpha=0.8, linestyle=':')
#
#     # 可以保存为svg这种矢量图片的格式,放大不会有锯齿
#     plt.savefig(str(name) + '.pdf')
#
#     # 对保存的图片进行显示
#     plt.show()
#
# def sard_node(path,name):
# #读取数据
#     df = pd.read_excel(path)
#     x = df['x'].values
#     y = df['y'].values
#
#     #设置画布大小以及x轴和y轴
#     fig = plt.figure(figsize=(8,4),dpi=80)
#     ax = fig.add_axes([0.2, 0.25, 0.6, 0.6],zorder=11)
#     ax.set_xticks(np.arange(0,1300,200))
#     ax.set_xticklabels(np.arange(0,1300,200), fontdict={'horizontalalignment': 'center', 'size': 18})
#     ax.set_yticks(np.arange(0, 1.02, 0.2))
#     ax.set_yticklabels([0, 0.2, 0.4,0.6,0.8,1],
#                        fontdict={'horizontalalignment': 'right', 'size': 22})
#     ax.set_xlabel('node_num', fontsize=24)
#     ax.set_ylabel('CDF', fontsize=24)
#     # ax.set_xlim((0, 300))
#     ax.set_ylim((0,1.02))
#
#     ax.plot(x, y, linestyle="-",linewidth=3,color=seaborn.xkcd_rgb['grey blue'])
#
#     plt.grid(axis="y", alpha=0.8, linestyle=':')
#
#     # 可以保存为svg这种矢量图片的格式,放大不会有锯齿
#     plt.savefig(str(name) + '.pdf')
#
#     # 对保存的图片进行显示
#     plt.show()
#
# def github_code(path,name):
# #读取数据
#     df = pd.read_excel(path)
#     x = df['x'].values
#     y = df['y'].values
#
#     #设置画布大小以及x轴和y轴
#     fig = plt.figure(figsize=(8,4),dpi=80)
#     ax = fig.add_axes([0.2, 0.25, 0.6, 0.6],zorder=11)
#     ax.set_xticks(np.arange(0,2050,500))
#     ax.set_xticklabels(np.arange(0,2050,500), fontdict={'horizontalalignment': 'center', 'size': 20})
#     ax.set_yticks(np.arange(0, 1.02, 0.2))
#     ax.set_yticklabels([0, 0.2, 0.4,0.6,0.8,1],
#                        fontdict={'horizontalalignment': 'right', 'size': 20})
#     ax.set_xlabel('code_num', fontsize=22)
#     ax.set_ylabel('CDF', fontsize=22)
#     ax.set_xlim((0, 2050))
#     ax.set_ylim((0,1.02))
#
#     ax.plot(x, y, linestyle="-",linewidth=3,color=seaborn.xkcd_rgb['grey blue'])
#
#     plt.grid(axis="y", alpha=0.8, linestyle=':')
#
#     # 可以保存为svg这种矢量图片的格式,放大不会有锯齿
#     plt.savefig(str(name) + '.pdf')
#
#     # 对保存的图片进行显示
#     plt.show()
#
# def github_node(path,name):
# #读取数据
#     df = pd.read_excel(path)
#     x = df['x'].values
#     y = df['y'].values
#
#     #设置画布大小以及x轴和y轴
#     fig = plt.figure(figsize=(8,4),dpi=80)
#     ax = fig.add_axes([0.2, 0.3, 0.6, 0.6],zorder=11)
#     ax.set_xticks(np.arange(0, 6050,1000))
#     ax.set_xticklabels(np.arange(0, 6050,1000), fontdict={'horizontalalignment': 'center', 'size': 20})
#     ax.set_yticks(np.arange(0, 1.02, 0.2))
#     ax.set_yticklabels([0, 0.2, 0.4,0.6,0.8,1],
#                        fontdict={'horizontalalignment': 'right', 'size': 20})
#     ax.set_xlabel('node_num', fontsize=22)
#     ax.set_ylabel('CDF', fontsize=22)
#     ax.set_xlim((0, 6050))
#     ax.set_ylim((0,1.02))
#
#     ax.plot(x, y, linestyle="-",linewidth=3,color=seaborn.xkcd_rgb['grey blue'])
#
#     plt.grid(axis="y", alpha=0.8, linestyle=':')
#
#     # 可以保存为svg这种矢量图片的格式,放大不会有锯齿
#     plt.savefig(str(name) + '.pdf')
#
#     # 对保存的图片进行显示
#     plt.show()

#带箭头的不同分类方法的ROC图
def roc11(path,name):
    #读取数据
    data = pd.read_csv(path, error_bad_lines=False)
    f1 = data.loc[0]
    t1 = data.loc[1]
    f2 = data.loc[2]
    t2 = data.loc[3]
    f3 = data.loc[4]
    t3 = data.loc[5]
    f4 = data.loc[6]
    t4 = data.loc[7]
    f5 = data.loc[8]
    t5 = data.loc[9]
    f6 = data.loc[10]
    t6 = data.loc[11]

    #设置图层及横纵坐标
    fig = plt.figure(figsize=(6, 6), dpi=80)
    ax = fig.add_axes([0.2, 0.15, 0.7, 0.7], zorder=11)

    ax.set_xticks(np.arange(0, 1.01, 0.2))
    ax.set_xticklabels([0, 0.2, 0.4, 0.6, 0.8, 1],
                       fontdict={'horizontalalignment': 'center', 'size': 25,'family': 'Arial'})
    ax.set_yticks(np.arange(0, 1.02, 0.2))
    ax.set_yticklabels([0, 0.2, 0.4, 0.6, 0.8, 1],
                       fontdict={'horizontalalignment': 'right', 'size': 25,'family': 'Arial'})
    ax.set_xlabel('FPR', fontsize=30,fontdict={'family': 'Arial'})
    ax.set_ylabel('TPR', fontsize=30,fontdict={'family': 'Arial'})

    ax.plot(f1, t1, linestyle=":", marker='.',markersize=5, linewidth=3, alpha=0.9, label='FUNDED', color=seaborn.xkcd_rgb['orange pink'], zorder=12)
    ax.plot(f2, t2,  linestyle="-", markersize=10, linewidth=3, alpha=0.9, label='SABETTA et al.',
            color=seaborn.xkcd_rgb['dark brown'], zorder=12)
    ax.plot(f3, t3, linestyle="-.", linewidth=3, alpha=0.9, label='ZHOU et al.', color=seaborn.xkcd_rgb['lighter purple'],
            zorder=12)
    ax.plot(f4, t4, linestyle="--", linewidth=3, alpha=0.9, label='VCCFINDER', color=seaborn.xkcd_rgb['apple'], zorder=12)
    ax.plot(f5, t5, linestyle=(50, (8, 4)), markersize=10, linewidth=3, alpha=0.9, label='ZvD',
            color=seaborn.xkcd_rgb['water blue'], zorder=12)
    ax.plot(f6, t6,  linestyle=':',linewidth=3, alpha=0.9, label='VULPECKER',
            color=seaborn.xkcd_rgb['muddy yellow'], zorder=12)
    ax.plot([0, 1], [0, 1], linestyle=":", marker='$o$', linewidth=3, alpha=0.9, color='gray', zorder=12)

    # ax.plot(f1, t1, linestyle="-",linewidth=3, alpha=0.9, label='FUNDED',
    #         color='#473192', zorder=12)
    # ax.plot(f3, t3, linestyle="-", linewidth=3, alpha=0.9, label='ZHOU et al.',
    #         color='#654ca3',
    #         zorder=12)
    # ax.plot(f2, t2, linestyle="-",  linewidth=3, alpha=0.9, label='SABETTA et al.',
    #         color='#8169b5', zorder=12)
    #
    # ax.plot(f4, t4, linestyle="-", linewidth=3, alpha=0.9, label='VCCFINDER', color='#9c86c6',
    #         zorder=12)
    # ax.plot(f5, t5, linestyle="-", markersize=10, linewidth=3, alpha=0.9, label='ZvD',
    #         color='#b7a5d8', zorder=12)
    # ax.plot(f6, t6, linestyle='-', linewidth=3, alpha=0.9, label='VULPECKER',
    #         color='#d2c4e9', zorder=12)
    # ax.plot([0, 1], [0, 1], linestyle="-",  linewidth=3, alpha=0.9, color='#ede4fb',
    #         zorder=12)

    #添加箭头
    ax.arrow(0.1, 0.9, -0.1, 0.1,length_includes_head=True, head_width=0.04, head_length=0.05 ,fc='r',
             ec='k',shape='full')
    # bbox_props = dict(boxstyle="round", fc="w", ec="0.5", alpha=0.9)
    #添加箭头的文字
    ax.text(0.22, 0.95 ,"better", ha="center", va="center", size=20,fontfamily ='Arial',
            fontsize = 25)

    # 设置图例
    font = {'family': 'Arial',
            'weight': 'light',
            'size': 16
            }
    # 18
    plt.legend(loc='lower right', prop=font)

    # box = ax.get_position()
    # ax.set_position([box.x0, box.y0, box.width, box.height * 0.8])
    # ax.legend(loc='center left', bbox_to_anchor=(-0.12, 1.15), ncol=6, prop=font, columnspacing=1, handletextpad=0.1,
    #           handlelength=1)
    # ax.legend(loc='center left', bbox_to_anchor=(0.59, 0.24), ncol=2, prop=font,columnspacing=0)

    #设置网络线
    plt.grid(axis="y", alpha=0.8, linestyle=':')

    plt.savefig(str(name) + '.pdf')

    plt.show()

#带箭头的不同模型方法的ROC图
def roc101(path,name):
    data = pd.read_csv(path, error_bad_lines=False)
    f1 = data.loc[0]
    t1 = data.loc[1]
    f2 = data.loc[2]
    t2 = data.loc[3]
    f3 = data.loc[4]
    t3 = data.loc[5]
    f4 = data.loc[6]
    t4 = data.loc[7]
    f5 = data.loc[8]
    t5 = data.loc[9]
    f6 = data.loc[10]
    t6 = data.loc[11]

    fig = plt.figure(figsize=(6, 6), dpi=80)
    ax = fig.add_axes([0.2, 0.15, 0.7, 0.7], zorder=11)

    ax.set_xticks(np.arange(0, 1.01, 0.2))
    ax.set_xticklabels([0, 0.2, 0.4, 0.6, 0.8, 1],
                       fontdict={'horizontalalignment': 'center', 'size': 25,'family': 'Arial'})
    ax.set_yticks(np.arange(0, 1.02, 0.2))
    ax.set_yticklabels([0, 0.2, 0.4, 0.6, 0.8, 1],
                       fontdict={'horizontalalignment': 'right', 'size': 25,'family': 'Arial'})
    ax.set_xlabel('FPR', fontsize=30,fontdict={'family': 'Arial'})
    ax.set_ylabel('TPR', fontsize=30,fontdict={'family': 'Arial'})

    ax.plot(f1, t1, linestyle=":", marker='.',linewidth=3, alpha=0.9, label='FUNDED', color=seaborn.xkcd_rgb['orange pink'], zorder=12)
    ax.plot(f2, t2,  linestyle="-", markersize=10, linewidth=3, alpha=0.9, label='LR',
            color=seaborn.xkcd_rgb['dark brown'], zorder=12)
    ax.plot(f3, t3, linestyle=':', linewidth=3, alpha=0.9, label='RF', color=seaborn.xkcd_rgb['lighter purple'],
            zorder=12)
    ax.plot(f4, t4, linestyle="--", linewidth=3, alpha=0.9, label='GB', color=seaborn.xkcd_rgb['apple'], zorder=12)
    ax.plot(f5, t5, linestyle=(50, (7, 5)), markersize=10, linewidth=3, alpha=0.9, label='SVM',
            color=seaborn.xkcd_rgb['water blue'], zorder=12)
    ax.plot(f6, t6, linestyle="-.", linewidth=3, alpha=0.9, label='KNN',
            color=seaborn.xkcd_rgb['muddy yellow'], zorder=12)
    ax.plot([0, 1], [0, 1], linestyle=":", marker='$o$', linewidth=3, alpha=0.9, color='gray', zorder=12)

    # ax.plot(f1, t1, linestyle="-", linewidth=3, alpha=0.9, label='FUNDED',
    #         color='#473192', zorder=12)
    #
    # ax.plot(f4, t4, linestyle="-", linewidth=3, alpha=0.9, label='GB', color='#654ca3', zorder=12)
    # ax.plot(f2, t2, linestyle="-", linewidth=3, alpha=0.9, label='LR',
    #         color='#8169b5', zorder=12)
    # ax.plot(f5, t5, linestyle="-", markersize=10, linewidth=3, alpha=0.9, label='SVM',
    #         color='#9c86c6', zorder=12)
    # ax.plot(f6, t6, linestyle="-", linewidth=3, alpha=0.9, label='KNN',
    #         color='#d2c4e9', zorder=12)
    # ax.plot([0, 1], [0, 1], linestyle="-", linewidth=3, alpha=0.9, color='#ede4fb', zorder=12)
    # ax.plot(f3, t3, linestyle='-', linewidth=3, alpha=0.9, label='RF', color='#b7a5d8',
    #         zorder=12)
    ax.arrow(0.1, 0.9, -0.1, 0.1, length_includes_head=True, head_width=0.04, head_length=0.05, fc='r',
             ec='k', shape='full')
    # bbox_props = dict(boxstyle="round", fc="w", ec="0.5", alpha=0.9)
    ax.text(0.22, 0.95, "better", ha="center", va="center", size=20, fontfamily='Arial',
            fontsize=25)

    # 设置图例
    font = {'family': 'Arial',
            'weight': 'light',
            'size': 18
            }
    # 18
    plt.legend(loc='lower right', prop=font)

    plt.grid(axis="y", alpha=0.8, linestyle=':')

    plt.savefig(str(name) + '.pdf')

    plt.show()

# def code(path,name):
# #读取数据
#     df = pd.read_excel(path)
#     x = df['x'].values
#     y = df['y'].values
#
#     #设置画布大小以及x轴和y轴
#     fig = plt.figure(figsize=(8,4),dpi=80)
#     ax = fig.add_axes([0.2, 0.25, 0.6, 0.6],zorder=11)
#     ax.set_xticks(np.arange(0,510,100))
#     ax.set_xticklabels(np.arange(0,510,100), fontdict={'horizontalalignment': 'center', 'size': 20})
#     ax.set_yticks(np.arange(0, 1.02, 0.2))
#     ax.set_yticklabels([0, 0.2, 0.4,0.6,0.8,1],
#                        fontdict={'horizontalalignment': 'right', 'size': 20})
#     ax.set_xlabel('code_num', fontsize=22)
#     ax.set_ylabel('CDF', fontsize=22)
#     ax.set_xlim((0, 510))
#     ax.set_ylim((0,1.02))
#
#     ax.plot(x, y, linestyle="-",linewidth=3,color=seaborn.xkcd_rgb['grey blue'])
#
#     plt.grid(axis="y", alpha=0.8, linestyle=':')
#
#     # 可以保存为svg这种矢量图片的格式,放大不会有锯齿
#     plt.savefig(str(name) + '.pdf')
#
#     # 对保存的图片进行显示
#     plt.show()
#
# def node(path,name):
# #读取数据
#     df = pd.read_excel(path)
#     x = df['x'].values
#     y = df['y'].values
#
#     #设置画布大小以及x轴和y轴
#     fig = plt.figure(figsize=(8,4),dpi=80)
#     ax = fig.add_axes([0.2, 0.3, 0.6, 0.6],zorder=11)
#     ax.set_xticks(np.arange(0, 2100,500))
#     ax.set_xticklabels(np.arange(0, 2100,500), fontdict={'horizontalalignment': 'center', 'size': 20})
#     ax.set_yticks(np.arange(0, 1.02, 0.2))
#     ax.set_yticklabels([0, 0.2, 0.4,0.6,0.8,1],
#                        fontdict={'horizontalalignment': 'right', 'size': 20})
#     ax.set_xlabel('node_num', fontsize=22)
#     ax.set_ylabel('CDF', fontsize=22)
#     ax.set_xlim((0, 2100))
#     ax.set_ylim((0,1.02))
#
#     ax.plot(x, y, linestyle="-",linewidth=3,color=seaborn.xkcd_rgb['grey blue'])
#
#     plt.grid(axis="y", alpha=0.8, linestyle=':')
#
#     # 可以保存为svg这种矢量图片的格式,放大不会有锯齿
#     plt.savefig(str(name) + '.pdf')
#
#     # 对保存的图片进行显示
#     plt.show()


if __name__ == '__main__':
#========================================================================
    #带箭头的不同分类方法的ROC图
    path = r"C:\Users\WHT\Desktop\不能颓鸭\gra\CCS\10roc.csv"
    roc11(path,r"CCS/5_2/Eva_roc_1")
    #带箭头的不同模型的ROC图
    path = r"C:\Users\WHT\Desktop\不能颓鸭\gra\CCS\classify3.csv"
    roc101(path, r"CCS/5_2/Eva_roc_2")