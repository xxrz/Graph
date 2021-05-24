import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn

import matplotlib
"""
此代码用于画CCS论文的柱状图
注释掉的代码部分不用管
每个方法前都写明了功能
代码具体注释可以看graphSGM函数（详细）
"""

#修改fonttype，以使生成的pdf可编辑
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42
#
#
# # =======================不同分类器的不同recall值=======================
# def graph1(path, name):
#     df = pd.read_excel(path)
#     x = df['Classifier'].values
#     y = df['Recall rate'].values
#
#     fig = plt.figure(figsize=(18, 10), dpi=80)
#     plt.xticks(np.arange(7), x, fontsize=28, weight=600)
#     plt.yticks(np.arange(0.2, 0.8, 0.1), fontsize=28, weight=600)
#     plt.xlabel('Classifier', fontsize=30, weight=700)
#     plt.ylabel('Recall rate', fontsize=30, weight=700)
#     plt.ylim((0.2, 0.8))
#
#     bar_width = 0.4
#     # color = seaborn.xkcd_rgb['pale salmon']
#     plt.bar(x, height=y, label='recall', width=bar_width, edgecolor='grey', linewidth=2,
#             color=seaborn.xkcd_rgb['light peach'])
#
#     for a, b in enumerate(y):
#         # 显示数字标签为百分数
#         plt.text(a, b, '%.0f%%' % (b * 100), ha='center', va='bottom', fontdict={'size': 30, 'weight': 600})
#
#     # font = {'family': 'Times New Roman',
#     #         'weight': 'normal',
#     #         'size': 30
#     #         }
#     # plt.legend(loc='best', prop=font)
#     plt.grid(alpha=0.8, linestyle=':')
#     plt.savefig(str(name) + '.pdf')
#
#     plt.show()
#
#
# # ================不同模型不同数据集的recall的对比1：柱状图================
# def graph(path, name):
#     df = pd.read_excel(path)
#     x = df['dataset'].values
#     y1 = df['VccF'].values
#     y2 = df['Zhou'].values
#     y3 = df['SAP'].values
#     y4 = df['Vpeker'].values
#     y5 = df['ZvD'].values
#     y6 = df['Ours'].values
#
#     plt.figure(figsize=(18, 10), dpi=80)
#     plt.xticks([0.25, 1.25, 2.25], x, fontsize=28, weight=600)
#     plt.yticks(np.arange(0, 0.9, 0.1), fontsize=28, weight=600)
#     plt.xlabel('dataset', fontsize=30, weight=700)
#     plt.ylabel('recall', fontsize=30, weight=700)
#     # plt.title('Control precision to 90%', fontsize=30,weight =700)
#     plt.ylim((0, 0.9))
#     bar_width = 0.13
#     # pale salmon apricot
#     plt.bar(x, height=y1, label='VccF', width=bar_width, edgecolor=seaborn.xkcd_rgb['grey'], linewidth=2,
#             color=seaborn.xkcd_rgb['light peach'])
#     # 将X轴数据改为使用np.arange(len(x_data))+bar_width,
#     plt.bar(x=np.arange(len(x)) + bar_width, height=y2, label='Zhou', width=bar_width,
#             edgecolor=seaborn.xkcd_rgb['grey'], linewidth=2, color=seaborn.xkcd_rgb['dark cream'])
#     # 在柱状图上显示具体数值, ha参数控制水平对齐方式, va控制垂直对齐方式
#     # pale lime
#     plt.bar(x=np.arange(len(x)) + 2 * bar_width, height=y3, label='SAP', width=bar_width,
#             edgecolor=seaborn.xkcd_rgb['grey'], linewidth=2, color=seaborn.xkcd_rgb['mint'])
#     # pale aqua,pale blue
#     plt.bar(x=np.arange(len(x)) + 3 * bar_width, height=y4, label='Vpeker', width=bar_width,
#             edgecolor=seaborn.xkcd_rgb['grey'], linewidth=2, color=seaborn.xkcd_rgb['pale blue'])
#     # pastel blue
#     plt.bar(x=np.arange(len(x)) + 4 * bar_width, height=y5, label='ZvD', width=bar_width,
#             edgecolor=seaborn.xkcd_rgb['grey'], linewidth=2, color=seaborn.xkcd_rgb['pale lilac'])
#     # pale mauve
#     plt.bar(x=np.arange(len(x)) + 5 * bar_width, height=y6, label='Ours', width=bar_width,
#             edgecolor=seaborn.xkcd_rgb['grey'], linewidth=2, color=seaborn.xkcd_rgb['pale rose'])
#
#     for a, b in enumerate(y1):
#         # 显示数字标签为百分数
#         plt.text(a, b, '%.0f%%' % (b * 100), ha='center', va='bottom',
#                  fontdict={'size': 22, 'weight': 500})  # ha为水平位置，va为垂直位置
#     for a, b in enumerate(y2):
#         plt.text(a + 0.13, b, '%.0f%%' % (b * 100), ha='center', va='bottom', fontdict={'size': 22, 'weight': 500})
#     for a, b in enumerate(y3):
#         plt.text(a + 0.26, b, '%.0f%%' % (b * 100), ha='center', va='bottom', fontdict={'size': 22, 'weight': 500})
#     for a, b in enumerate(y4):
#         plt.text(a + 0.39, b, '%.0f%%' % (b * 100), ha='center', va='bottom', fontdict={'size': 22, 'weight': 500})
#     for a, b in enumerate(y5):
#         plt.text(a + 0.52, b, '%.0f%%' % (b * 100), ha='center', va='bottom', fontdict={'size': 22, 'weight': 500})
#     for a, b in enumerate(y6):
#         plt.text(a + 0.65, b, '%.0f%%' % (b * 100), ha='center', va='bottom', fontdict={'size': 22, 'weight': 500})
#
#     # 显示图例
#     font = {'family': 'Times New Roman',
#             'weight': 'normal',
#             'size': 30
#             }
#     plt.legend(loc='best', prop=font)
#     plt.grid(alpha=0.8, linestyle=':')
#     plt.savefig(str(name) + '.pdf')
#
#     plt.show()
#
#
# # ================不同模型不同数据集的f1的对比2：柱状图================
# def graph4(path, name):
#     df = pd.read_excel(path)
#     x = df['model'].values
#     y1 = df['Their dataset'].values
#     y2 = df['Our dataset'].values
#
#     plt.figure(figsize=(18, 9), dpi=80)
#     plt.xticks(np.arange(0, 6) + 0.17, x, fontsize=30, weight=600)
#     plt.yticks(np.arange(0.2, 0.8, 0.1), fontsize=30, weight=600)
#     # plt.xlabel('model', fontsize=30, weight=700)
#     plt.ylabel('F1 SCORE', fontsize=30, weight=700)
#     plt.ylim((0.2, 0.7))
#
#     bar_width = 0.3
#     # hatch 内部填充形状{'/', '\', '|', '-', '+', 'x', 'o', 'O', '.', '*'}
#     plt.bar(x, height=y1, label='Their dataset', width=bar_width, edgecolor=seaborn.xkcd_rgb['grey green'], linewidth=2,
#             color=seaborn.xkcd_rgb['light grey green'], alpha=0.9, zorder=10, hatch='//')
#     # 将X轴数据改为使用np.arange(len(x_data))+bar_width,
#     # zorder参数越大 表示最后画上去 可以避免被覆盖
#     plt.bar(x=np.arange(len(x)) + bar_width + 0.05, height=y2, label='Our dataset', width=bar_width,
#             edgecolor=seaborn.xkcd_rgb['grey blue'], linewidth=2, color=seaborn.xkcd_rgb['light grey blue'],
#             alpha=0.9, zorder=10, hatch='')
#
#     for a, b in enumerate(y1):
#         # 显示数字标签为百分数
#         plt.text(a, b, '%.0f%%' % (b * 100), ha='center', va='bottom',
#                  fontdict={'size': 25, 'weight': 600}, zorder=10)  # ha为水平位置，va为垂直位置
#     for a, b in enumerate(y2):
#         plt.text(a + 0.36, b, '%.0f%%' % (b * 100), ha='center', va='bottom',
#                  fontdict={'size': 25, 'weight': 600}, zorder=10)
#
#     # 显示图例
#     font = {'family': 'Times New Roman',
#             'weight': 'normal',
#             'size': 28
#             }
#     plt.legend(loc='upper left', prop=font)
#     plt.grid(axis="y", alpha=0.8, linestyle=':')
#     plt.savefig(str(name) + '.pdf')
#
#     plt.show()
#
#
# # ================不同模型不同CWE类型的f1的对比==========================
# def graph9(path, name):
#     df = pd.read_excel(path)
#     x = df['CWE'].values
#     y1 = df['vuldeepecker'].values
#     y2 = df['μvuldeepecker'].values
#     y3 = df['TDSC'].values
#     y4 = df['GCN'].values
#
#     fig = plt.figure(figsize=(30, 6), dpi=80)
#     # 在bar之后添加线
#     ax = fig.add_axes([0.08, 0.3, 0.9, 0.5], zorder=11)
#     # 设置坐标轴的位置
#     # ax.spines['bottom'].set_position(('axes',0.25))
#     # ax.spines['bottom'].set_position(('data', 0))
#     # ax.spines['left'].set_position(('axes',0))
#     # ax.spines['left'].set_position(('data', 0.4))
#
#     ax.set_xticks(np.arange(0, 31) + 0.31)
#     ax.set_xticklabels(x, fontdict={'horizontalalignment': 'right', 'size': 22, 'weight': 600, 'rotation': 45})
#     ax.set_yticks(np.arange(0.4, 1.02, 0.1))
#     ax.set_yticklabels([0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1],
#                        fontdict={'horizontalalignment': 'right', 'size': 22, 'weight': 700})
#     # plt.xlabel('CWE-TYPE', fontsize=30, weight=700)
#     ax.set_ylabel('F1 SCORE', fontsize=25, weight=700)
#     ax.set_xlim((-0.5, 31))
#     ax.set_ylim((0.4, 1.02))
#     bar_width = 0.15
#
#     ax.bar(x=np.arange(len(x)), height=y1, label='vuldeepecker', width=bar_width, edgecolor=seaborn.xkcd_rgb['tan'],
#            linewidth=1,
#            color=seaborn.xkcd_rgb['yellow tan'], zorder=10, alpha=0.9, hatch="//")
#     ax.bar(x=np.arange(len(x)) + bar_width + 0.06, height=y2, label='μvuldeepecker', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey green'], linewidth=1, color=seaborn.xkcd_rgb['light grey green'], zorder=10,
#            alpha=0.9, hatch="o")
#     ax.bar(x=np.arange(len(x)) + 2 * bar_width + 0.12, height=y3, label='TDSC', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey blue'], linewidth=1, color=seaborn.xkcd_rgb['light grey blue'], zorder=10,
#            alpha=0.9, hatch="")
#     ax.bar(x=np.arange(len(x)) + 3 * bar_width + 0.18, height=y4, label='GCN', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey purple'], linewidth=1, color=seaborn.xkcd_rgb['pale purple'], zorder=10,
#            alpha=0.9, hatch="\\\\")
#     # 叠在一起的柱状图
#     # plt.bar(x, height=y3, label='GCN', width=bar_width,
#     #         edgecolor=seaborn.xkcd_rgb['grey'], linewidth=2, color='white')
#     # plt.bar(x, height=y1, label='μvuldeepecker', width=bar_width, edgecolor=seaborn.xkcd_rgb['grey'], linewidth=2,
#     #         color=seaborn.xkcd_rgb['light peach'])
#     # plt.bar(x, height=y2, label='vuldeepecker', width=bar_width,
#     #         edgecolor=seaborn.xkcd_rgb['grey'], linewidth=2, color='black')
#
#     # 水平柱状图
#     # fig = plt.figure(figsize=(10, 25), dpi=80)
#     #
#     # plt.yticks(np.arange(34), x, fontsize=16, weight=600)
#     # plt.xticks(np.arange(0.4, 1.015, 0.1), fontsize=28, weight=600)
#     # plt.xlim((0.4, 1.015))
#     # plt.ylabel('CWE-Type', fontsize=30, weight=700)
#     # plt.xlabel('f1', fontsize=30, weight=700)
#     # bar_width = 0.2
#
#     # plt.barh(y=x, width=y1,label='μvuldeepecker',height=bar_width)
#     # plt.barh(y=np.arange(len(x)) + bar_width, width=y2,label='vuldeepecker', height=bar_width)
#     # plt.barh(y=np.arange(len(x)) + 2*bar_width, width=y3, label='GCN', height=bar_width)
#     # plt.barh(y=x, width=y3, label='GCN', height=bar_width, alpha=0.7,color='white',edgecolor='black')
#     # plt.barh(y=x, width=y1, label='μvuldeepecker', height=bar_width,alpha = 0.7,color='red',edgecolor='black')
#     # plt.barh(y=x, width=y2, label='vuldeepecker', height=bar_width,alpha = 0.7,color='black',edgecolor='black')
#
#     font = {'family': 'Times New Roman',
#             'weight': 'normal',
#             'size': 22
#             }
#     box = ax.get_position()
#     ax.set_position([box.x0, box.y0, box.width, box.height * 0.8])
#     ax.legend(loc='center left', bbox_to_anchor=(0.26, 1.12), ncol=4, prop=font)
#     plt.grid(axis="y", alpha=0.8, linestyle=':')
#     plt.savefig(str(name) + '.pdf')
#
#     plt.show()
#
#
# # ===========================GCN的效果的展示=============================
# def graphGCN(path, name):
#     df = pd.read_excel(path)
#     x = df['CWE'].values
#     y1 = df['accuracy'].values
#     y2 = df['precision'].values
#     y3 = df['recall'].values
#     y4 = df['f1'].values
#     fig = plt.figure(figsize=(28, 6), dpi=80)
#     # 在bar之后添加线
#     ax = fig.add_axes([0.07, 0.3, 0.9, 0.5], zorder=11)
#
#     ax.set_xticks(np.arange(0, 31) + 0.27)
#     ax.set_xticklabels(x, fontdict={'horizontalalignment': 'right', 'size': 25, 'rotation': 45})
#     ax.set_yticks(np.arange(0.8, 1.01, 0.05))
#     ax.set_yticklabels(['80%', '85%', '90%', '95%', '100%'],
#                        fontdict={'horizontalalignment': 'right', 'size': 25})
#     # plt.xlabel('CWE-TYPE', fontsize=30, weight=700)
#     # ax.set_ylabel('SCORE', fontsize=25, weight=700)
#     ax.set_xlim((-0.5, 31))
#     ax.set_ylim((0.8, 1.01))
#     bar_width = 0.15
#
#     ax.bar(x=np.arange(len(x)), height=y1, label='Accuracy', width=bar_width, edgecolor=seaborn.xkcd_rgb['tan'],
#            linewidth=1,
#            color=seaborn.xkcd_rgb['yellow tan'], zorder=10, alpha=0.9, hatch="//")
#     ax.bar(x=np.arange(len(x)) + bar_width + 0.06, height=y2, label='Precision', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey green'], linewidth=1, color=seaborn.xkcd_rgb['light grey green'], zorder=10,
#            alpha=0.9, hatch="xx")
#     ax.bar(x=np.arange(len(x)) + 2 * bar_width + 0.12, height=y3, label='Recall', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey blue'], linewidth=1, color=seaborn.xkcd_rgb['light grey blue'], zorder=10,
#            alpha=0.9, hatch="")
#     ax.bar(x=np.arange(len(x)) + 3 * bar_width + 0.18, height=y4, label='F1 Score', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey purple'], linewidth=1, color=seaborn.xkcd_rgb['pale purple'], zorder=10,
#            alpha=0.9, hatch="\\\\")
#
#     font = {'family': 'Times New Roman',
#             'weight': 'normal',
#             'size': 27
#             }
#     # plt.legend(loc='upper left', prop=font)
#     # plt.grid(axis="y", alpha=0.8, linestyle=':')
#
#     # 图例：设置位置
#     box = ax.get_position()
#     ax.set_position([box.x0, box.y0, box.width, box.height * 0.8])
#     ax.legend(loc='center left', bbox_to_anchor=(0.25, 1.15), ncol=4, prop=font)
#     plt.grid(axis="y", alpha=0.8, linestyle=':')
#
#     plt.savefig(str(name) + '.pdf')
#     plt.show()
#
#
# ##===========================迁移：c->java============================
# def graphQY1(path, name):
#     df = pd.read_excel(path)
#     x = df['CWE'].values
#     y2 = df['vuldeepecker'].values
#     y5 = df['μvuldeepecker'].values
#     y4 = df['TDSC'].values
#     y1 = df['Vuddy'].values
#     y6 = df['GCN'].values
#     y3 = df['Namebugs'].values
#     fig = plt.figure(figsize=(20, 4), dpi=80)
#     # 在bar之后添加线
#     ax = fig.add_axes([0.12, 0.3, 0.8, 0.52], zorder=11)
#
#     ax.set_xticks(np.arange(10) + 0.33)
#     ax.set_xticklabels(x, fontdict={'horizontalalignment': 'center', 'size': 25, 'rotation': 20})
#     ax.set_yticks(np.arange(0.3, 1.015, 0.2))
#     ax.set_yticklabels(['30%', '50%', '70%', '90%'],
#                        fontdict={'horizontalalignment': 'right', 'size': 25})
#     # plt.xlabel('CWE-TYPE', fontsize=30, weight=700)
#     ax.set_ylabel('F1 SCORE', fontsize=28)
#     ax.set_xlim((-0.3, 10))
#     ax.set_ylim((0.3, 0.94))
#     bar_width = 0.1
#
#     ax.bar(x=np.arange(len(x)), height=y1, label='Vuddy', width=bar_width, edgecolor=seaborn.xkcd_rgb['tan'],
#            linewidth=1, color=seaborn.xkcd_rgb['yellow tan'], zorder=10, alpha=0.9, hatch="//")
#     ax.bar(x=np.arange(len(x)) + bar_width + 0.04, height=y2, label='Vuldeepecker', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey green'],
#            linewidth=1, color=seaborn.xkcd_rgb['light grey green'], zorder=10, alpha=0.9, hatch="||")
#     ax.bar(x=np.arange(len(x)) + 2 * bar_width + 0.08, height=y3, label='Deepbugs', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['coffee'], linewidth=1, color=seaborn.xkcd_rgb['very light brown'], zorder=10,
#            alpha=0.9, hatch="xx", align="center")
#     ax.bar(x=np.arange(len(x)) + 3 * bar_width + 0.12, height=y4, label='Lin', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey blue'], linewidth=1, color=seaborn.xkcd_rgb['light grey blue'], zorder=10,
#            alpha=0.9, hatch="")
#     ax.bar(x=np.arange(len(x)) + 4 * bar_width + 0.16, height=y5, label='μVuldeepecker', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey purple'], linewidth=1, color=seaborn.xkcd_rgb['pale purple'], zorder=10,
#            alpha=0.9, hatch="++")
#     ax.bar(x=np.arange(len(x)) + 5 * bar_width + 0.2, height=y6, label='LACUNA', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['rose'], linewidth=1, color=seaborn.xkcd_rgb['faded pink'], zorder=10,
#            alpha=0.9, hatch="\\\\")
#
#     font = {'family': 'Times New Roman',
#             'weight': 'normal',
#             'size': 23
#             }
#     # plt.legend(loc='upper left', prop=font)
#     # plt.grid(axis="y", alpha=0.8, linestyle=':')
#
#     box = ax.get_position()
#     ax.set_position([box.x0, box.y0, box.width, box.height * 0.8])
#     ax.legend(loc='center left', bbox_to_anchor=(-0.06, 1.18), ncol=6, prop=font)
#     plt.grid(axis="y", alpha=0.8, linestyle=':')
#
#     plt.savefig(str(name) + '.pdf')
#
#     plt.show()
#
#
# ##===========================迁移：c->swift============================
# def graphQY2(path, name):
#     df = pd.read_excel(path)
#     x = df['CWE'].values
#     y2 = df['vuldeepecker'].values
#     y3 = df['μvuldeepecker'].values
#     y5 = df['TDSC'].values
#     y1 = df['Vuddy'].values
#     y6 = df['GCN'].values
#     y4 = df['Namebugs'].values
#
#     fig = plt.figure(figsize=(15, 3), dpi=80)
#     # 在bar之后添加线
#     ax = fig.add_axes([0.13, 0.3, 0.8, 0.6], zorder=12)
#
#     ax.set_xticks(np.arange(5) + 0.32)
#     ax.set_xticklabels(x, fontdict={'horizontalalignment': 'center', 'size': 23, 'rotation': 15})
#     ax.set_yticks(np.arange(0.4, 0.85, 0.1))
#     ax.set_yticklabels(['40%', '50%', '60%', '70%', '80%'],
#                        fontdict={'horizontalalignment': 'right', 'size': 23})
#     # plt.xlabel('CWE-TYPE', fontsize=30, weight=700)
#     ax.set_ylabel('F1 SCORE', fontsize=25)
#     ax.set_ylim((0.4, 0.85))
#
#     bar_width = 0.1
#     # ax.bar(x=np.arange(len(x)), height=y1, label='Vuddy', width=bar_width, edgecolor=seaborn.xkcd_rgb['tan'],
#     #        linewidth=1, color=seaborn.xkcd_rgb['yellow tan'], zorder=10, alpha=0.9, hatch="//")
#     # ax.bar(x=np.arange(len(x)) + bar_width + 0.04, height=y2, label='Vuldeepecker', width=bar_width,
#     #        edgecolor=seaborn.xkcd_rgb['grey green'],
#     #        linewidth=1, color=seaborn.xkcd_rgb['light grey green'], zorder=10, alpha=0.9, hatch="||")
#     # ax.bar(x=np.arange(len(x)) + 2 * bar_width + 0.08, height=y3, label='μVuldeepecker', width=bar_width,
#     #        edgecolor=seaborn.xkcd_rgb['coffee'], linewidth=1, color=seaborn.xkcd_rgb['very light brown'], zorder=10,
#     #        alpha=0.9, hatch="xx", align="center")
#     # ax.bar(x=np.arange(len(x)) + 3 * bar_width + 0.12, height=y4, label='Deepbugs', width=bar_width,
#     #        edgecolor=seaborn.xkcd_rgb['grey blue'], linewidth=1, color=seaborn.xkcd_rgb['light grey blue'], zorder=10,
#     #        alpha=0.9, hatch="")
#     # ax.bar(x=np.arange(len(x)) + 4 * bar_width + 0.16, height=y5, label='Lin', width=bar_width,
#     #        edgecolor=seaborn.xkcd_rgb['grey purple'], linewidth=1, color=seaborn.xkcd_rgb['pale purple'], zorder=10,
#     #        alpha=0.9, hatch="++")
#     # ax.bar(x=np.arange(len(x)) + 5 * bar_width + 0.2, height=y6, label='LACUNA', width=bar_width,
#     #        edgecolor=seaborn.xkcd_rgb['rose'], linewidth=1, color=seaborn.xkcd_rgb['faded pink'], zorder=10,
#     #        alpha=0.9, hatch="\\\\")
#
#     ax.bar(x=np.arange(len(x)), height=y1, label='Vuddy', width=bar_width, edgecolor=seaborn.xkcd_rgb['tan'],
#            linewidth=1, color=seaborn.xkcd_rgb['yellow tan'], zorder=10, alpha=0.9, hatch="//")
#     ax.bar(x=np.arange(len(x)) + bar_width + 0.04, height=y2, label='Vuldeepecker', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey green'],
#            linewidth=1, color=seaborn.xkcd_rgb['light grey green'], zorder=10, alpha=0.9, hatch="||")
#     ax.bar(x=np.arange(len(x)) + 2 * bar_width + 0.08, height=y3, label='μVuldeepecker', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey purple'], linewidth=1, color=seaborn.xkcd_rgb['pale purple'], zorder=10,
#            alpha=0.9, hatch="++")
#     ax.bar(x=np.arange(len(x)) + 3 * bar_width + 0.12, height=y4, label='Deepbugs', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['coffee'], linewidth=1, color=seaborn.xkcd_rgb['very light brown'], zorder=10,
#            alpha=0.9, hatch="xx", align="center")
#     ax.bar(x=np.arange(len(x)) + 4 * bar_width + 0.16, height=y5, label='Lin', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey blue'], linewidth=1, color=seaborn.xkcd_rgb['light grey blue'], zorder=10,
#            alpha=0.9, hatch="")
#     ax.bar(x=np.arange(len(x)) + 5 * bar_width + 0.2, height=y6, label='LACUNA', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['rose'], linewidth=1, color=seaborn.xkcd_rgb['faded pink'], zorder=10,
#            alpha=0.9, hatch="\\\\")
#
#     font = {'family': 'Times New Roman',
#             'weight': 'normal',
#             'size': 17.5
#             }
#     # plt.legend(loc='upper left', prop=font)
#     # plt.grid(axis="y", alpha=0.8, linestyle=':')
#     # plt.savefig(str(name) + '.pdf')
#
#     box = ax.get_position()
#     ax.set_position([box.x0, box.y0, box.width, box.height * 0.8])
#     ax.legend(loc='center left', bbox_to_anchor=(-0.06, 1.16), ncol=6, prop=font)
#     plt.grid(axis="y", alpha=0.8, linestyle=':')
#     plt.savefig(str(name) + '.pdf')
#
#     plt.show()
#
#
# ##===========================迁移：java->php============================
# def graphQY3(path, name):
#     df = pd.read_excel(path)
#     x = df['CWE'].values
#     y1 = df['vuldeepecker'].values
#     y2 = df['μvuldeepecker'].values
#     y3 = df['TDSC'].values
#     y4 = df['Vuddy'].values
#     y6 = df['GCN'].values
#     y5 = df['Namebugs'].values
#
#     fig = plt.figure(figsize=(15, 3), dpi=80)
#     # 在bar之后添加线
#     ax = fig.add_axes([0.13, 0.3, 0.8, 0.6], zorder=12)
#
#     ax.set_xticks(np.arange(5) + 0.32)
#     ax.set_xticklabels(x, fontdict={'horizontalalignment': 'center', 'size': 23, 'rotation': 15})
#     ax.set_yticks(np.arange(0.4, 0.902, 0.1))
#     ax.set_yticklabels(['40%', '50%', '60%', '70%', '80%', '90%'],
#                        fontdict={'horizontalalignment': 'right', 'size': 23})
#     # plt.xlabel('CWE-TYPE', fontsize=30, weight=700)
#     ax.set_ylabel('F1 SCORE', fontsize=25)
#     ax.set_ylim((0.4, 0.90))
#     bar_width = 0.1
#
#     # ax.bar(x=np.arange(len(x)), height=y1, label='Vuldeepecker', width=bar_width, edgecolor=seaborn.xkcd_rgb['tan'],
#     #        linewidth=1, color=seaborn.xkcd_rgb['yellow tan'], zorder=10, alpha=0.9, hatch="//")
#     # ax.bar(x=np.arange(len(x)) + bar_width + 0.04, height=y2, label='μVuldeepecker', width=bar_width,
#     #        edgecolor=seaborn.xkcd_rgb['grey green'],
#     #        linewidth=1, color=seaborn.xkcd_rgb['light grey green'], zorder=10, alpha=0.9, hatch="||")
#     # ax.bar(x=np.arange(len(x)) + 2 * bar_width + 0.08, height=y3, label='Lin', width=bar_width,
#     #        edgecolor=seaborn.xkcd_rgb['coffee'], linewidth=1, color=seaborn.xkcd_rgb['very light brown'], zorder=10,
#     #        alpha=0.9, hatch="xx", align="center")
#     # ax.bar(x=np.arange(len(x)) + 3 * bar_width + 0.12, height=y4, label='Vuddy', width=bar_width,
#     #        edgecolor=seaborn.xkcd_rgb['grey blue'], linewidth=1, color=seaborn.xkcd_rgb['light grey blue'], zorder=10,
#     #        alpha=0.9, hatch="")
#     # ax.bar(x=np.arange(len(x)) + 4 * bar_width + 0.16, height=y5, label='Deepbugs', width=bar_width,
#     #        edgecolor=seaborn.xkcd_rgb['grey purple'], linewidth=1, color=seaborn.xkcd_rgb['pale purple'], zorder=10,
#     #        alpha=0.9, hatch="++")
#     # ax.bar(x=np.arange(len(x)) + 5 * bar_width + 0.2, height=y6, label='LACUNA', width=bar_width,
#     #        edgecolor=seaborn.xkcd_rgb['rose'], linewidth=1, color=seaborn.xkcd_rgb['faded pink'], zorder=10,
#     #        alpha=0.9, hatch="\\\\")
#
#     ax.bar(x=np.arange(len(x)), height=y1, label='Vuldeepecker', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey green'],
#            linewidth=1, color=seaborn.xkcd_rgb['light grey green'], zorder=10, alpha=0.9, hatch="||")
#     ax.bar(x=np.arange(len(x)) + bar_width + 0.04, height=y2, label='μVuldeepecker', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey purple'], linewidth=1, color=seaborn.xkcd_rgb['pale purple'], zorder=10,
#            alpha=0.9, hatch="++")
#     ax.bar(x=np.arange(len(x)) + 2 * bar_width + 0.08, height=y3, label='Lin', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey blue'], linewidth=1, color=seaborn.xkcd_rgb['light grey blue'], zorder=10,
#            alpha=0.9, hatch="")
#     ax.bar(x=np.arange(len(x)) + 3 * bar_width + 0.12, height=y4, label='Vuddy', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['tan'],
#            linewidth=1, color=seaborn.xkcd_rgb['yellow tan'], zorder=10, alpha=0.9, hatch="//")
#     ax.bar(x=np.arange(len(x)) + 4 * bar_width + 0.16, height=y5, label='Deepbugs', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['coffee'], linewidth=1, color=seaborn.xkcd_rgb['very light brown'], zorder=10,
#            alpha=0.9, hatch="xx", align="center")
#     ax.bar(x=np.arange(len(x)) + 5 * bar_width + 0.2, height=y6, label='LACUNA', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['rose'], linewidth=1, color=seaborn.xkcd_rgb['faded pink'], zorder=10,
#            alpha=0.9, hatch="\\\\")
#
#     font = {'family': 'Times New Roman',
#             'weight': 'normal',
#             'size': 17.5
#             }
#     # plt.legend(loc='upper left', prop=font)
#     # plt.grid(axis="y", alpha=0.8, linestyle=':')
#
#     # 图例：设置位置
#     box = ax.get_position()
#     ax.set_position([box.x0, box.y0, box.width, box.height * 0.8])
#     ax.legend(loc='center left', bbox_to_anchor=(-0.06, 1.16), ncol=6, prop=font)
#     plt.grid(axis="y", alpha=0.8, linestyle=':')
#
#     plt.savefig(str(name) + '.pdf')
#
#     plt.show()
#
#
# ##===========================sard->github============================
# def graphSG(path, name):
#     df = pd.read_excel(path)
#     x = df['CWE'].values
#     y1 = df['VUDDY'].values
#     y2 = df['vuldeepecker'].values
#     y4 = df['μvuldeepecker'].values
#     y5 = df['TDSC'].values
#     y3 = df['Deepbug'].values
#     y6 = df['GCN'].values
#
#     fig = plt.figure(figsize=(25, 5), dpi=80)
#     # 在bar之后添加线
#     ax = fig.add_axes([0.12, 0.3, 0.8, 0.6], zorder=12)
#
#     ax.set_xticks(np.arange(11) + 0.35)
#     ax.set_xticklabels(x, fontdict={'horizontalalignment': 'center', 'size': 24, 'rotation': 20})
#     ax.set_yticks(np.arange(0.5, 0.95, 0.1))
#     ax.set_yticklabels([0.5, 0.6, 0.7, 0.8, 0.9],
#                        fontdict={'horizontalalignment': 'right', 'size': 30})
#     # plt.xlabel('CWE-TYPE', fontsize=30, weight=700)
#     ax.set_ylabel('Accuracy', fontsize=30)
#     ax.set_ylim((0.5, 0.95))
#     ax.set_xlim((-0.2, 11))
#
#     bar_width = 0.1
#     ax.bar(x=np.arange(len(x)), height=y1, label='VUDDY', width=bar_width, edgecolor=seaborn.xkcd_rgb['tan'],
#            linewidth=1, color=seaborn.xkcd_rgb['yellow tan'], zorder=10, alpha=0.9, hatch="//")
#     ax.bar(x=np.arange(len(x)) + bar_width + 0.04, height=y2, label='Vuldeepecker', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey green'],
#            linewidth=1, color=seaborn.xkcd_rgb['light grey green'], zorder=10, alpha=0.9, hatch="|||")
#     ax.bar(x=np.arange(len(x)) + 2 * bar_width + 0.08, height=y3, label='Deepbugs', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['coffee'], linewidth=1, color=seaborn.xkcd_rgb['very light brown'], zorder=10,
#            alpha=0.9, hatch="xx", align="center")
#     ax.bar(x=np.arange(len(x)) + 3 * bar_width + 0.12, height=y4, label='μVuldeepecker', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey blue'], linewidth=1, color=seaborn.xkcd_rgb['light grey blue'], zorder=10,
#            alpha=0.9, hatch="")
#     ax.bar(x=np.arange(len(x)) + 4 * bar_width + 0.16, height=y5, label='Lin', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey purple'], linewidth=1, color=seaborn.xkcd_rgb['pale purple'], zorder=10,
#            alpha=0.9, hatch="+++")
#     ax.bar(x=np.arange(len(x)) + 5 * bar_width + 0.2, height=y6, label='LACUNA', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['rose'], linewidth=1, color=seaborn.xkcd_rgb['faded pink'], zorder=10,
#            alpha=0.9, hatch="\\\\")
#
#     font = {'family': 'Times New Roman',
#             'weight': 'normal',
#             'size': 22
#             }
#     # plt.legend(loc='upper left', prop=font)
#     # plt.grid(axis="y", alpha=0.8, linestyle=':')
#
#     # 图例：设置位置
#     box = ax.get_position()
#     ax.set_position([box.x0, box.y0, box.width, box.height * 0.8])
#     ax.legend(loc='center left', bbox_to_anchor=(0.07, 1.12), ncol=6, prop=font)
#     plt.grid(axis="y", alpha=0.8, linestyle=':')
#
#     plt.savefig(str(name) + '.pdf')
#
#     plt.show()
#
#
# ##===========================addVul============================
# def graphAV(path, name):
#     df = pd.read_excel(path)
#     x = df['CWE'].values
#     y1 = df['baseline'].values
#     y2 = df['Zhou'].values
#     y3 = df['Zvd'].values
#     y4 = df['Serina'].values
#     y5 = df['LACUNA'].values
#
#     fig = plt.figure(figsize=(25, 5), dpi=80)
#     # 在bar之后添加线
#     ax = fig.add_axes([0.07, 0.3, 0.9, 0.52], zorder=11)
#
#     ax.set_xticks(np.arange(11) + 0.32)
#     ax.set_xticklabels(x, fontdict={'horizontalalignment': 'center', 'size': 26, 'weight': 700, 'rotation': 20})
#     ax.set_yticks(np.arange(0.4, 0.85, 0.1))
#     ax.set_yticklabels([0.4, 0.5, 0.6, 0.7, 0.8, 0.9],
#                        fontdict={'horizontalalignment': 'right', 'size': 30, 'weight': 700})
#     # plt.xlabel('CWE-TYPE', fontsize=30, weight=700)
#     ax.set_ylabel('F1 SCORE', fontsize=30, weight=700)
#     ax.set_ylim((0.4, 0.85))
#     ax.set_xlim((-0.35, 11))
#
#     bar_width = 0.12
#     ax.bar(x=np.arange(len(x)), height=y1, label='Baseline', width=bar_width, edgecolor=seaborn.xkcd_rgb['tan'],
#            linewidth=1, color=seaborn.xkcd_rgb['yellow tan'], zorder=10, alpha=0.9, hatch="//")
#     ax.bar(x=np.arange(len(x)) + bar_width + 0.04, height=y2, label='Zhou', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey green'],
#            linewidth=1, color=seaborn.xkcd_rgb['light grey green'], zorder=10, alpha=0.9, hatch="*")
#     ax.bar(x=np.arange(len(x)) + 2 * bar_width + 0.08, height=y3, label='Zvd', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey blue'], linewidth=1, color=seaborn.xkcd_rgb['light grey blue'], zorder=10,
#            alpha=0.9, hatch="", align="center")
#     ax.bar(x=np.arange(len(x)) + 3 * bar_width + 0.12, height=y4, label='Sabetta', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey purple'], linewidth=1, color=seaborn.xkcd_rgb['pale purple'], zorder=10,
#            alpha=0.9, hatch="..")
#     ax.bar(x=np.arange(len(x)) + 4 * bar_width + 0.16, height=y5, label='LACUNA', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['rose'], linewidth=1, color=seaborn.xkcd_rgb['faded pink'], zorder=10,
#            alpha=0.9, hatch="\\\\")
#
#     font = {'family': 'Times New Roman',
#             'weight': 'normal',
#             'size': 25
#             }
#     # plt.legend(loc='upper left', prop=font)
#     # plt.grid(axis="y", alpha=0.8, linestyle=':')
#
#     # 图例：设置位置
#     box = ax.get_position()
#     ax.set_position([box.x0, box.y0, box.width, box.height * 0.8])
#     ax.legend(loc='center left', bbox_to_anchor=(0.2, 1.15), ncol=5, prop=font)
#     plt.grid(axis="y", alpha=0.8, linestyle=':')
#
#     plt.savefig(str(name) + '.pdf')
#
#     plt.show()
#
#
# ##===========================adduVul============================
# def graphAUV(path, name):
#     df = pd.read_excel(path)
#     x = df['CWE'].values
#     y1 = df['baseline'].values
#     y2 = df['Zhou'].values
#     y3 = df['Zvd'].values
#     y4 = df['Serina'].values
#     y5 = df['LACUNA'].values
#
#     fig = plt.figure(figsize=(25, 5), dpi=80)
#     # 在bar之后添加线
#     ax = fig.add_axes([0.07, 0.3, 0.9, 0.52], zorder=11)
#
#     ax.set_xticks(np.arange(11) + 0.32)
#     ax.set_xticklabels(x, fontdict={'horizontalalignment': 'center', 'size': 26, 'weight': 700, 'rotation': 20})
#     ax.set_yticks(np.arange(0.4, 1.02, 0.1))
#     ax.set_yticklabels([0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1],
#                        fontdict={'horizontalalignment': 'right', 'size': 30, 'weight': 700})
#     # plt.xlabel('CWE-TYPE', fontsize=30, weight=700)
#     ax.set_ylabel('F1 SCORE', fontsize=30, weight=700)
#     ax.set_ylim((0.4, 1.02))
#     ax.set_xlim((-0.35, 11))
#
#     bar_width = 0.12
#     ax.bar(x=np.arange(len(x)), height=y1, label='Baseline', width=bar_width, edgecolor=seaborn.xkcd_rgb['tan'],
#            linewidth=1, color=seaborn.xkcd_rgb['yellow tan'], zorder=10, alpha=0.9, hatch="//")
#     ax.bar(x=np.arange(len(x)) + bar_width + 0.04, height=y2, label='Zhou', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey green'],
#            linewidth=1, color=seaborn.xkcd_rgb['light grey green'], zorder=10, alpha=0.9, hatch="*")
#     ax.bar(x=np.arange(len(x)) + 2 * bar_width + 0.08, height=y3, label='Zvd', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey blue'], linewidth=1, color=seaborn.xkcd_rgb['light grey blue'], zorder=10,
#            alpha=0.9, hatch="", align="center")
#     ax.bar(x=np.arange(len(x)) + 3 * bar_width + 0.12, height=y4, label='Sabetta', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey purple'], linewidth=1, color=seaborn.xkcd_rgb['pale purple'], zorder=10,
#            alpha=0.9, hatch="..")
#     ax.bar(x=np.arange(len(x)) + 4 * bar_width + 0.16, height=y5, label='LACUNA', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['rose'], linewidth=1, color=seaborn.xkcd_rgb['faded pink'], zorder=10,
#            alpha=0.9, hatch="\\\\")
#
#     font = {'family': 'Times New Roman',
#             'weight': 'normal',
#             'size': 25
#             }
#     # plt.legend(loc='upper left', prop=font)
#     # plt.grid(axis="y", alpha=0.8, linestyle=':')
#
#     # 图例：设置位置
#     box = ax.get_position()
#     ax.set_position([box.x0, box.y0, box.width, box.height * 0.8])
#     ax.legend(loc='center left', bbox_to_anchor=(0.2, 1.15), ncol=5, prop=font)
#     plt.grid(axis="y", alpha=0.8, linestyle=':')
#
#     plt.savefig(str(name) + '.pdf')
#
#     plt.show()
#
#
# ##===========================adduVul============================
# def graphALACUNA(path, name):
#     df = pd.read_excel(path)
#     x = df['CWE'].values
#     y1 = df['baseline'].values
#     y2 = df['Zhou'].values
#     y3 = df['Zvd'].values
#     y4 = df['Serina'].values
#     y5 = df['LACUNA'].values
#
#     fig = plt.figure(figsize=(25, 5), dpi=80)
#     # 在bar之后添加线
#     ax = fig.add_axes([0.07, 0.3, 0.9, 0.52], zorder=11)
#
#     ax.set_xticks(np.arange(11) + 0.32)
#     ax.set_xticklabels(x, fontdict={'horizontalalignment': 'center', 'size': 26, 'weight': 700, 'rotation': 20})
#     ax.set_yticks(np.arange(0.7, 1.02, 0.1))
#     ax.set_yticklabels([0.7, 0.8, 0.9, 1],
#                        fontdict={'horizontalalignment': 'right', 'size': 30, 'weight': 700})
#     # plt.xlabel('CWE-TYPE', fontsize=30, weight=700)
#     ax.set_ylabel('F1 SCORE', fontsize=30, weight=700)
#     ax.set_ylim((0.7, 1.02))
#     ax.set_xlim((-0.35, 11))
#
#     bar_width = 0.12
#     ax.bar(x=np.arange(len(x)), height=y1, label='Baseline', width=bar_width, edgecolor=seaborn.xkcd_rgb['tan'],
#            linewidth=1, color=seaborn.xkcd_rgb['yellow tan'], zorder=10, alpha=0.9, hatch="//")
#     ax.bar(x=np.arange(len(x)) + bar_width + 0.04, height=y2, label='Zhou', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey green'],
#            linewidth=1, color=seaborn.xkcd_rgb['light grey green'], zorder=10, alpha=0.9, hatch="*")
#     ax.bar(x=np.arange(len(x)) + 2 * bar_width + 0.08, height=y3, label='Zvd', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey blue'], linewidth=1, color=seaborn.xkcd_rgb['light grey blue'], zorder=10,
#            alpha=0.9, hatch="", align="center")
#     ax.bar(x=np.arange(len(x)) + 3 * bar_width + 0.12, height=y4, label='Sabetta', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey purple'], linewidth=1, color=seaborn.xkcd_rgb['pale purple'], zorder=10,
#            alpha=0.9, hatch="..")
#     ax.bar(x=np.arange(len(x)) + 4 * bar_width + 0.16, height=y5, label='LACUNA', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['rose'], linewidth=1, color=seaborn.xkcd_rgb['faded pink'], zorder=10,
#            alpha=0.9, hatch="\\\\")
#
#     font = {'family': 'Times New Roman',
#             'weight': 'normal',
#             'size': 25
#             }
#     # plt.legend(loc='upper left', prop=font)
#     # plt.grid(axis="y", alpha=0.8, linestyle=':')
#
#     # 图例：设置位置
#     box = ax.get_position()
#     ax.set_position([box.x0, box.y0, box.width, box.height * 0.8])
#     ax.legend(loc='center left', bbox_to_anchor=(0.2, 1.15), ncol=5, prop=font)
#     plt.grid(axis="y", alpha=0.8, linestyle=':')
#
#     plt.savefig(str(name) + '.pdf')
#
#     plt.show()
#
#
# # ============================多分类：多分类器============================
# def graphMulcla1(path, name):
#     df = pd.read_excel(path)
#     x = df['classifier'].values
#     y1 = df['precision'].values
#     y2 = df['recall'].values
#     y3 = df['F1'].values
#     y4 = df['FPR'].values
#
#     fig = plt.figure(figsize=(16, 5), dpi=80)
#     # 在bar之后添加线
#     ax = fig.add_axes([0.12, 0.32, 0.8, 0.4], zorder=11)
#     ax.set_xticks(np.arange(8) + 0.18)
#     ax.set_xticklabels(x, fontdict={'horizontalalignment': 'center', 'size': 22})
#     ax.set_yticks(np.arange(0, 1.02, 0.2))
#     ax.set_yticklabels([0, 0.2, 0.4, 0.6, 0.8, 1],
#                        fontdict={'horizontalalignment': 'right', 'size': 22})
#     plt.xlabel('classifier', fontsize=30)
#     ax.set_ylim((0, 1.02))
#     ax.set_xlim((-0.5, 8))
#
#     bar_width = 0.15
#     # hatch 内部填充形状{'/', '\', '|', '-', '+', 'x', 'o', 'O', '.', '*'}
#     plt.bar(x, height=y1, label='Precision', width=bar_width, edgecolor=seaborn.xkcd_rgb['tan'], linewidth=2,
#             color=seaborn.xkcd_rgb['yellow tan'], alpha=0.9, zorder=10, hatch='//')
#     # 将X轴数据改为使用np.arange(len(x_data))+bar_width,
#     # zorder参数越大 表示最后画上去 可以避免被覆盖
#     plt.bar(x=np.arange(len(x)) + bar_width + 0.04, height=y2, label='Recall', width=bar_width,
#             edgecolor=seaborn.xkcd_rgb['grey green'], linewidth=2, color=seaborn.xkcd_rgb['light grey green'],
#             alpha=0.9, zorder=10, hatch='xx')
#     ax.bar(x=np.arange(len(x)) + 2 * bar_width + 0.08, height=y3, label='F1', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey blue'], linewidth=1, color=seaborn.xkcd_rgb['light grey blue'], zorder=10,
#            alpha=0.9, hatch="")
#     ax.bar(x=np.arange(len(x)) + 3 * bar_width + 0.12, height=y4, label='FPR', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey purple'], linewidth=1, color=seaborn.xkcd_rgb['pale purple'], zorder=10,
#            alpha=0.9, hatch="\\\\")
#
#     # for a, b in enumerate(y1):
#     #     # 显示数字标签为百分数
#     #     plt.text(a+0.05, b, '%.0f%%' % (b * 100), ha='center', va='bottom',
#     #              fontdict={'size': 22, 'weight': 600})  # ha为水平位置，va为垂直位置
#     # for a, b in enumerate(y2):
#     #     plt.text(a + 0.46, b, '%.0f%%' % (b * 100), ha='center', va='bottom', fontdict={'size': 22, 'weight': 600})
#
#     # 显示图例
#     font = {'family': 'Times New Roman',
#             'weight': 'normal',
#             'size': 22
#             }
#     # plt.legend(loc='upper left', prop=font)
#     # plt.grid(axis="y",alpha=0.8, linestyle=':')
#     # plt.savefig(str(name) + '.pdf')
#     box = ax.get_position()
#     ax.set_position([box.x0, box.y0, box.width, box.height * 0.8])
#     ax.legend(loc='center left', bbox_to_anchor=(0.14, 1.18), ncol=5, prop=font)
#     plt.grid(axis="y", alpha=0.8, linestyle=':')
#
#     plt.savefig(str(name) + '.pdf')
#     plt.show()
#
#
# # ============================多分类：效果============================
# def graphMulcla2(path, name):
#     df = pd.read_excel(path)
#     x = df['CWE'].values
#     y1 = df['precision'].values
#     y2 = df['recall'].values
#     y3 = df['f1'].values
#
#     fig = plt.figure(figsize=(18, 8), dpi=80)
#     # 在bar之后添加线
#     ax = fig.add_axes([0.12, 0.3, 0.8, 0.52], zorder=11)
#     ax.set_xticks(np.arange(12) + 0.18)
#     ax.set_xticklabels(x, fontdict={'horizontalalignment': 'center', 'size': 20, 'weight': 700, 'rotation': 20})
#     ax.set_yticks(np.arange(0.7, 1.02, 0.05))
#     ax.set_yticklabels([0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1],
#                        fontdict={'horizontalalignment': 'right', 'size': 30, 'weight': 700})
#     ax.set_ylim((0.7, 1.02))
#     ax.set_xlim((-0.5, 12))
#
#     bar_width = 0.2
#     # hatch 内部填充形状{'/', '\', '|', '-', '+', 'x', 'o', 'O', '.', '*'}
#     ax.bar(x=np.arange(len(x)), height=y1, label='Precision', width=bar_width, edgecolor=seaborn.xkcd_rgb['tan'],
#            linewidth=1, color=seaborn.xkcd_rgb['yellow tan'], zorder=10, alpha=0.9, hatch="//")
#     ax.bar(x=np.arange(len(x)) + bar_width + 0.04, height=y2, label='Recall', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey green'],
#            linewidth=1, color=seaborn.xkcd_rgb['light grey green'], zorder=10, alpha=0.9, hatch="o")
#     ax.bar(x=np.arange(len(x)) + 2 * bar_width + 0.08, height=y3, label='F1', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey blue'], linewidth=1, color=seaborn.xkcd_rgb['light grey blue'], zorder=10,
#            alpha=0.9, hatch="", align="center")
#
#     # 显示图例
#     font = {'family': 'Times New Roman',
#             'weight': 'normal',
#             'size': 20
#             }
#     # plt.legend(loc='upper left', prop=font)
#     # plt.grid(axis="y",alpha=0.8, linestyle=':')
#
#     box = ax.get_position()
#     ax.set_position([box.x0, box.y0, box.width, box.height * 0.8])
#     ax.legend(loc='center left', bbox_to_anchor=(0.3, 0.92), ncol=5, prop=font)
#     plt.grid(axis="y", alpha=0.8, linestyle=':')
#
#     plt.savefig(str(name) + '.pdf')
#
#     plt.show()
#
#
# # ============================fig3:sap dataset============================
# def graph3SAP(path, name):
#     df = pd.read_excel(path)
#     x = df['model'].values
#     y1 = df['precision'].values
#     y2 = df['recall'].values
#     y3 = df['f1'].values
#     y4 = df['fpr'].values
#
#     fig = plt.figure(figsize=(15, 6), dpi=80)
#     # 在bar之后添加线
#     ax = fig.add_axes([0.12, 0.28, 0.8, 0.6], zorder=12)
#
#     ax.set_xticks(np.arange(7) + 0.29)
#     ax.set_xticklabels(x, fontdict={'horizontalalignment': 'center', 'size': 26, 'weight': 700})
#     ax.set_yticks(np.arange(0, 0.88, 0.1))
#     ax.set_yticklabels([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8],
#                        fontdict={'horizontalalignment': 'right', 'size': 26, 'weight': 700})
#     plt.xlabel('SAP dataset', fontsize=30, weight=700)
#     # ax.set_ylabel('SCORE', fontsize=30, weight=700)
#     ax.set_ylim((0, 0.88))
#
#     bar_width = 0.15
#     ax.bar(x=np.arange(len(x)), height=y1, label='Precision', width=bar_width, edgecolor=seaborn.xkcd_rgb['tan'],
#            linewidth=1,
#            color=seaborn.xkcd_rgb['yellow tan'], zorder=10, alpha=0.9, hatch="//")
#     ax.bar(x=np.arange(len(x)) + bar_width + 0.04, height=y2, label='Recall', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey green'], linewidth=1, color=seaborn.xkcd_rgb['light grey green'], zorder=10,
#            alpha=0.9, hatch="o", align="center")
#     ax.bar(x=np.arange(len(x)) + 2 * bar_width + 0.08, height=y3, label='F1', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey blue'], linewidth=1, color=seaborn.xkcd_rgb['light grey blue'], zorder=10,
#            alpha=0.9, hatch="")
#     ax.bar(x=np.arange(len(x)) + 3 * bar_width + 0.12, height=y4, label='FPR', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey purple'], linewidth=1, color=seaborn.xkcd_rgb['pale purple'], zorder=10,
#            alpha=0.9, hatch="\\\\")
#
#     font = {'family': 'Times New Roman',
#             'weight': 'normal',
#             'size': 22
#             }
#     # plt.legend(loc='upper left', prop=font)
#     # plt.grid(axis="y", alpha=0.8, linestyle=':')
#
#     # 图例：设置位置
#     box = ax.get_position()
#     ax.set_position([box.x0, box.y0, box.width, box.height * 0.8])
#     ax.legend(loc='center left', bbox_to_anchor=(0.15, 1.11), ncol=4, prop=font)
#     plt.grid(axis="y", alpha=0.8, linestyle=':')
#
#     plt.savefig(str(name) + '.pdf')
#
#     plt.show()
#
#
# # ============================fig3:ours dataset============================
# def graph3Ours(path, name):
#     df = pd.read_excel(path)
#     x = df['model'].values
#     y1 = df['precision'].values
#     y2 = df['recall'].values
#     y3 = df['f1'].values
#     y4 = df['fpr'].values
#
#     fig = plt.figure(figsize=(15, 6), dpi=80)
#     # 在bar之后添加线
#     ax = fig.add_axes([0.12, 0.28, 0.8, 0.6], zorder=12)
#
#     ax.set_xticks(np.arange(7) + 0.29)
#     ax.set_xticklabels(x, fontdict={'horizontalalignment': 'center', 'size': 26, 'weight': 700, 'rotation': 20})
#     ax.set_yticks(np.arange(0, 0.912, 0.1))
#     ax.set_yticklabels([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9],
#                        fontdict={'horizontalalignment': 'right', 'size': 26, 'weight': 700})
#     plt.xlabel('Ours dataset', fontsize=30, weight=700)
#     # ax.set_ylabel('SCORE', fontsize=30, weight=700)
#     ax.set_ylim((0, 0.912))
#
#     bar_width = 0.15
#     ax.bar(x=np.arange(len(x)), height=y1, label='Precision', width=bar_width, edgecolor=seaborn.xkcd_rgb['tan'],
#            linewidth=1,
#            color=seaborn.xkcd_rgb['yellow tan'], zorder=10, alpha=0.9, hatch="//")
#     ax.bar(x=np.arange(len(x)) + bar_width + 0.04, height=y2, label='Recall', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey green'], linewidth=1, color=seaborn.xkcd_rgb['light grey green'], zorder=10,
#            alpha=0.9, hatch="o", align="center")
#     ax.bar(x=np.arange(len(x)) + 2 * bar_width + 0.08, height=y3, label='F1', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey blue'], linewidth=1, color=seaborn.xkcd_rgb['light grey blue'], zorder=10,
#            alpha=0.9, hatch="")
#     ax.bar(x=np.arange(len(x)) + 3 * bar_width + 0.12, height=y4, label='FPR', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey purple'], linewidth=1, color=seaborn.xkcd_rgb['pale purple'], zorder=10,
#            alpha=0.9, hatch="\\\\")
#
#     font = {'family': 'Times New Roman',
#             'weight': 'normal',
#             'size': 22
#             }
#     # plt.legend(loc='upper left', prop=font)
#     # plt.grid(axis="y", alpha=0.8, linestyle=':')
#
#     # 图例：设置位置
#     box = ax.get_position()
#     ax.set_position([box.x0, box.y0, box.width, box.height * 0.8])
#     ax.legend(loc='center left', bbox_to_anchor=(0.15, 1.11), ncol=4, prop=font)
#     plt.grid(axis="y", alpha=0.8, linestyle=':')
#
#     plt.savefig(str(name) + '.pdf')
#
#     plt.show()


##===========================sard->accuracy============================
#画ccs的不同模型的不同CWE类型的accuracy的对比
def graphSA(path, name):
    df = pd.read_excel(path)
    x = df['CWE'].values
    # x2 = df['x'].values

    y1 = df['Lin'].values
    y2 = df['VUDDY'].values
    y3 = df['vuldeepecker'].values
    y4 = df['μvuldeepecker'].values
    y5 = df['NIPS'].values
    y6 = df['TDSC'].values
    y7 = df['RGIN'].values

    fig = plt.figure(figsize=(31, 6), dpi=80)
    # 在bar之后添加线
    ax = fig.add_axes([0.028, 0.3, 0.95, 0.5], zorder=11)

    ax.set_xticks(np.arange(31)+0.4)
    ax.set_xticklabels(x, fontdict={'horizontalalignment': 'center', 'size': 25, 'rotation': 45,'family': 'Arial'})

    ax.set_yticks(np.arange(0.4, 1.02, 0.1))
    ax.set_yticklabels(['40%', '50%', '60%', '70%', '80%', '90%', '100%'],
                       fontdict={'horizontalalignment': 'right', 'size': 20,'family': 'Arial'})
    # plt.xlabel('CWE-TYPE', fontsize=30, weight=700)
    ax.set_ylabel('Accuracy', fontsize=30,fontdict={'family': 'Arial'})
    ax.set_ylim((0.4, 1.02))
    ax.set_xlim((-0.4, 31.3))

    # hatch 内部填充形状{'/', '\', '|', '-', '+', 'x', 'o', 'O', '.', '*'}
    bar_width = 0.09

    # ax.bar(x=np.arange(len(x)), height=y1, label='DEEPBUGS', width=bar_width, edgecolor=seaborn.xkcd_rgb['grey blue'],
    #        linewidth=1, color=seaborn.xkcd_rgb['light grey blue'], zorder=10,
    #        alpha=0.9, hatch="\\\\", align="center")
    # ax.bar(x=np.arange(len(x)) + bar_width + 0.04, height=y2, label='VUDDY', width=bar_width,
    #        edgecolor=seaborn.xkcd_rgb['coffee'],
    #        linewidth=1, color=seaborn.xkcd_rgb['very light brown'], zorder=10, alpha=0.9, hatch="xx")
    # ax.bar(x=np.arange(len(x)) + 2 * bar_width + 0.08, height=y3, label='VULDEEPECKER', width=bar_width,
    #        edgecolor=seaborn.xkcd_rgb['grey green'],
    #        linewidth=1, color=seaborn.xkcd_rgb['light grey green'], zorder=10, alpha=0.9, hatch="||")
    # ax.bar(x=np.arange(len(x)) + 3 * bar_width + 0.12, height=y4, label='μVULDEEPECKER', width=bar_width,
    #        edgecolor=seaborn.xkcd_rgb['grey purple'], linewidth=1, color=seaborn.xkcd_rgb['pale purple'], zorder=10,
    #        alpha=0.9, hatch="++")
    # ax.bar(x=np.arange(len(x)) + 4 * bar_width + 0.16, height=y5, label='DEVIGN', width=bar_width,
    #        edgecolor=seaborn.xkcd_rgb['rose'], linewidth=1, color=seaborn.xkcd_rgb['faded pink'], zorder=10,
    #        alpha=0.9, hatch="")
    # ax.bar(x=np.arange(len(x)) + 5 * bar_width + 0.2, height=y6, label='LIN et al.', width=bar_width,
    #        edgecolor=seaborn.xkcd_rgb['perrywinkle'], linewidth=1, color=seaborn.xkcd_rgb['light violet'], zorder=10,
    #        alpha=0.9, hatch="|\\|")
    # ax.bar(x=np.arange(len(x)) + 6 * bar_width + 0.24, height=y7, label='FUNDED', width=bar_width,
    #        edgecolor=seaborn.xkcd_rgb['orangeish'], linewidth=1, color=seaborn.xkcd_rgb['peach'], zorder=10,
    #        alpha=0.9, hatch="-/")

    ax.bar(x=np.arange(len(x)), height=y1, label='DEEPBUGS', width=bar_width, edgecolor='#D3D3D3',
           linewidth=1, color='#ede4fb', zorder=10,
           alpha=0.9, hatch="", align="center")
    ax.bar(x=np.arange(len(x)) + bar_width + 0.04, height=y2, label='VUDDY', width=bar_width,
           edgecolor='#cabfdc',
           linewidth=1, color='#d3c4ea', zorder=10, alpha=0.9, hatch="")
    ax.bar(x=np.arange(len(x)) + 2 * bar_width + 0.08, height=y3, label='VULDEEPECKER', width=bar_width,
           edgecolor='#a79bbe',
           linewidth=1, color='#b8a5d9', zorder=10, alpha=0.9, hatch="")
    ax.bar(x=np.arange(len(x)) + 3 * bar_width + 0.12, height=y4, label='μVULDEEPECKER', width=bar_width,
           edgecolor='#8678a0', linewidth=1, color='#9d87c8', zorder=10,
           alpha=0.9, hatch="")
    ax.bar(x=np.arange(len(x)) + 4 * bar_width + 0.16, height=y5, label='DEVIGN', width=bar_width,
           edgecolor='#655784', linewidth=1, color='#836ab7', zorder=10,
           alpha=0.9, hatch="")
    ax.bar(x=np.arange(len(x)) + 5 * bar_width + 0.2, height=y6, label='LIN et al.', width=bar_width,
           edgecolor='#453768', linewidth=1, color='#674ea7', zorder=10,
           alpha=0.9, hatch="")
    ax.bar(x=np.arange(len(x)) + 6 * bar_width + 0.24, height=y7, label='FUNDED', width=bar_width,
           edgecolor='#261a4d', linewidth=1, color='#493396', zorder=10,
           alpha=0.9, hatch="")

    font = {'family': 'Arial',
            'weight': 'normal',
            'size': 27
            }
    # plt.legend(loc='upper left', prop=font)
    # plt.grid(axis="y", alpha=0.8, linestyle=':')

    # 图例：设置位置
    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width, box.height * 0.8])
    ax.legend(loc='center left', bbox_to_anchor=(0.035, 1.15), ncol=7, prop=font)
    plt.grid(axis="y", alpha=0.8, linestyle=':')

    plt.savefig(str(name) + '.pdf')

    plt.show()

##===========================sard->accuracy============================
#画FUNDED模型的不同CWE的不同指标的对比
def graphLACUNA(path, name):
    df = pd.read_excel(path)
    x = df['CWE'].values
    y1 = df['accuracy'].values
    y2 = df['precision'].values
    y3 = df['recall'].values
    y4 = df['f1'].values

    fig = plt.figure(figsize=(28, 6), dpi=80)
    # 在bar之后添加线
    ax = fig.add_axes([0.07, 0.3, 0.9, 0.5], zorder=11)

    ax.set_xticks(np.arange(31)-0.1)
    # ax.set_xticks([])
    ax.set_xticklabels(x, fontdict={'horizontalalignment': 'center', 'size': 25, 'rotation': 40,'family':'Arial'})
    ax.set_yticks(np.arange(0.5, 1.02, 0.1))
    ax.set_yticklabels(['0.5', '0.6', '0.7', '0.8', '0.9', '1'],
                       fontdict={'horizontalalignment': 'right', 'size': 25,'family':'Arial'})
    # plt.xlabel('CWE-TYPE', fontsize=30, weight=700)
    # ax.set_ylabel('Accuracy', fontsize=30, weight=700)
    ax.set_ylim((0.5, 1.02))
    ax.set_xlim((-0.5, 31.2))

    # hatch 内部填充形状{'/', '\', '|', '-', '+', 'x', 'o', 'O', '.', '*'}
    bar_width = 0.12
    # ax.bar(x=np.arange(len(x)), height=y1, label='Accuracy', width=bar_width, edgecolor=seaborn.xkcd_rgb['tan'],
    #        linewidth=1,
    #        color=seaborn.xkcd_rgb['yellow tan'], zorder=10, alpha=0.9, hatch="//")
    # ax.bar(x=np.arange(len(x)) + bar_width + 0.06, height=y2, label='Precision', width=bar_width,
    #        edgecolor=seaborn.xkcd_rgb['grey green'], linewidth=1, color=seaborn.xkcd_rgb['light grey green'], zorder=10,
    #        alpha=0.9, hatch="xx")
    # ax.bar(x=np.arange(len(x)) + 2 * bar_width + 0.12, height=y3, label='Recall', width=bar_width,
    #        edgecolor=seaborn.xkcd_rgb['grey blue'], linewidth=1, color=seaborn.xkcd_rgb['light grey blue'], zorder=10,
    #        alpha=0.9, hatch="")
    # ax.bar(x=np.arange(len(x)) + 3 * bar_width + 0.18, height=y4, label='F1 Score', width=bar_width,
    #        edgecolor=seaborn.xkcd_rgb['grey purple'], linewidth=1, color=seaborn.xkcd_rgb['pale purple'], zorder=10,
    #        alpha=0.9, hatch="\\\\")

    ax.bar(x=np.arange(len(x)), height=y1, label='Accuracy', width=bar_width,
           linewidth=1,edgecolor = '#D3D3D3',color='#ede4fb', zorder=10, alpha=0.9,hatch="")
    ax.bar(x=np.arange(len(x)) + bar_width + 0.06, height=y2, label='Precision', width=bar_width,
           linewidth=1, edgecolor = '#a79bbe',color='#b8a5d9', zorder=10,
           alpha=0.9,hatch="")
    ax.bar(x=np.arange(len(x)) + 2 * bar_width + 0.12, height=y3, label='Recall', width=bar_width,
            linewidth=1, edgecolor = '#655784',color='#836ab7', zorder=10,
           alpha=0.9,hatch="")
    ax.bar(x=np.arange(len(x)) + 3 * bar_width + 0.18, height=y4, label='F1 Score', width=bar_width,
          linewidth=1, color='#261a4d', zorder=10)

    font = {'family': 'Arial',
            'weight': 'normal',
            'size': 27
    }
    # plt.legend(loc='upper left', prop=font)
    # plt.grid(axis="y", alpha=0.8, linestyle=':')

    # 图例：设置位置
    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width, box.height * 0.8])
    ax.legend(loc='center left', bbox_to_anchor=(0.25, 1.15), ncol=6, prop=font)
    plt.grid(axis="y", alpha=0.8, linestyle=':')

    plt.savefig(str(name) + '.pdf')

    plt.show()


# ##===========================Eva_CopSap============================
# def graph31(path, name):
#     df = pd.read_excel(path)
#     x = df['value'].values
#     y1 = df['VccFinder'].values
#     y2 = df['Zhou'].values
#     y3 = df['Vulpecker'].values
#     y4 = df['Zvd'].values
#     y5 = df['Serina'].values
#     y6 = df['LACUNA'].values
#
#     fig = plt.figure(figsize=(8, 3), dpi=80)
#     # 在bar之后添加线
#     ax = fig.add_axes([0.14, 0.28, 0.8, 0.5], zorder=11)
#
#     ax.set_xticks(np.arange(0, 2, 1) + 0.33)
#     ax.set_xticklabels(x, fontdict={'horizontalalignment': 'center', 'size': 14})
#     ax.set_yticks(np.arange(0, 1.02, 0.2))
#     ax.set_yticklabels(['0%', '20%', '40%', '60%', '80%', '100%'],
#                        fontdict={'horizontalalignment': 'right', 'size': 14})
#     # plt.xlabel('SAP Dataset', fontsize=30, weight=700)
#     # ax.set_ylabel('Accuracy', fontsize=30, weight=700)
#     ax.set_ylim((0, 1.02))
#     ax.set_xlim((-0.1, 1.8))
#
#     # hatch 内部填充形状{'/', '\', '|', '-', '+', 'x', 'o', 'O', '.', '*'}
#     bar_width = 0.1
#     # ax.bar(x=np.arange(len(x)), height=y1, label='VccFinder', width=bar_width, edgecolor=seaborn.xkcd_rgb['tan'],
#     #        linewidth=1, color=seaborn.xkcd_rgb['yellow tan'], zorder=10, alpha=0.9, hatch="//")
#     # ax.bar(x=np.arange(len(x)) + bar_width + 0.03, height=y2, label='Zhou', width=bar_width,
#     #        edgecolor=seaborn.xkcd_rgb['grey green'],
#     #        linewidth=1, color=seaborn.xkcd_rgb['light grey green'], zorder=10, alpha=0.9, hatch="||")
#     # ax.bar(x=np.arange(len(x)) + 2 * bar_width + 0.06, height=y3, label='Vulpecker', width=bar_width,
#     #        edgecolor=seaborn.xkcd_rgb['coffee'], linewidth=1, color=seaborn.xkcd_rgb['very light brown'], zorder=10,
#     #        alpha=0.9, hatch="xx", align="center")
#     # ax.bar(x=np.arange(len(x)) + 3 * bar_width + 0.09, height=y4, label='Zvd', width=bar_width,
#     #        edgecolor=seaborn.xkcd_rgb['grey blue'], linewidth=1, color=seaborn.xkcd_rgb['light grey blue'], zorder=10,
#     #        alpha=0.9, hatch="")
#     # ax.bar(x=np.arange(len(x)) + 4 * bar_width + 0.12, height=y5, label='Sabetta', width=bar_width,
#     #        edgecolor=seaborn.xkcd_rgb['grey purple'], linewidth=1, color=seaborn.xkcd_rgb['pale purple'], zorder=10,
#     #        alpha=0.9, hatch="++")
#     # ax.bar(x=np.arange(len(x)) + 5 * bar_width + 0.15, height=y6, label='LACUNA', width=bar_width,
#     #        edgecolor=seaborn.xkcd_rgb['rose'], linewidth=1, color=seaborn.xkcd_rgb['faded pink'], zorder=10,
#     #        alpha=0.9, hatch="\\\\")
#     ax.bar(x=np.arange(len(x)), height=y1, label='VccFinder', width=bar_width, edgecolor=seaborn.xkcd_rgb['rose'],
#            linewidth=1, color=seaborn.xkcd_rgb['faded pink'], zorder=10, alpha=0.9, hatch="||")
#     ax.bar(x=np.arange(len(x)) + bar_width + 0.03, height=y2, label='Zhou', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['tan'],
#            linewidth=1, color=seaborn.xkcd_rgb['yellow tan'], zorder=10, alpha=0.9, hatch="///")
#     ax.bar(x=np.arange(len(x)) + 2 * bar_width + 0.06, height=y3, label='Vulpecker', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['coffee'], linewidth=1, color=seaborn.xkcd_rgb['very light brown'], zorder=10,
#            alpha=0.9, hatch="++", align="center")
#     ax.bar(x=np.arange(len(x)) + 3 * bar_width + 0.09, height=y4, label='Zvd', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey green'], linewidth=1, color=seaborn.xkcd_rgb['light grey green'], zorder=10,
#            alpha=0.9, hatch="xx")
#     ax.bar(x=np.arange(len(x)) + 4 * bar_width + 0.12, height=y5, label='Sabetta', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey blue'], linewidth=1, color=seaborn.xkcd_rgb['light grey blue'], zorder=10,
#            alpha=0.9, hatch="")
#     ax.bar(x=np.arange(len(x)) + 5 * bar_width + 0.15, height=y6, label='LACUNA', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey purple'], linewidth=1, color=seaborn.xkcd_rgb['pale purple'], zorder=10,
#            alpha=0.9, hatch="\\\\\\")
#
#     font = {'family': 'Times New Roman',
#             'weight': 'normal',
#             'size': 10.5
#             }
#     # plt.legend(loc='upper left', prop=font)
#     # plt.grid(axis="y", alpha=0.8, linestyle=':')
#
#     # 图例：设置位置
#     box = ax.get_position()
#     ax.set_position([box.x0, box.y0, box.width, box.height * 0.8])
#     # ax.legend(loc='center left', bbox_to_anchor=(0, 1.25), ncol=3, prop=font)
#     ax.legend(loc='center left', bbox_to_anchor=(-0.08, 1.15), ncol=6, prop=font)
#     plt.grid(axis="y", alpha=0.8, linestyle=':')
#
#     plt.savefig(str(name) + '.pdf')
#
#     plt.show()
#
#
# ##===========================Eva_CopOurs============================
# def graph32(path, name):
#     df = pd.read_excel(path)
#     x = df['value'].values
#     y1 = df['VccFinder'].values
#     y2 = df['Vulpecker'].values
#     y3 = df['Zvd'].values
#     y4 = df['Serina'].values
#     y5 = df['Zhou'].values
#     y6 = df['LACUNA'].values
#
#     fig = plt.figure(figsize=(8, 3), dpi=80)
#     # 在bar之后添加线
#     ax = fig.add_axes([0.14, 0.28, 0.8, 0.5], zorder=11)
#
#     ax.set_xticks(np.arange(0, 2, 1) + 0.33)
#     ax.set_xticklabels(x, fontdict={'horizontalalignment': 'center', 'size': 14})
#     ax.set_yticks(np.arange(0, 1.02, 0.2))
#     ax.set_yticklabels(['0%', '20%', '40%', '60%', '80%', '100%'],
#                        fontdict={'horizontalalignment': 'right', 'size': 14})
#     # plt.xlabel('Github Dataset', fontsize=30, weight=700)
#     # ax.set_ylabel('Accuracy', fontsize=30, weight=700)
#     ax.set_ylim((0, 1.02))
#     ax.set_xlim((-0.1, 1.8))
#
#     # hatch 内部填充形状{'/', '\', '|', '-', '+', 'x', 'o', 'O', '.', '*'}
#     bar_width = 0.1
#     # ax.bar(x=np.arange(len(x)), height=y1, label='VccFinder', width=bar_width, edgecolor=seaborn.xkcd_rgb['tan'],
#     #        linewidth=1, color=seaborn.xkcd_rgb['yellow tan'], zorder=10, alpha=0.9, hatch="//")
#     # ax.bar(x=np.arange(len(x)) + bar_width + 0.03, height=y2, label='Zhou', width=bar_width,
#     #        edgecolor=seaborn.xkcd_rgb['grey green'],
#     #        linewidth=1, color=seaborn.xkcd_rgb['light grey green'], zorder=10, alpha=0.9, hatch="||")
#     # ax.bar(x=np.arange(len(x)) + 2 * bar_width + 0.06, height=y3, label='Vulpecker', width=bar_width,
#     #        edgecolor=seaborn.xkcd_rgb['coffee'], linewidth=1, color=seaborn.xkcd_rgb['very light brown'], zorder=10,
#     #        alpha=0.9, hatch="xx", align="center")
#     # ax.bar(x=np.arange(len(x)) + 3 * bar_width + 0.09, height=y4, label='Zvd', width=bar_width,
#     #        edgecolor=seaborn.xkcd_rgb['grey blue'], linewidth=1, color=seaborn.xkcd_rgb['light grey blue'], zorder=10,
#     #        alpha=0.9, hatch="")
#     # ax.bar(x=np.arange(len(x)) + 4 * bar_width + 0.12, height=y5, label='Sabetta', width=bar_width,
#     #        edgecolor=seaborn.xkcd_rgb['grey purple'], linewidth=1, color=seaborn.xkcd_rgb['pale purple'], zorder=10,
#     #        alpha=0.9, hatch="++")
#     # ax.bar(x=np.arange(len(x)) + 5 * bar_width + 0.15, height=y6, label='LACUNA', width=bar_width,
#     #        edgecolor=seaborn.xkcd_rgb['rose'], linewidth=1, color=seaborn.xkcd_rgb['faded pink'], zorder=10,
#     #        alpha=0.9, hatch="\\\\")
#     ax.bar(x=np.arange(len(x)), height=y1, label='VccFinder', width=bar_width, edgecolor=seaborn.xkcd_rgb['rose'],
#            linewidth=1, color=seaborn.xkcd_rgb['faded pink'], zorder=10, alpha=0.9, hatch="||")
#     ax.bar(x=np.arange(len(x)) + bar_width + 0.03, height=y2, label='Zhou', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['tan'],
#            linewidth=1, color=seaborn.xkcd_rgb['yellow tan'], zorder=10, alpha=0.9, hatch="///")
#     ax.bar(x=np.arange(len(x)) + 2 * bar_width + 0.06, height=y3, label='Vulpecker', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['coffee'], linewidth=1, color=seaborn.xkcd_rgb['very light brown'], zorder=10,
#            alpha=0.9, hatch="++", align="center")
#     ax.bar(x=np.arange(len(x)) + 3 * bar_width + 0.09, height=y4, label='Zvd', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey green'], linewidth=1, color=seaborn.xkcd_rgb['light grey green'], zorder=10,
#            alpha=0.9, hatch="xx")
#     ax.bar(x=np.arange(len(x)) + 4 * bar_width + 0.12, height=y5, label='Sabetta', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey blue'], linewidth=1, color=seaborn.xkcd_rgb['light grey blue'], zorder=10,
#            alpha=0.9, hatch="")
#     ax.bar(x=np.arange(len(x)) + 5 * bar_width + 0.15, height=y6, label='LACUNA', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey purple'], linewidth=1, color=seaborn.xkcd_rgb['pale purple'], zorder=10,
#            alpha=0.9, hatch="\\\\\\")
#
#     font = {'family': 'Times New Roman',
#             'weight': 'normal',
#             'size': 10.5
#             }
#     # plt.legend(loc='upper left', prop=font)
#     # plt.grid(axis="y", alpha=0.8, linestyle=':')
#
#     # 图例：设置位置
#     box = ax.get_position()
#     ax.set_position([box.x0, box.y0, box.width, box.height * 0.8])
#     # ax.legend(loc='center left', bbox_to_anchor=(0, 1.25), ncol=3, prop=font)
#     ax.legend(loc='center left', bbox_to_anchor=(-0.08, 1.15), ncol=6, prop=font)
#     plt.grid(axis="y", alpha=0.8, linestyle=':')
#
#     plt.savefig(str(name) + '.pdf')
#
#     plt.show()
#
#
# ##===========================Eva_CopDetect============================
# def graph33(path, name):
#     df = pd.read_excel(path)
#     x = df['value'].values
#     y1 = df['VccFinder'].values
#     y2 = df['Serina'].values
#     y3 = df['Vulpecker'].values
#     y4 = df['Zhou'].values
#     y5 = df['Zvd'].values
#     y6 = df['LACUNA'].values
#
#     fig = plt.figure(figsize=(8, 3), dpi=80)
#     # 在bar之后添加线
#     ax = fig.add_axes([0.14, 0.28, 0.8, 0.5], zorder=11)
#
#     ax.set_xticks(np.arange(0, 2, 1) + 0.33)
#     ax.set_xticklabels(x, fontdict={'horizontalalignment': 'center', 'size': 14})
#     ax.set_yticks(np.arange(0, 1.02, 0.2))
#     ax.set_yticklabels(['0%', '20%', '40%', '60%', '80%', '100%'],
#                        fontdict={'horizontalalignment': 'right', 'size': 14})
#     # plt.xlabel('Zvd Dataset', fontsize=30, weight=700)
#     # ax.set_ylabel('Accuracy', fontsize=30, weight=700)
#     ax.set_ylim((0, 1.02))
#     ax.set_xlim((-0.1, 1.8))
#
#     # hatch 内部填充形状{'/', '\', '|', '-', '+', 'x', 'o', 'O', '.', '*'}
#     bar_width = 0.1
#     ax.bar(x=np.arange(len(x)), height=y1, label='VccFinder', width=bar_width, edgecolor=seaborn.xkcd_rgb['rose'],
#            linewidth=1, color=seaborn.xkcd_rgb['faded pink'], zorder=10, alpha=0.9, hatch="||")
#     ax.bar(x=np.arange(len(x)) + bar_width + 0.03, height=y2, label='Zhou', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['tan'],
#            linewidth=1, color=seaborn.xkcd_rgb['yellow tan'], zorder=10, alpha=0.9, hatch="///")
#     ax.bar(x=np.arange(len(x)) + 2 * bar_width + 0.06, height=y3, label='Vulpecker', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['coffee'], linewidth=1, color=seaborn.xkcd_rgb['very light brown'], zorder=10,
#            alpha=0.9, hatch="++", align="center")
#     ax.bar(x=np.arange(len(x)) + 3 * bar_width + 0.09, height=y4, label='Zvd', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey green'], linewidth=1, color=seaborn.xkcd_rgb['light grey green'], zorder=10,
#            alpha=0.9, hatch="xx")
#     ax.bar(x=np.arange(len(x)) + 4 * bar_width + 0.12, height=y5, label='Sabetta', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey blue'], linewidth=1, color=seaborn.xkcd_rgb['light grey blue'], zorder=10,
#            alpha=0.9, hatch="")
#     ax.bar(x=np.arange(len(x)) + 5 * bar_width + 0.15, height=y6, label='LACUNA', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey purple'], linewidth=1, color=seaborn.xkcd_rgb['pale purple'], zorder=10,
#            alpha=0.9, hatch="\\\\\\")
#
#     font = {'family': 'Times New Roman',
#             'weight': 'normal',
#             'size': 10.5
#             }
#     # plt.legend(loc='upper left', prop=font)
#     # plt.grid(axis="y", alpha=0.8, linestyle=':')
#
#     # 图例：设置位置
#     box = ax.get_position()
#     ax.set_position([box.x0, box.y0, box.width, box.height * 0.8])
#     # ax.legend(loc='center left', bbox_to_anchor=(0, 1.25), ncol=3, prop=font)
#     ax.legend(loc='center left', bbox_to_anchor=(-0.08, 1.15), ncol=6, prop=font)
#     plt.grid(axis="y", alpha=0.8, linestyle=':')
#
#     plt.savefig(str(name) + '.pdf')
#
#     plt.show()
#
#
# ##===========================sard自测展示 precision recall f1============================
# def graphPRF(path, name):
#     df = pd.read_excel(path)
#     x = df['value'].values
#     y1 = df['VUDDY'].values
#     y2 = df['vuldeepecker'].values
#     y3 = df['Deepbugs'].values
#     y4 = df['μvuldeepecker'].values
#     y5 = df['Lin'].values
#     y6 = df['LACUNA'].values
#
#     df2 = pd.read_excel(r"C:\Users\WHT\Desktop\不能颓鸭\gra\gra\P.xlsx")
#     x1 = df2['value'].values
#     y12 = df2['Deepbugs'].values
#     y22 = df2['Lin'].values
#     y32 = df2['vuldeepecker'].values
#     y42 = df2['μvuldeepecker'].values
#     y52 = df2['LACUNA'].values
#     y62 = df2['VUDDY'].values
#
#     fig = plt.figure(figsize=(12, 3), dpi=80)
#     # 在bar之后添加线
#     ax = fig.add_axes([0.12, 0.25, 0.8, 0.5], zorder=11)
#
#     ax.set_xticks(np.arange(0, 3, 1) + 0.35)
#     ax.set_xticklabels(x, fontdict={'horizontalalignment': 'center', 'size': 16})
#     ax.set_yticks(np.arange(0, 1.02, 0.2))
#     ax.set_yticklabels([0, 0.2, 0.4, 0.6, 0.8, 1],
#                        fontdict={'horizontalalignment': 'right', 'size': 16})
#     # plt.xlabel('Mean', fontsize=30, weight=700)
#     # ax.set_ylabel('Accuracy', fontsize=30, weight=700)
#     ax.set_ylim((0, 1.02))
#     # ax.set_xlim((-0.1,1.8))
#
#     # 异常值
#     # ax.scatter(x=1, y=0.72, marker='X', s=300, color='r', alpha=0.8)
#     # ax.scatter(x=1.15, y=0.72, marker='X', s=300, color='r', alpha=0.8)
#     # ax.scatter(x=2, y=0.72, marker='X',s=300, color = 'r',alpha=0.8)
#     # ax.scatter(x=2.15, y=0.72, marker='X', s=300, color='r', alpha=0.8)
#
#     # hatch 内部填充形状{'/', '\', '|', '-', '+', 'x', 'o', 'O', '.', '*'}
#     bar_width = 0.1
#     # precision
#     ax.bar(x=np.arange(len(x1)), height=y12, width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['coffee'], linewidth=1, color=seaborn.xkcd_rgb['very light brown'], zorder=11,
#            alpha=0.9, hatch="xx", align="center")
#     ax.bar(x=np.arange(len(x1)) + bar_width + 0.04, height=y22, width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey purple'], linewidth=1, color=seaborn.xkcd_rgb['pale purple'], zorder=11,
#            alpha=0.9, hatch="++")
#     ax.bar(x=np.arange(len(x1)) + 2 * bar_width + 0.08, height=y32, width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey green'], linewidth=1, color=seaborn.xkcd_rgb['light grey green'], zorder=11,
#            alpha=0.9, hatch="|||")
#     ax.bar(x=np.arange(len(x1)) + 3 * bar_width + 0.12, height=y42, width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey blue'], linewidth=1, color=seaborn.xkcd_rgb['light grey blue'], zorder=11,
#            alpha=0.9, hatch="")
#     ax.bar(x=np.arange(len(x1)) + 4 * bar_width + 0.16, height=y52, width=bar_width, edgecolor=seaborn.xkcd_rgb['rose'],
#            linewidth=1, color=seaborn.xkcd_rgb['faded pink'], zorder=11, alpha=0.9, hatch="\\\\")
#     ax.bar(x=np.arange(len(x1)) + 5 * bar_width + 0.2, height=y62, width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['tan'],
#            linewidth=1, color=seaborn.xkcd_rgb['yellow tan'], zorder=11, alpha=0.9, hatch="//")
#
#     # recall f1
#     ax.bar(x=np.arange(len(x)), height=y1, label='VUDDY', width=bar_width, edgecolor=seaborn.xkcd_rgb['tan'],
#            linewidth=1, color=seaborn.xkcd_rgb['yellow tan'], zorder=10, alpha=0.9, hatch="//")
#     ax.bar(x=np.arange(len(x)) + bar_width + 0.04, height=y2, label='vuldeepecker', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey green'],
#            linewidth=1, color=seaborn.xkcd_rgb['light grey green'], zorder=10, alpha=0.9, hatch="|||")
#     ax.bar(x=np.arange(len(x)) + 2 * bar_width + 0.08, height=y3, label='Deepbugs', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['coffee'], linewidth=1, color=seaborn.xkcd_rgb['very light brown'], zorder=10,
#            alpha=0.9, hatch="xx", align="center")
#     ax.bar(x=np.arange(len(x)) + 3 * bar_width + 0.12, height=y4, label='μVuldeepecker', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey blue'], linewidth=1, color=seaborn.xkcd_rgb['light grey blue'], zorder=10,
#            alpha=0.9, hatch="")
#     ax.bar(x=np.arange(len(x)) + 4 * bar_width + 0.16, height=y5, label='Lin', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey purple'], linewidth=1, color=seaborn.xkcd_rgb['pale purple'], zorder=10,
#            alpha=0.9, hatch="++")
#     ax.bar(x=np.arange(len(x)) + 5 * bar_width + 0.2, height=y6, label='LACUNA', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['rose'], linewidth=1, color=seaborn.xkcd_rgb['faded pink'], zorder=10,
#            alpha=0.9, hatch="\\\\")
#
#     # 找一下每个柱子的位置
#     # ax.scatter(x=0, y=0.75, marker='X', s=200, color='k', alpha=0.8)
#     # ax.scatter(x=0.14, y=0.75, marker='X', s=200, color='k', alpha=0.8)
#     # ax.scatter(x=0.28, y=0.75, marker='X', s=200, color='k', alpha=0.8)
#     # ax.scatter(x=0.42, y=0.75, marker='X', s=200, color='k', alpha=0.8)
#     # ax.scatter(x=0.56, y=0.75, marker='X', s=200, color='k', alpha=0.8)
#     # ax.scatter(x=0.7, y=0.75, marker='X', s=200, color='k', alpha=0.8)
#     #
#     # ax.scatter(x=0.98, y=0.75, marker='X', s=200, color='k', alpha=0.8)
#     # ax.scatter(x=1.13, y=0.75, marker='X', s=200, color='k', alpha=0.8)
#     # ax.scatter(x=1.27, y=0.75, marker='X', s=200, color='k', alpha=0.8)
#     # ax.scatter(x=1.42, y=0.75, marker='X', s=200, color='k', alpha=0.8)
#     # ax.scatter(x=1.55, y=0.75, marker='X', s=200, color='k', alpha=0.8)
#     # ax.scatter(x=1.69, y=0.75, marker='X', s=200, color='k', alpha=0.8)
#     #
#     # ax.scatter(x=2, y=0.75, marker='X', s=200, color='k', alpha=0.8)
#     # ax.scatter(x=2.14, y=0.75, marker='X', s=200, color='k', alpha=0.8)
#     # ax.scatter(x=2.28, y=0.75, marker='X', s=200, color='k', alpha=0.8)
#     # ax.scatter(x=2.42, y=0.75, marker='X', s=200, color='k', alpha=0.8)
#     # ax.scatter(x=2.56, y=0.75, marker='X', s=200, color='k', alpha=0.8)
#     # ax.scatter(x=2.7, y=0.75, marker='X', s=200, color='k', alpha=0.8)
#
#     # 最大最小值
#     p = r"C:\Users\WHT\Desktop\不能颓鸭\gra\gra\PRF_S.xlsx"
#     df = pd.read_excel(p)
#     xx = df['x'].values
#     yy1 = df['min'].values
#     yy2 = df['max'].values
#     # ax.scatter(x=xx, y=yy1, marker='^', s=40, color='k', alpha=0.5,zorder=12)
#     # ax.scatter(x=xx, y=yy2, marker='v', s=40, color='k', alpha=0.5,zorder=12)
#     ax.vlines(x=xx, ymin=yy1, ymax=yy2, color='k', alpha=0.5, linewidth=2, zorder=12)
#     ax.hlines(y=yy1, xmin=xx - 0.03, xmax=xx + 0.03, color='k', alpha=0.6, linewidth=2, zorder=12)
#     ax.hlines(y=yy2, xmin=xx - 0.03, xmax=xx + 0.03, color='k', alpha=0.6, linewidth=2, zorder=12)
#
#     font = {'family': 'Times New Roman',
#             'weight': 'normal',
#             'size': 13
#             }
#     # plt.legend(loc='upper left', prop=font)
#     # plt.grid(axis="y", alpha=0.8, linestyle=':')
#
#     # 图例：设置位置
#     box = ax.get_position()
#     ax.set_position([box.x0, box.y0, box.width, box.height * 0.8])
#     # ax.legend(loc='center left', bbox_to_anchor=(-0.028, 1.29), ncol=3, prop=font)
#     ax.legend(loc='center left', bbox_to_anchor=(-0.02, 1.19), ncol=6, prop=font)
#     plt.grid(axis="y", alpha=0.8, linestyle=':')
#
#     plt.savefig(str(name) + '.pdf')
#
#     plt.show()


##===========================Eva_addVul:包括最大最小值============================
#画往不同模型中添加数据的不同指标的不同CWE类型平均数的对比（vuldeepecker）,并标有最大最小值
def graphAV1(path, name):
    df = pd.read_excel(path)
    x = df['value'].values
    # 平均值
    y1 = df['Zhou'].values
    y2 = df['Zvd'].values
    y3 = df['Serina'].values
    y4 = df['LACUNA'].values
    # 最小值
    s1 = df['sZhou'].values
    s2 = df['sZvd'].values
    s3 = df['sSerina'].values
    s4 = df['sLACUNA'].values
    # 最大值
    b1 = df['bZhou'].values
    b2 = df['bZvd'].values
    b3 = df['bSerina'].values
    b4 = df['bLACUNA'].values

    fig = plt.figure(figsize=(12, 3), dpi=80)
    ax = fig.add_axes([0.12, 0.25, 0.8, 0.5], zorder=11)

    ax.set_xticks(np.arange(0, 4, 1) + 0.22)
    ax.set_xticklabels(x, fontdict={'horizontalalignment': 'center', 'size': 22,'family': 'Arial'})
    ax.set_yticks(np.arange(-0.1, 0.31, 0.1))
    ax.set_yticklabels([-10, 0, 10, 20, 30],
                       fontdict={'horizontalalignment': 'right', 'size': 22,'family': 'Arial'})
    ax.set_ylim((-0.1, 0.31))
    ax.set_ylabel('% of improvement', fontsize=16,fontdict={'family': 'Arial'})

    bar_width = 0.1
    # ax.bar(x=np.arange(len(x)), height=y1, width=bar_width, label='ZHOU et al.',
    #        edgecolor=seaborn.xkcd_rgb['grey'], linewidth=1, color=seaborn.xkcd_rgb['greenish grey'], zorder=11,
    #        alpha=0.9, hatch="////", align="center")
    # ax.bar(x=np.arange(len(x)) + bar_width + 0.04, height=y2, width=bar_width, label='ZvD',
    #        edgecolor=seaborn.xkcd_rgb['golden rod'], linewidth=1, color=seaborn.xkcd_rgb['sunflower'], zorder=11,
    #        alpha=0.9, hatch="xx")
    # ax.bar(x=np.arange(len(x)) + 2 * bar_width + 0.08, height=y3, width=bar_width, label='SABETTA et al.',
    #        edgecolor=seaborn.xkcd_rgb['grey blue'], linewidth=1, color=seaborn.xkcd_rgb['cool blue'], zorder=11,
    #        alpha=0.9, hatch="")
    # ax.bar(x=np.arange(len(x)) + 3 * bar_width + 0.12, height=y4, width=bar_width, label='FUNDED',
    #        edgecolor=seaborn.xkcd_rgb['orangeish'], linewidth=1, color=seaborn.xkcd_rgb['peach'], zorder=11,
    #        alpha=0.9, hatch="-/")

    ax.bar(x=np.arange(len(x)), height=y1, label='ZHOU et al.', width=bar_width,
           linewidth=1, edgecolor='#D3D3D3', color='#ede4fb', zorder=10, alpha=0.9, hatch="")
    ax.bar(x=np.arange(len(x)) + bar_width + 0.04, height=y2, label='ZvD', width=bar_width,
           linewidth=1, edgecolor='#a79bbe', color='#c5b4e0', zorder=10,
           alpha=0.9, hatch="")
    ax.bar(x=np.arange(len(x)) + 2 * bar_width + 0.08, height=y3, label='SABETTA et al.', width=bar_width,
           linewidth=1, edgecolor='#655784', color='#9c86c6', zorder=10,
           alpha=0.9, hatch="")
    ax.bar(x=np.arange(len(x)) + 3 * bar_width + 0.12, height=y4, label='FUNDED', width=bar_width,
           linewidth=1, color='#735bac', zorder=10)

    # 最大最小值
    ax.hlines(y=s1, xmin=np.arange(len(x)) - 0.03, xmax=np.arange(len(x)) + 0.03, color='k', alpha=0.6, linewidth=2,
              zorder=12)
    ax.hlines(y=s2, xmin=np.arange(len(x)) + bar_width + 0.04 - 0.03, xmax=np.arange(len(x)) + bar_width + 0.04 + 0.03,
              color='k', alpha=0.6, linewidth=2.5, zorder=12)
    ax.hlines(y=s3, xmin=np.arange(len(x)) + 2 * bar_width + 0.08 - 0.03,
              xmax=np.arange(len(x)) + 2 * bar_width + 0.08 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
    ax.hlines(y=s4, xmin=np.arange(len(x)) + 3 * bar_width + 0.12 - 0.03,
              xmax=np.arange(len(x)) + 3 * bar_width + 0.12 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)

    ax.hlines(y=b1, xmin=np.arange(len(x)) - 0.03, xmax=np.arange(len(x)) + 0.03, color='k', alpha=0.6, linewidth=2,
              zorder=12)
    ax.hlines(y=b2, xmin=np.arange(len(x)) + bar_width + 0.04 - 0.03, xmax=np.arange(len(x)) + bar_width + 0.04 + 0.03,
              color='k', alpha=0.6, linewidth=2.5, zorder=12)
    ax.hlines(y=b3, xmin=np.arange(len(x)) + 2 * bar_width + 0.08 - 0.03,
              xmax=np.arange(len(x)) + 2 * bar_width + 0.08 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
    ax.hlines(y=b4, xmin=np.arange(len(x)) + 3 * bar_width + 0.12 - 0.03,
              xmax=np.arange(len(x)) + 3 * bar_width + 0.12 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)

    ax.vlines(x=np.arange(len(x)), ymin=s1, ymax=b1, color='k', alpha=0.6, linewidth=2, zorder=12)
    ax.vlines(x=np.arange(len(x)) + 1 * bar_width + 0.04, ymin=s2, ymax=b2, color='k', alpha=0.6, linewidth=2,
              zorder=12)
    ax.vlines(x=np.arange(len(x)) + 2 * bar_width + 0.08, ymin=s3, ymax=b3, color='k', alpha=0.6, linewidth=2,
              zorder=12)
    ax.vlines(x=np.arange(len(x)) + 3 * bar_width + 0.12, ymin=s4, ymax=b4, color='k', alpha=0.6, linewidth=2,
              zorder=12)

    font = {'family':'Arial',
            'weight': 'light',
            'size': 22
            }

    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width, box.height * 0.8])
    ax.legend(loc='center left', bbox_to_anchor=(-0.02, 1.23), ncol=4, prop=font, columnspacing=1.4, handletextpad=0.1,
              handlelength=2)
    plt.grid(axis="y", alpha=0.8, linestyle=':')

    plt.savefig(str(name) + '.pdf')

    plt.show()


##===========================Eva_addUVul:包括最大最小值============================
#画往不同模型中添加数据的不同指标的不同CWE类型平均数的对比（uvuldeepecker）,并标有最大最小值
def graphAUV1(path, name):
    df = pd.read_excel(path)
    x = df['value'].values
    # 平均值
    y1 = df['Zhou'].values
    y2 = df['Zvd'].values
    y3 = df['Serina'].values
    y4 = df['LACUNA'].values
    # 最小值
    s1 = df['sZhou'].values
    s2 = df['sZvd'].values
    s3 = df['sSerina'].values
    s4 = df['sLACUNA'].values
    # 最大值
    b1 = df['bZhou'].values
    b2 = df['bZvd'].values
    b3 = df['bSerina'].values
    b4 = df['bLACUNA'].values

    fig = plt.figure(figsize=(12, 3), dpi=80)
    ax = fig.add_axes([0.12, 0.25, 0.8, 0.5], zorder=11)

    ax.set_xticks(np.arange(0, 4, 1) + 0.22)
    ax.set_xticklabels(x, fontdict={'horizontalalignment': 'center', 'size': 22,'family': 'Arial'})
    ax.set_yticks(np.arange(-0.1, 0.36, 0.1))
    ax.set_yticklabels([-10, 0, 10, 20, 30],
                       fontdict={'horizontalalignment': 'right', 'size': 22,'family': 'Arial'})
    ax.set_ylim((-0.1, 0.36))
    ax.set_ylabel('% of improvement', fontsize=16,fontdict={'family': 'Arial'})

    bar_width = 0.1
    # ax.bar(x=np.arange(len(x)), height=y1, width=bar_width, label='ZHOU et al.',
    #        edgecolor=seaborn.xkcd_rgb['tan'], linewidth=1, color=seaborn.xkcd_rgb['yellow tan'], zorder=11,
    #        alpha=0.9, hatch="////", align="center")
    # ax.bar(x=np.arange(len(x)) + bar_width + 0.04, height=y2, width=bar_width, label='ZvD',
    #        edgecolor=seaborn.xkcd_rgb['grey green'], linewidth=1, color=seaborn.xkcd_rgb['light grey green'], zorder=11,
    #        alpha=0.9, hatch="xx")
    # ax.bar(x=np.arange(len(x)) + 2 * bar_width + 0.08, height=y3, width=bar_width, label='SABETTA et al.',
    #        edgecolor=seaborn.xkcd_rgb['grey blue'], linewidth=1, color=seaborn.xkcd_rgb['light grey blue'], zorder=11,
    #        alpha=0.9, hatch="")
    # ax.bar(x=np.arange(len(x)) + 3 * bar_width + 0.12, height=y4, width=bar_width, label='FUNDED',
    #        edgecolor=seaborn.xkcd_rgb['grey purple'], linewidth=1, color=seaborn.xkcd_rgb['pale purple'], zorder=11,
    #        alpha=0.9, hatch="\\\\")

    ax.bar(x=np.arange(len(x)), height=y1, label='ZHOU et al.', width=bar_width,
           linewidth=1, edgecolor='#D3D3D3', color='#ede4fb', zorder=10, alpha=0.9, hatch="")
    ax.bar(x=np.arange(len(x)) + bar_width + 0.04, height=y2, label='ZvD', width=bar_width,
           linewidth=1, edgecolor='#a79bbe', color='#c5b4e0', zorder=10,
           alpha=0.9, hatch="")
    ax.bar(x=np.arange(len(x)) + 2 * bar_width + 0.08, height=y3, label='SABETTA et al.', width=bar_width,
           linewidth=1, edgecolor='#655784', color='#9c86c6', zorder=10,
           alpha=0.9, hatch="")
    ax.bar(x=np.arange(len(x)) + 3 * bar_width + 0.12, height=y4, label='FUNDED', width=bar_width,
           linewidth=1, color='#735bac', zorder=10)

    # 最大最小值
    ax.hlines(y=s1, xmin=np.arange(len(x)) - 0.03, xmax=np.arange(len(x)) + 0.03, color='k', alpha=0.6, linewidth=2,
              zorder=12)
    ax.hlines(y=s2, xmin=np.arange(len(x)) + bar_width + 0.04 - 0.03, xmax=np.arange(len(x)) + bar_width + 0.04 + 0.03,
              color='k', alpha=0.6, linewidth=2.5, zorder=12)
    ax.hlines(y=s3, xmin=np.arange(len(x)) + 2 * bar_width + 0.08 - 0.03,
              xmax=np.arange(len(x)) + 2 * bar_width + 0.08 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
    ax.hlines(y=s4, xmin=np.arange(len(x)) + 3 * bar_width + 0.12 - 0.03,
              xmax=np.arange(len(x)) + 3 * bar_width + 0.12 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)

    ax.hlines(y=b1, xmin=np.arange(len(x)) - 0.03, xmax=np.arange(len(x)) + 0.03, color='k', alpha=0.6, linewidth=2,
              zorder=12)
    ax.hlines(y=b2, xmin=np.arange(len(x)) + bar_width + 0.04 - 0.03, xmax=np.arange(len(x)) + bar_width + 0.04 + 0.03,
              color='k', alpha=0.6, linewidth=2.5, zorder=12)
    ax.hlines(y=b3, xmin=np.arange(len(x)) + 2 * bar_width + 0.08 - 0.03,
              xmax=np.arange(len(x)) + 2 * bar_width + 0.08 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
    ax.hlines(y=b4, xmin=np.arange(len(x)) + 3 * bar_width + 0.12 - 0.03,
              xmax=np.arange(len(x)) + 3 * bar_width + 0.12 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)

    ax.vlines(x=np.arange(len(x)), ymin=s1, ymax=b1, color='k', alpha=0.6, linewidth=2, zorder=12)
    ax.vlines(x=np.arange(len(x)) + 1 * bar_width + 0.04, ymin=s2, ymax=b2, color='k', alpha=0.6, linewidth=2,
              zorder=12)
    ax.vlines(x=np.arange(len(x)) + 2 * bar_width + 0.08, ymin=s3, ymax=b3, color='k', alpha=0.6, linewidth=2,
              zorder=12)
    ax.vlines(x=np.arange(len(x)) + 3 * bar_width + 0.12, ymin=s4, ymax=b4, color='k', alpha=0.6, linewidth=2,
              zorder=12)

    font = {'family':'Arial',
            'weight': 'normal',
            'size': 22
            }

    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width, box.height * 0.8])
    ax.legend(loc='center left', bbox_to_anchor=(-0.02, 1.23), ncol=4, prop=font, columnspacing=1.4, handletextpad=0.1,
              handlelength=2)
    plt.grid(axis="y", alpha=0.8, linestyle=':')

    plt.savefig(str(name) + '.pdf')

    plt.show()


# ##===========================Eva_addLACUNA:包括最大最小值============================
# def graphAL1(path, name):
#     df = pd.read_excel(path)
#     x = df['value'].values
#     # 平均值
#     y1 = df['Zhou'].values
#     y2 = df['Zvd'].values
#     y3 = df['Serina'].values
#     y4 = df['LACUNA'].values
#     # 最小值
#     s1 = df['sZhou'].values
#     s2 = df['sZvd'].values
#     s3 = df['sSerina'].values
#     s4 = df['sLACUNA'].values
#     # 最大值
#     b1 = df['bZhou'].values
#     b2 = df['bZvd'].values
#     b3 = df['bSerina'].values
#     b4 = df['bLACUNA'].values
#
#     fig = plt.figure(figsize=(12, 3), dpi=80)
#     ax = fig.add_axes([0.12, 0.25, 0.8, 0.5], zorder=11)
#
#     ax.set_xticks(np.arange(0, 4, 1) + 0.22)
#     ax.set_xticklabels(x, fontdict={'horizontalalignment': 'center', 'size': 16, 'weight': 700})
#     ax.set_yticks(np.arange(-0.1, 0.22, 0.1))
#     ax.set_yticklabels([-0.1, 0, 0.1, 0.2],
#                        fontdict={'horizontalalignment': 'right', 'size': 16, 'weight': 700})
#     ax.set_ylim((-0.1, 0.22))
#
#     bar_width = 0.1
#     ax.bar(x=np.arange(len(x)), height=y1, width=bar_width, label='Zhou',
#            edgecolor=seaborn.xkcd_rgb['tan'], linewidth=1, color=seaborn.xkcd_rgb['yellow tan'], zorder=11,
#            alpha=0.9, hatch="////", align="center")
#     ax.bar(x=np.arange(len(x)) + bar_width + 0.04, height=y2, width=bar_width, label='Zvd',
#            edgecolor=seaborn.xkcd_rgb['grey green'], linewidth=1, color=seaborn.xkcd_rgb['light grey green'], zorder=11,
#            alpha=0.9, hatch="xx")
#     ax.bar(x=np.arange(len(x)) + 2 * bar_width + 0.08, height=y3, width=bar_width, label='Sabetta',
#            edgecolor=seaborn.xkcd_rgb['grey blue'], linewidth=1, color=seaborn.xkcd_rgb['light grey blue'], zorder=11,
#            alpha=0.9, hatch="")
#     ax.bar(x=np.arange(len(x)) + 3 * bar_width + 0.12, height=y4, width=bar_width, label='LACUNA',
#            edgecolor=seaborn.xkcd_rgb['grey purple'], linewidth=1, color=seaborn.xkcd_rgb['pale purple'], zorder=11,
#            alpha=0.9, hatch="\\\\")
#
#     # 最大最小值
#     ax.hlines(y=s1, xmin=np.arange(len(x)) - 0.03, xmax=np.arange(len(x)) + 0.03, color='k', alpha=0.6, linewidth=2,
#               zorder=12)
#     ax.hlines(y=s2, xmin=np.arange(len(x)) + bar_width + 0.04 - 0.03, xmax=np.arange(len(x)) + bar_width + 0.04 + 0.03,
#               color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=s3, xmin=np.arange(len(x)) + 2 * bar_width + 0.08 - 0.03,
#               xmax=np.arange(len(x)) + 2 * bar_width + 0.08 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=s4, xmin=np.arange(len(x)) + 3 * bar_width + 0.12 - 0.03,
#               xmax=np.arange(len(x)) + 3 * bar_width + 0.12 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#
#     ax.hlines(y=b1, xmin=np.arange(len(x)) - 0.03, xmax=np.arange(len(x)) + 0.03, color='k', alpha=0.6, linewidth=2,
#               zorder=12)
#     ax.hlines(y=b2, xmin=np.arange(len(x)) + bar_width + 0.04 - 0.03, xmax=np.arange(len(x)) + bar_width + 0.04 + 0.03,
#               color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=b3, xmin=np.arange(len(x)) + 2 * bar_width + 0.08 - 0.03,
#               xmax=np.arange(len(x)) + 2 * bar_width + 0.08 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=b4, xmin=np.arange(len(x)) + 3 * bar_width + 0.12 - 0.03,
#               xmax=np.arange(len(x)) + 3 * bar_width + 0.12 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#
#     ax.vlines(x=np.arange(len(x)), ymin=s1, ymax=b1, color='k', alpha=0.6, linewidth=2, zorder=12)
#     ax.vlines(x=np.arange(len(x)) + 1 * bar_width + 0.04, ymin=s2, ymax=b2, color='k', alpha=0.6, linewidth=2,
#               zorder=12)
#     ax.vlines(x=np.arange(len(x)) + 2 * bar_width + 0.08, ymin=s3, ymax=b3, color='k', alpha=0.6, linewidth=2,
#               zorder=12)
#     ax.vlines(x=np.arange(len(x)) + 3 * bar_width + 0.12, ymin=s4, ymax=b4, color='k', alpha=0.6, linewidth=2,
#               zorder=12)
#
#     font = {'family': 'Times New Roman',
#             'weight': 'normal',
#             'size': 15
#             }
#
#     box = ax.get_position()
#     ax.set_position([box.x0, box.y0, box.width, box.height * 0.8])
#     ax.legend(loc='center left', bbox_to_anchor=(0.18, 1.18), ncol=4, prop=font)
#     plt.grid(axis="y", alpha=0.8, linestyle=':')
#
#     plt.savefig(str(name) + '.pdf')
#
#     plt.show()
#
#
# # ===========================Eva_ML_Compare：已废===========================
# def graphMLC(path, name):
#     df = pd.read_excel(path)
#     x = df['value'].values
#     y1 = df['KNN'].values
#     y2 = df['RF'].values
#     y3 = df['LR'].values
#     y4 = df['Ada'].values
#     y5 = df['SVM'].values
#     y6 = df['GB'].values
#     y7 = df['Ensemble'].values
#
#     fig = plt.figure(figsize=(8, 3), dpi=80)
#     # 在bar之后添加线
#     ax = fig.add_axes([0.13, 0.28, 0.8, 0.5], zorder=11)
#
#     ax.set_xticks(np.arange(0, 2, 1) + 0.39)
#     ax.set_xticklabels(x, fontdict={'horizontalalignment': 'center', 'size': 14})
#     ax.set_yticks(np.arange(0, 1.02, 0.2))
#     ax.set_yticklabels(['0%', '20%', '40%', '60%', '80%', '100%'],
#                        fontdict={'horizontalalignment': 'right', 'size': 14})
#     # plt.xlabel('SAP Dataset', fontsize=30, weight=700)
#     # ax.set_ylabel('Accuracy', fontsize=30, weight=700)
#     ax.set_ylim((0, 1.02))
#     # ax.set_xlim((-0.1,1.8))
#
#     # hatch 内部填充形状{'/', '\', '|', '-', '+', 'x', 'o', 'O', '.', '*'}
#     bar_width = 0.1
#     ax.bar(x=np.arange(len(x)), height=y1, label='KNN', width=bar_width, edgecolor=seaborn.xkcd_rgb['tan'],
#            linewidth=1, color=seaborn.xkcd_rgb['yellow tan'], zorder=10, alpha=0.9, hatch="//")
#     ax.bar(x=np.arange(len(x)) + bar_width + 0.03, height=y2, label='RF', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey green'],
#            linewidth=1, color=seaborn.xkcd_rgb['light grey green'], zorder=10, alpha=0.9, hatch="--")
#     ax.bar(x=np.arange(len(x)) + 2 * bar_width + 0.06, height=y3, label='LR', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['coffee'], linewidth=1, color=seaborn.xkcd_rgb['very light brown'], zorder=10,
#            alpha=0.9, hatch="xx", align="center")
#     ax.bar(x=np.arange(len(x)) + 3 * bar_width + 0.09, height=y4, label='Ada', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey blue'], linewidth=1, color=seaborn.xkcd_rgb['light grey blue'], zorder=10,
#            alpha=0.9, hatch="")
#     ax.bar(x=np.arange(len(x)) + 4 * bar_width + 0.12, height=y5, label='SVM', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey purple'], linewidth=1, color=seaborn.xkcd_rgb['pale purple'], zorder=10,
#            alpha=0.9, hatch="||")
#     ax.bar(x=np.arange(len(x)) + 5 * bar_width + 0.15, height=y6, label='GB', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['rose'], linewidth=1, color=seaborn.xkcd_rgb['faded pink'], zorder=10,
#            alpha=0.9, hatch="++")
#     ax.bar(x=np.arange(len(x)) + 6 * bar_width + 0.18, height=y7, label='Ensemble', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['dusty teal'], linewidth=1, color=seaborn.xkcd_rgb['grey teal'], zorder=10,
#            alpha=0.9, hatch="\\\\")
#
#     font = {'family': 'Times New Roman',
#             'weight': 'normal',
#             'size': 10.5
#             }
#     # plt.legend(loc='upper left', prop=font)
#     # plt.grid(axis="y", alpha=0.8, linestyle=':')
#
#     # 图例：设置位置
#     box = ax.get_position()
#     ax.set_position([box.x0, box.y0, box.width, box.height * 0.8])
#     ax.legend(loc='center left', bbox_to_anchor=(-0.08, 1.15), ncol=7, prop=font)
#     # ax.legend(loc='center left', bbox_to_anchor=(0.5, 0.7), ncol=3, prop=font)
#     plt.grid(axis="y", alpha=0.8, linestyle=':')
#
#     plt.savefig(str(name) + '.pdf')
#
#     plt.show()


##===========================sard->sard 的mean,按顺序===========================
#画不同模型的不同指标的不同CWE类型平均数的对比（sard）,并标有最大最小值
def graphSM(path, name):
    df = pd.read_excel(path)
    x = df['value'].values
    # 平均值
    y1 = df['Lin'].values
    y2 = df['VUDDY'].values
    y3 = df['vuldeepecker'].values
    y4 = df['μvuldeepecker'].values
    y5 = df['NIPS'].values
    y6 = df['TDSC'].values
    y7 = df['RGIN'].values
    # 最小值
    s1 = df['sLin'].values
    s2 = df['sVUDDY'].values
    s3 = df['svuldeepecker'].values
    s4 = df['sμvuldeepecker'].values
    s5 = df['sNIPS'].values
    s6 = df['sTDSC'].values
    s7 = df['sRGIN'].values
    # 最大值
    b1 = df['bLin'].values
    b2 = df['bVUDDY'].values
    b3 = df['bvuldeepecker'].values
    b4 = df['bμvuldeepecker'].values
    b5 = df['bNIPS'].values
    b6 = df['bTDSC'].values
    b7 = df['bRGIN'].values

    fig = plt.figure(figsize=(15, 3), dpi=80)
    ax = fig.add_axes([0.12, 0.25, 0.8, 0.6], zorder=11)

    ax.set_xticks(np.arange(0, 4, 1) + 0.33)
    ax.set_xticklabels(x, fontdict={'horizontalalignment': 'center', 'size': 28,'family': 'Arial'})
    ax.set_yticks(np.arange(0, 1.02, 0.2))
    ax.set_yticklabels([0, 0.2, 0.4, 0.6, 0.8, 1],
                       fontdict={'horizontalalignment': 'right', 'size': 24,'family': 'Arial'})
    ax.set_ylim((0, 1.02))
    # ax.set_ylabel('% of value', fontsize=14)
    bar_width = 0.08
    ax.bar(x=np.arange(len(x)), height=y1, label='DEEPBUGS',
           width=bar_width, edgecolor='#D3D3D3',
           linewidth=1, color='#ede5fb', zorder=10,
           alpha=0.9,  align="center")
    ax.bar(x=np.arange(len(x)) + bar_width + 0.03, height=y2, label='VUDDY', width=bar_width,
           edgecolor='#cabfdc',
           linewidth=1, color='#d2c4e9', zorder=10, alpha=0.9, )
    ax.bar(x=np.arange(len(x)) + 2 * bar_width + 0.06, height=y3, label='VULDEEPECKER', width=bar_width,
           edgecolor='#a79bbe',
           linewidth=1, color='#b7a5d8', zorder=10, alpha=0.9)
    ax.bar(x=np.arange(len(x)) + 3 * bar_width + 0.09, height=y4, label='μVULDEEPECKER', width=bar_width,
           edgecolor='#8678a0', linewidth=1, color='#9c86c6', zorder=10,
           alpha=0.9)
    ax.bar(x=np.arange(len(x)) + 4 * bar_width + 0.12, height=y5, label='DEVIGN', width=bar_width,
           edgecolor='#655784', linewidth=1, color='#8169b5', zorder=10,
           alpha=0.9)
    ax.bar(x=np.arange(len(x)) + 5 * bar_width + 0.15, height=y6, label='LIN et al.', width=bar_width,
           edgecolor='#453768', linewidth=1, color='#654ca3', zorder=10,
           alpha=0.9)
    ax.bar(x=np.arange(len(x)) + 6 * bar_width + 0.18, height=y7, label='FUNDED', width=bar_width,
           edgecolor='#261a4d', linewidth=1, color='#473192', zorder=10,
           alpha=0.9)


    # 最大最小值
    ax.hlines(y=s1, xmin=np.arange(len(x)) - 0.03, xmax=np.arange(len(x)) + 0.03, color='k', alpha=0.6, linewidth=2,
              zorder=12)
    ax.hlines(y=s2, xmin=np.arange(len(x)) + bar_width + 0.03 - 0.03, xmax=np.arange(len(x)) + bar_width + 0.04 + 0.03,
              color='k', alpha=0.6, linewidth=2.5, zorder=12)
    ax.hlines(y=s3, xmin=np.arange(len(x)) + 2 * bar_width + 0.06 - 0.03,
              xmax=np.arange(len(x)) + 2 * bar_width + 0.06 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
    ax.hlines(y=s4, xmin=np.arange(len(x)) + 3 * bar_width + 0.09 - 0.03,
              xmax=np.arange(len(x)) + 3 * bar_width + 0.09 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
    ax.hlines(y=s5, xmin=np.arange(len(x)) + 4 * bar_width + 0.12 - 0.03,
              xmax=np.arange(len(x)) + 4 * bar_width + 0.12 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
    ax.hlines(y=s6, xmin=np.arange(len(x)) + 5 * bar_width + 0.15 - 0.03,
              xmax=np.arange(len(x)) + 5 * bar_width + 0.15 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
    ax.hlines(y=s7, xmin=np.arange(len(x)) + 6 * bar_width + 0.18 - 0.03,
              xmax=np.arange(len(x)) + 6 * bar_width + 0.18 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)

    ax.hlines(y=b1, xmin=np.arange(len(x)) - 0.03, xmax=np.arange(len(x)) + 0.03, color='k', alpha=0.6, linewidth=2,
              zorder=12)
    ax.hlines(y=b2, xmin=np.arange(len(x)) + bar_width + 0.03 - 0.03, xmax=np.arange(len(x)) + bar_width + 0.04 + 0.03,
              color='k', alpha=0.6, linewidth=2.5, zorder=12)
    ax.hlines(y=b3, xmin=np.arange(len(x)) + 2 * bar_width + 0.06 - 0.03,
              xmax=np.arange(len(x)) + 2 * bar_width + 0.06 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
    ax.hlines(y=b4, xmin=np.arange(len(x)) + 3 * bar_width + 0.09 - 0.03,
              xmax=np.arange(len(x)) + 3 * bar_width + 0.09 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
    ax.hlines(y=b5, xmin=np.arange(len(x)) + 4 * bar_width + 0.12 - 0.03,
              xmax=np.arange(len(x)) + 4 * bar_width + 0.12 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
    ax.hlines(y=b6, xmin=np.arange(len(x)) + 5 * bar_width + 0.15 - 0.03,
              xmax=np.arange(len(x)) + 5 * bar_width + 0.15 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
    ax.hlines(y=b7, xmin=np.arange(len(x)) + 6 * bar_width + 0.18 - 0.03,
              xmax=np.arange(len(x)) + 6 * bar_width + 0.18 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)


    ax.vlines(x=np.arange(len(x)), ymin=s1, ymax=b1, color='k', alpha=0.6, linewidth=2, zorder=12)
    ax.vlines(x=np.arange(len(x)) + 1 * bar_width + 0.03, ymin=s2, ymax=b2, color='k', alpha=0.6, linewidth=2,
              zorder=12)
    ax.vlines(x=np.arange(len(x)) + 2 * bar_width + 0.06, ymin=s3, ymax=b3, color='k', alpha=0.6, linewidth=2,
              zorder=12)
    ax.vlines(x=np.arange(len(x)) + 3 * bar_width + 0.09, ymin=s4, ymax=b4, color='k', alpha=0.6, linewidth=2,
              zorder=12)
    ax.vlines(x=np.arange(len(x)) + 4 * bar_width + 0.12, ymin=s5, ymax=b5, color='k', alpha=0.6, linewidth=2,
              zorder=12)
    ax.vlines(x=np.arange(len(x)) + 5 * bar_width + 0.15, ymin=s6, ymax=b6, color='k', alpha=0.6, linewidth=2,
              zorder=12)
    ax.vlines(x=np.arange(len(x)) + 6 * bar_width + 0.18, ymin=s7, ymax=b7, color='k', alpha=0.6, linewidth=2,
              zorder=12)

    font = {'family': 'Arial',
            'weight': 'light',
            'size': 20.2
            }

    box = ax.get_position()
    # columnspacing=2
    ax.set_position([box.x0, box.y0, box.width, box.height * 0.8])
    ax.legend(loc='center left', bbox_to_anchor=(-0.06, 1.22), ncol=7, prop=font, columnspacing=0.08, handletextpad=0.045,
              handlelength=0.8)
    plt.grid(axis="y", alpha=0.8, linestyle=':')

    plt.savefig(str(name) + '.pdf')

    plt.show()


##===========================sard->github 的mean,正负===========================
# def graphSGM2(path, name):
#     df = pd.read_excel(path)
#     x = df['value'].values
#
#     # 平均值
#     y1 = df['VUDDY'].values
#     y2 = df['vuldeepecker'].values
#     y3 = df['Deepbugs'].values
#     y4 = df['μvuldeepecker'].values
#     y5 = df['Lin'].values
#     y6 = df['LACUNA'].values
#     # 最小值
#     s1 = df['sVUDDY'].values
#     s2 = df['svuldeepecker'].values
#     s3 = df['sDeepbugs'].values
#     s4 = df['sμvuldeepecker'].values
#     s5 = df['sLin'].values
#     s6 = df['sLACUNA'].values
#     # 最大值
#     b1 = df['bVUDDY'].values
#     b2 = df['bvuldeepecker'].values
#     b3 = df['bDeepbugs'].values
#     b4 = df['bμvuldeepecker'].values
#     b5 = df['bLin'].values
#     b6 = df['bLACUNA'].values
#
#     fig = plt.figure(figsize=(15, 3), dpi=80)
#     ax = fig.add_axes([0.12, 0.25, 0.8, 0.5], zorder=11)
#
#     ax.set_xticks(np.arange(0, 4, 1) + 0.33)
#     ax.set_xticklabels(x, fontdict={'horizontalalignment': 'center', 'size': 16})
#     ax.set_yticks(np.arange(0, 1.02, 0.2))
#     ax.set_yticklabels(['0%', '20%', '40%', '60%', '80%', '100%'],
#                        fontdict={'horizontalalignment': 'right', 'size': 16})
#     ax.set_ylim((0, 1.02))
#     # ax.set_ylabel('% of value', fontsize=14)
#
#     bar_width = 0.1
#
#     ax.bar(x=np.arange(len(x)), height=y1, label='VUDDY', width=bar_width, edgecolor=seaborn.xkcd_rgb['tan'],
#            linewidth=1, color=seaborn.xkcd_rgb['yellow tan'], zorder=10, alpha=0.9, hatch="//")
#     ax.bar(x=np.arange(len(x)) + bar_width + 0.04, height=y2, label='Vuldeepecker', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey green'],
#            linewidth=1, color=seaborn.xkcd_rgb['light grey green'], zorder=10, alpha=0.9, hatch="||")
#     ax.bar(x=np.arange(len(x)) + 2 * bar_width + 0.08, height=y3, label='Deepbugs', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['coffee'], linewidth=1, color=seaborn.xkcd_rgb['very light brown'], zorder=10,
#            alpha=0.9, hatch="xx", align="center")
#     ax.bar(x=np.arange(len(x)) + 3 * bar_width + 0.12, height=y4, label='μVuldeepecker', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey purple'], linewidth=1, color=seaborn.xkcd_rgb['pale purple'], zorder=10,
#            alpha=0.9, hatch="++")
#     ax.bar(x=np.arange(len(x)) + 4 * bar_width + 0.16, height=y5, label='Lin', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey blue'], linewidth=1, color=seaborn.xkcd_rgb['light grey blue'], zorder=10,
#            alpha=0.9, hatch="")
#     ax.bar(x=np.arange(len(x)) + 5 * bar_width + 0.2, height=y6, label='LACUNA', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['rose'], linewidth=1, color=seaborn.xkcd_rgb['faded pink'], zorder=10,
#            alpha=0.9, hatch="\\\\")
#
#     # 最大最小值
#     ax.hlines(y=s1, xmin=np.arange(len(x)) - 0.03, xmax=np.arange(len(x)) + 0.03, color='k', alpha=0.6, linewidth=2,
#               zorder=12)
#     ax.hlines(y=s2, xmin=np.arange(len(x)) + bar_width + 0.04 - 0.03, xmax=np.arange(len(x)) + bar_width + 0.04 + 0.03,
#               color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=s3, xmin=np.arange(len(x)) + 2 * bar_width + 0.08 - 0.03,
#               xmax=np.arange(len(x)) + 2 * bar_width + 0.08 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=s4, xmin=np.arange(len(x)) + 3 * bar_width + 0.12 - 0.03,
#               xmax=np.arange(len(x)) + 3 * bar_width + 0.12 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=s5, xmin=np.arange(len(x)) + 4 * bar_width + 0.16 - 0.03,
#               xmax=np.arange(len(x)) + 4 * bar_width + 0.16 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=s6, xmin=np.arange(len(x)) + 5 * bar_width + 0.2 - 0.03,
#               xmax=np.arange(len(x)) + 5 * bar_width + 0.2 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#
#     ax.hlines(y=b1, xmin=np.arange(len(x)) - 0.03, xmax=np.arange(len(x)) + 0.03, color='k', alpha=0.6, linewidth=2,
#               zorder=12)
#     ax.hlines(y=b2, xmin=np.arange(len(x)) + bar_width + 0.04 - 0.03, xmax=np.arange(len(x)) + bar_width + 0.04 + 0.03,
#               color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=b3, xmin=np.arange(len(x)) + 2 * bar_width + 0.08 - 0.03,
#               xmax=np.arange(len(x)) + 2 * bar_width + 0.08 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=b4, xmin=np.arange(len(x)) + 3 * bar_width + 0.12 - 0.03,
#               xmax=np.arange(len(x)) + 3 * bar_width + 0.12 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=b5, xmin=np.arange(len(x)) + 4 * bar_width + 0.16 - 0.03,
#               xmax=np.arange(len(x)) + 4 * bar_width + 0.16 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=b6, xmin=np.arange(len(x)) + 5 * bar_width + 0.2 - 0.03,
#               xmax=np.arange(len(x)) + 5 * bar_width + 0.2 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#
#     ax.vlines(x=np.arange(len(x)), ymin=s1, ymax=b1, color='k', alpha=0.6, linewidth=2, zorder=12)
#     ax.vlines(x=np.arange(len(x)) + 1 * bar_width + 0.04, ymin=s2, ymax=b2, color='k', alpha=0.6, linewidth=2,
#               zorder=12)
#     ax.vlines(x=np.arange(len(x)) + 2 * bar_width + 0.08, ymin=s3, ymax=b3, color='k', alpha=0.6, linewidth=2,
#               zorder=12)
#     ax.vlines(x=np.arange(len(x)) + 3 * bar_width + 0.12, ymin=s4, ymax=b4, color='k', alpha=0.6, linewidth=2,
#               zorder=12)
#     ax.vlines(x=np.arange(len(x)) + 4 * bar_width + 0.16, ymin=s5, ymax=b5, color='k', alpha=0.6, linewidth=2,
#               zorder=12)
#     ax.vlines(x=np.arange(len(x)) + 5 * bar_width + 0.2, ymin=s6, ymax=b6, color='k', alpha=0.6, linewidth=2, zorder=12)
#
#     font = {'family': 'Times New Roman',
#             'weight': 'light',
#             'size': 17
#             }
#
#     box = ax.get_position()
#     ax.set_position([box.x0, box.y0, box.width, box.height * 0.8])
#     ax.legend(loc='center left', bbox_to_anchor=(-0.05, 1.22), ncol=6, prop=font)
#     plt.grid(axis="y", alpha=0.8, linestyle=':')
#
#     plt.savefig(str(name) + '.pdf')
#
#     plt.show()


##===========================sard->github 的mean,按顺序===========================
#画不同模型的不同指标的不同CWE类型平均数的对比（github）,并标有最大最小值
def graphSGM(path, name):
    #读取数据
    df = pd.read_excel(path)
    x = df['value'].values
    # 平均值
    y1 = df['VUDDY'].values
    y2 = df['RGCN'].values
    y3 = df['μvuldeepecker'].values
    y4 = df['vuldeepecker'].values
    y5 = df['Lin'].values
    y6 = df['TDSC'].values
    y7 = df['NIPS'].values
    y8 = df['RGIN'].values
    # 最小值
    s1 = df['sVUDDY'].values
    s2 = df['sRGCN'].values
    s3 = df['sμvuldeepecker'].values
    s4 = df['svuldeepecker'].values
    s5 = df['sLin'].values
    s6 = df['sTDSC'].values
    s7 = df['sNIPS'].values
    s8 = df['sRGIN'].values
    # 最大值
    b1 = df['bVUDDY'].values
    b2 = df['bRGCN'].values
    b3 = df['bμvuldeepecker'].values
    b4 = df['bvuldeepecker'].values
    b5 = df['bLin'].values
    b6 = df['bTDSC'].values
    b7 = df['bNIPS'].values
    b8 = df['bRGIN'].values

    #设置图层以及轴坐标
    fig = plt.figure(figsize=(15, 3), dpi=80)
    ax = fig.add_axes([0.12, 0.25, 0.8, 0.6], zorder=11)

    ax.set_xticks(np.arange(0, 4, 1) + 0.33)
    ax.set_xticklabels(x, fontdict={'horizontalalignment': 'center', 'size': 28,'family': 'Arial'})
    ax.set_yticks(np.arange(0, 1.02, 0.2))
    ax.set_yticklabels([0, 0.2, 0.4, 0.6, 0.8, 1],
                       fontdict={'horizontalalignment': 'right', 'size': 24,'family': 'Arial'})
    ax.set_ylim((0, 1.02))
    # ax.set_ylabel('% of value', fontsize=14)
    bar_width = 0.08
    # ax.bar(x=np.arange(len(x)), height=y1, label='VUDDY', width=bar_width, edgecolor=seaborn.xkcd_rgb['coffee'],
    #        linewidth=1, color=seaborn.xkcd_rgb['very light brown'], zorder=10,
    #        alpha=0.9, hatch="xx", align="center")
    # ax.bar(x=np.arange(len(x)) + bar_width + 0.03, height=y2, label='RGCN', width=bar_width,
    #        edgecolor=seaborn.xkcd_rgb['tan'],
    #        linewidth=1, color=seaborn.xkcd_rgb['yellow tan'], zorder=10, alpha=0.9, hatch="//")
    # ax.bar(x=np.arange(len(x)) + 2 * bar_width + 0.06, height=y3, label='μVULDEEPECKER', width=bar_width,
    #        edgecolor=seaborn.xkcd_rgb['grey purple'],
    #        linewidth=1, color=seaborn.xkcd_rgb['pale purple'], zorder=10, alpha=0.9, hatch="++")
    # ax.bar(x=np.arange(len(x)) + 3 * bar_width + 0.09, height=y4, label='VULDEEPECKER', width=bar_width,
    #        edgecolor=seaborn.xkcd_rgb['grey green'], linewidth=1, color=seaborn.xkcd_rgb['light grey green'], zorder=10,
    #        alpha=0.9, hatch="||")
    # ax.bar(x=np.arange(len(x)) + 4 * bar_width + 0.12, height=y5, label='DEEPBUGS', width=bar_width,
    #        edgecolor=seaborn.xkcd_rgb['grey blue'], linewidth=1, color=seaborn.xkcd_rgb['light grey blue'], zorder=10,
    #        alpha=0.9, hatch="\\\\")
    # ax.bar(x=np.arange(len(x)) + 5 * bar_width + 0.15, height=y6, label='LIN et al.', width=bar_width,
    #        edgecolor=seaborn.xkcd_rgb['perrywinkle'], linewidth=1, color=seaborn.xkcd_rgb['light violet'], zorder=10,
    #        alpha=0.9, hatch="|\\|")
    # ax.bar(x=np.arange(len(x)) + 6 * bar_width + 0.18, height=y7, label='DEVIGN', width=bar_width,
    #        edgecolor=seaborn.xkcd_rgb['rose'], linewidth=1, color=seaborn.xkcd_rgb['faded pink'], zorder=10,
    #        alpha=0.9, hatch="")
    # ax.bar(x=np.arange(len(x)) + 7 * bar_width + 0.21, height=y8, label='FUNDED', width=bar_width,
    #        edgecolor=seaborn.xkcd_rgb['orangeish'], linewidth=1, color=seaborn.xkcd_rgb['peach'], zorder=10,
    #        alpha=0.9, hatch="-/")

    # ax.bar(x=np.arange(len(x)), height=y1, label='VUDDY', width=bar_width, edgecolor='#D3D3D3',
    #        linewidth=1, color='#ede4fb', zorder=10,alpha=0.9,align="center")
    # ax.bar(x=np.arange(len(x)) + bar_width + 0.03, height=y2, label='RGCN', width=bar_width,
    #        edgecolor='#cfc5e0',
    #        linewidth=1, color='#d6c9ec', zorder=10, alpha=0.9)
    # ax.bar(x=np.arange(len(x)) + 2 * bar_width + 0.06, height=y3, label='μVULDEEPECKER', width=bar_width,
    #        edgecolor='#b1a5c6',
    #        linewidth=1, color='#c0aede', zorder=10, alpha=0.9)
    # ax.bar(x=np.arange(len(x)) + 3 * bar_width + 0.09, height=y4, label='VULDEEPECKER', width=bar_width,
    #        edgecolor='#9487ad', linewidth=1, color='#a994cf', zorder=10,
    #        alpha=0.9)
    # ax.bar(x=np.arange(len(x)) + 4 * bar_width + 0.12, height=y5, label='DEEPBUGS', width=bar_width,
    #        edgecolor='#776994', linewidth=1, color='#927bc1', zorder=10,
    #        alpha=0.9)
    # ax.bar(x=np.arange(len(x)) + 5 * bar_width + 0.15, height=y6, label='LIN et al.', width=bar_width,
    #        edgecolor='#5c4d7b', linewidth=1, color='#7961b0', zorder=10,alpha=0.9)
    # ax.bar(x=np.arange(len(x)) + 6 * bar_width + 0.18, height=y7, label='DEVIGN', width=bar_width,
    #        edgecolor='#413364', linewidth=1, color='#634aa4', zorder=10,
    #        alpha=0.9)
    # ax.bar(x=np.arange(len(x)) + 7 * bar_width + 0.21, height=y8, label='FUNDED', width=bar_width,
    #        edgecolor='#261a4d', linewidth=1, color='#493396', zorder=10,
    #        alpha=0.9)

    #画柱状图
    ax.bar(x=np.arange(len(x)), height=y1, label='VUDDY', width=bar_width,
           edgecolor='#cabfdc',
           linewidth=1, color='#d3c4ea', zorder=10, alpha=0.9, align="center")
    ax.bar(x=np.arange(len(x)) + bar_width + 0.03, height=y2, label='RGCN', width=bar_width,
           edgecolor='#cfc5e0',
           linewidth=1, color='#d6c9ec', zorder=10, alpha=0.9)
    ax.bar(x=np.arange(len(x)) + 2 * bar_width + 0.06, height=y3, label='μVULDEEPECKER', width=bar_width,
           edgecolor='#8678a0',
           linewidth=1, color='#9d87c8', zorder=10, alpha=0.9)
    ax.bar(x=np.arange(len(x)) + 3 * bar_width + 0.09, height=y4, label='VULDEEPECKER', width=bar_width,
           edgecolor='#a79bbe', linewidth=1, color='#b8a5d9', zorder=10,
           alpha=0.9)
    ax.bar(x=np.arange(len(x)) + 4 * bar_width + 0.12, height=y5, label='DEEPBUGS', width=bar_width,
           edgecolor='#D3D3D3', linewidth=1, color='#ede4fb', zorder=10,
           alpha=0.9)
    ax.bar(x=np.arange(len(x)) + 5 * bar_width + 0.15, height=y6, label='LIN et al.', width=bar_width,
           edgecolor='#453768', linewidth=1, color='#674ea7', zorder=10, alpha=0.9)
    ax.bar(x=np.arange(len(x)) + 6 * bar_width + 0.18, height=y7, label='DEVIGN', width=bar_width,
           edgecolor='#655784', linewidth=1, color='#836ab7', zorder=10,
           alpha=0.9)
    ax.bar(x=np.arange(len(x)) + 7 * bar_width + 0.21, height=y8, label='FUNDED', width=bar_width,
           edgecolor='#261a4d', linewidth=1, color='#493396', zorder=10,
           alpha=0.9)

    # 添加最大最小值
    #添加水平线最小值
    ax.hlines(y=s1, xmin=np.arange(len(x)) - 0.03, xmax=np.arange(len(x)) + 0.03, color='k', alpha=0.6, linewidth=2,
              zorder=12)
    ax.hlines(y=s2, xmin=np.arange(len(x)) + bar_width + 0.03 - 0.03, xmax=np.arange(len(x)) + bar_width + 0.04 + 0.03,
              color='k', alpha=0.6, linewidth=2.5, zorder=12)
    ax.hlines(y=s3, xmin=np.arange(len(x)) + 2 * bar_width + 0.06 - 0.03,
              xmax=np.arange(len(x)) + 2 * bar_width + 0.06 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
    ax.hlines(y=s4, xmin=np.arange(len(x)) + 3 * bar_width + 0.09 - 0.03,
              xmax=np.arange(len(x)) + 3 * bar_width + 0.09 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
    ax.hlines(y=s5, xmin=np.arange(len(x)) + 4 * bar_width + 0.12 - 0.03,
              xmax=np.arange(len(x)) + 4 * bar_width + 0.12 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
    ax.hlines(y=s6, xmin=np.arange(len(x)) + 5 * bar_width + 0.15 - 0.03,
              xmax=np.arange(len(x)) + 5 * bar_width + 0.15 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
    ax.hlines(y=s7, xmin=np.arange(len(x)) + 6 * bar_width + 0.18 - 0.03,
              xmax=np.arange(len(x)) + 6 * bar_width + 0.18 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
    ax.hlines(y=s8, xmin=np.arange(len(x)) + 7 * bar_width + 0.21 - 0.03,
              xmax=np.arange(len(x)) + 7 * bar_width + 0.21 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)

    # 添加水平线最大值
    ax.hlines(y=b1, xmin=np.arange(len(x)) - 0.03, xmax=np.arange(len(x)) + 0.03, color='k', alpha=0.6, linewidth=2,
              zorder=12)
    ax.hlines(y=b2, xmin=np.arange(len(x)) + bar_width + 0.03 - 0.03, xmax=np.arange(len(x)) + bar_width + 0.04 + 0.03,
              color='k', alpha=0.6, linewidth=2.5, zorder=12)
    ax.hlines(y=b3, xmin=np.arange(len(x)) + 2 * bar_width + 0.06 - 0.03,
              xmax=np.arange(len(x)) + 2 * bar_width + 0.06 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
    ax.hlines(y=b4, xmin=np.arange(len(x)) + 3 * bar_width + 0.09 - 0.03,
              xmax=np.arange(len(x)) + 3 * bar_width + 0.09 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
    ax.hlines(y=b5, xmin=np.arange(len(x)) + 4 * bar_width + 0.12 - 0.03,
              xmax=np.arange(len(x)) + 4 * bar_width + 0.12 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
    ax.hlines(y=b6, xmin=np.arange(len(x)) + 5 * bar_width + 0.15 - 0.03,
              xmax=np.arange(len(x)) + 5 * bar_width + 0.15 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
    ax.hlines(y=b7, xmin=np.arange(len(x)) + 6 * bar_width + 0.18 - 0.03,
              xmax=np.arange(len(x)) + 6 * bar_width + 0.18 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
    ax.hlines(y=b8, xmin=np.arange(len(x)) + 7 * bar_width + 0.21 - 0.03,
              xmax=np.arange(len(x)) + 7 * bar_width + 0.21 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)

    #添加最大最小值间的垂直线
    ax.vlines(x=np.arange(len(x)), ymin=s1, ymax=b1, color='k', alpha=0.6, linewidth=2, zorder=12)
    ax.vlines(x=np.arange(len(x)) + 1 * bar_width + 0.03, ymin=s2, ymax=b2, color='k', alpha=0.6, linewidth=2,
              zorder=12)
    ax.vlines(x=np.arange(len(x)) + 2 * bar_width + 0.06, ymin=s3, ymax=b3, color='k', alpha=0.6, linewidth=2,
              zorder=12)
    ax.vlines(x=np.arange(len(x)) + 3 * bar_width + 0.09, ymin=s4, ymax=b4, color='k', alpha=0.6, linewidth=2,
              zorder=12)
    ax.vlines(x=np.arange(len(x)) + 4 * bar_width + 0.12, ymin=s5, ymax=b5, color='k', alpha=0.6, linewidth=2,
              zorder=12)
    ax.vlines(x=np.arange(len(x)) + 5 * bar_width + 0.15, ymin=s6, ymax=b6, color='k', alpha=0.6, linewidth=2, zorder=12)
    ax.vlines(x=np.arange(len(x)) + 6 * bar_width + 0.18, ymin=s7, ymax=b7, color='k', alpha=0.6, linewidth=2,
              zorder=12)
    ax.vlines(x=np.arange(len(x)) + 7 * bar_width + 0.21, ymin=s8, ymax=b8, color='k', alpha=0.6, linewidth=2, zorder=12)

    #设置图例
    font = {'family': 'Arial',
            'weight': 'light',
            'size': 19
            }

    box = ax.get_position()
    # columnspacing=2
    ax.set_position([box.x0, box.y0, box.width, box.height * 0.8])
    ax.legend(loc='center left', bbox_to_anchor=(-0.06, 1.22), ncol=8, prop=font, columnspacing=0.15, handletextpad=0.05,
              handlelength=0.6)
    #设置网格线
    plt.grid(axis="y", alpha=0.8, linestyle=':')

    #存为PDF
    plt.savefig(str(name) + '.pdf')

    plt.show()


# ##===========================sard->sard 的mean,按大小===========================
# def graphSM1(path, name):
#     df = pd.read_excel(path)
#     x = df['value'].values
#     # 平均值
#     y1 = df['Deepbugs'].values
#     y2 = df['VUDDY'].values
#     y3 = df['vuldeepecker'].values
#     y4 = df['μvuldeepecker'].values
#     y5 = df['Lin'].values
#     y6 = df['LACUNA'].values
#     # 最小值
#     s1 = df['sDeepbugs'].values
#     s2 = df['sVUDDY'].values
#     s3 = df['svuldeepecker'].values
#     s4 = df['sμvuldeepecker'].values
#     s5 = df['sLin'].values
#     s6 = df['sLACUNA'].values
#     # 最大值
#     b1 = df['bDeepbugs'].values
#     b2 = df['bVUDDY'].values
#     b3 = df['bvuldeepecker'].values
#     b4 = df['bμvuldeepecker'].values
#     b5 = df['bLin'].values
#     b6 = df['bLACUNA'].values
#
#     fig = plt.figure(figsize=(15, 3), dpi=80)
#     ax = fig.add_axes([0.12, 0.25, 0.8, 0.5], zorder=11)
#
#     ax.set_xticks(np.arange(0, 4, 1) + 0.33)
#     ax.set_xticklabels(x, fontdict={'horizontalalignment': 'center', 'size': 16})
#     ax.set_yticks(np.arange(0, 1.02, 0.2))
#     ax.set_yticklabels(['0%', '20%', '40%', '60%', '80%', '100%'],
#                        fontdict={'horizontalalignment': 'right', 'size': 16})
#     ax.set_ylim((0, 1.02))
#     # ax.set_ylabel('% of value', fontsize=14)
#
#     bar_width = 0.1
#     ax.bar(x=np.arange(len(x)), height=y1, label='Deepbugs', width=bar_width, edgecolor=seaborn.xkcd_rgb['tan'],
#            linewidth=1, color=seaborn.xkcd_rgb['yellow tan'], zorder=10, alpha=0.9, hatch="//")
#     ax.bar(x=np.arange(len(x)) + bar_width + 0.04, height=y2, label='VUDDY', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey green'],
#            linewidth=1, color=seaborn.xkcd_rgb['light grey green'], zorder=10, alpha=0.9, hatch="||")
#     ax.bar(x=np.arange(len(x)) + 2 * bar_width + 0.08, height=y3, label='Vuldeepecker', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['coffee'], linewidth=1, color=seaborn.xkcd_rgb['very light brown'], zorder=10,
#            alpha=0.9, hatch="xx", align="center")
#     ax.bar(x=np.arange(len(x)) + 3 * bar_width + 0.12, height=y4, label='μVuldeepecker', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey blue'], linewidth=1, color=seaborn.xkcd_rgb['light grey blue'], zorder=10,
#            alpha=0.9, hatch="")
#     ax.bar(x=np.arange(len(x)) + 4 * bar_width + 0.16, height=y5, label='Lin', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey purple'], linewidth=1, color=seaborn.xkcd_rgb['pale purple'], zorder=10,
#            alpha=0.9, hatch="++")
#     ax.bar(x=np.arange(len(x)) + 5 * bar_width + 0.2, height=y6, label='LACUNA', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['rose'], linewidth=1, color=seaborn.xkcd_rgb['faded pink'], zorder=10,
#            alpha=0.9, hatch="\\\\")
#
#     # 最大最小值
#     ax.hlines(y=s1, xmin=np.arange(len(x)) - 0.03, xmax=np.arange(len(x)) + 0.03, color='k', alpha=0.6, linewidth=2,
#               zorder=12)
#     ax.hlines(y=s2, xmin=np.arange(len(x)) + bar_width + 0.04 - 0.03, xmax=np.arange(len(x)) + bar_width + 0.04 + 0.03,
#               color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=s3, xmin=np.arange(len(x)) + 2 * bar_width + 0.08 - 0.03,
#               xmax=np.arange(len(x)) + 2 * bar_width + 0.08 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=s4, xmin=np.arange(len(x)) + 3 * bar_width + 0.12 - 0.03,
#               xmax=np.arange(len(x)) + 3 * bar_width + 0.12 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=s5, xmin=np.arange(len(x)) + 4 * bar_width + 0.16 - 0.03,
#               xmax=np.arange(len(x)) + 4 * bar_width + 0.16 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=s6, xmin=np.arange(len(x)) + 5 * bar_width + 0.2 - 0.03,
#               xmax=np.arange(len(x)) + 5 * bar_width + 0.2 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#
#     ax.hlines(y=b1, xmin=np.arange(len(x)) - 0.03, xmax=np.arange(len(x)) + 0.03, color='k', alpha=0.6, linewidth=2,
#               zorder=12)
#     ax.hlines(y=b2, xmin=np.arange(len(x)) + bar_width + 0.04 - 0.03, xmax=np.arange(len(x)) + bar_width + 0.04 + 0.03,
#               color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=b3, xmin=np.arange(len(x)) + 2 * bar_width + 0.08 - 0.03,
#               xmax=np.arange(len(x)) + 2 * bar_width + 0.08 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=b4, xmin=np.arange(len(x)) + 3 * bar_width + 0.12 - 0.03,
#               xmax=np.arange(len(x)) + 3 * bar_width + 0.12 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=b5, xmin=np.arange(len(x)) + 4 * bar_width + 0.16 - 0.03,
#               xmax=np.arange(len(x)) + 4 * bar_width + 0.16 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=b6, xmin=np.arange(len(x)) + 5 * bar_width + 0.2 - 0.03,
#               xmax=np.arange(len(x)) + 5 * bar_width + 0.2 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#
#     ax.vlines(x=np.arange(len(x)), ymin=s1, ymax=b1, color='k', alpha=0.6, linewidth=2, zorder=12)
#     ax.vlines(x=np.arange(len(x)) + 1 * bar_width + 0.04, ymin=s2, ymax=b2, color='k', alpha=0.6, linewidth=2,
#               zorder=12)
#     ax.vlines(x=np.arange(len(x)) + 2 * bar_width + 0.08, ymin=s3, ymax=b3, color='k', alpha=0.6, linewidth=2,
#               zorder=12)
#     ax.vlines(x=np.arange(len(x)) + 3 * bar_width + 0.12, ymin=s4, ymax=b4, color='k', alpha=0.6, linewidth=2,
#               zorder=12)
#     ax.vlines(x=np.arange(len(x)) + 4 * bar_width + 0.16, ymin=s5, ymax=b5, color='k', alpha=0.6, linewidth=2,
#               zorder=12)
#     ax.vlines(x=np.arange(len(x)) + 5 * bar_width + 0.2, ymin=s6, ymax=b6, color='k', alpha=0.6, linewidth=2, zorder=12)
#
#     df1 = pd.read_excel(r'C:\Users\WHT\Desktop\不能颓鸭\gra\gra\SM1_P.xlsx')
#     x1 = df1['value'].values
#     y11 = df1['vuldeepecker'].values
#     y21 = df1['μvuldeepecker'].values
#     y31 = df1['Lin'].values
#     y41 = df1['LACUNA'].values
#     y51 = df1['Deepbugs'].values
#     y61 = df1['VUDDY'].values
#     # 最小值
#     s11 = df1['svuldeepecker'].values
#     s21 = df1['sμvuldeepecker'].values
#     s31 = df1['sLin'].values
#     s41 = df1['sLACUNA'].values
#     s51 = df1['sDeepbugs'].values
#     s61 = df1['sVUDDY'].values
#     # 最大值
#     b11 = df1['bvuldeepecker'].values
#     b21 = df1['bμvuldeepecker'].values
#     b31 = df1['bLin'].values
#     b41 = df1['bLACUNA'].values
#     b51 = df1['bDeepbugs'].values
#     b61 = df1['bVUDDY'].values
#
#     bar_width = 0.1
#     ax.bar(x=np.arange(len(x1)), height=y11, width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['coffee'], linewidth=1, color=seaborn.xkcd_rgb['very light brown'], zorder=10,
#            alpha=0.9, hatch="xx", align="center")
#     ax.bar(x=np.arange(len(x1)) + 1 * bar_width + 0.04, height=y21, width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey blue'], linewidth=1, color=seaborn.xkcd_rgb['light grey blue'], zorder=10,
#            alpha=0.9, hatch="")
#     ax.bar(x=np.arange(len(x1)) + 2 * bar_width + 0.08, height=y31, width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey purple'], linewidth=1, color=seaborn.xkcd_rgb['pale purple'], zorder=10,
#            alpha=0.9, hatch="++")
#     ax.bar(x=np.arange(len(x1)) + 3 * bar_width + 0.12, height=y41, width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['rose'], linewidth=1, color=seaborn.xkcd_rgb['faded pink'], zorder=10,
#            alpha=0.9, hatch="\\\\")
#     ax.bar(x=np.arange(len(x1)) + 4 * bar_width + 0.16, height=y51, width=bar_width, edgecolor=seaborn.xkcd_rgb['tan'],
#            linewidth=1, color=seaborn.xkcd_rgb['yellow tan'], zorder=10, alpha=0.9, hatch="//")
#     ax.bar(x=np.arange(len(x1)) + 5 * bar_width + 0.2, height=y61, width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey green'],
#            linewidth=1, color=seaborn.xkcd_rgb['light grey green'], zorder=10, alpha=0.9, hatch="||")
#
#     ax.hlines(y=s11, xmin=np.arange(len(x1)) - 0.03, xmax=np.arange(len(x1)) + 0.03, color='k', alpha=0.6, linewidth=2,
#               zorder=12)
#     ax.hlines(y=s21, xmin=np.arange(len(x1)) + bar_width + 0.04 - 0.03,
#               xmax=np.arange(len(x1)) + bar_width + 0.04 + 0.03,
#               color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=s31, xmin=np.arange(len(x1)) + 2 * bar_width + 0.08 - 0.03,
#               xmax=np.arange(len(x1)) + 2 * bar_width + 0.08 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=s41, xmin=np.arange(len(x1)) + 3 * bar_width + 0.12 - 0.03,
#               xmax=np.arange(len(x1)) + 3 * bar_width + 0.12 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=s51, xmin=np.arange(len(x1)) + 4 * bar_width + 0.16 - 0.03,
#               xmax=np.arange(len(x1)) + 4 * bar_width + 0.16 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=s61, xmin=np.arange(len(x1)) + 5 * bar_width + 0.2 - 0.03,
#               xmax=np.arange(len(x1)) + 5 * bar_width + 0.2 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#
#     ax.hlines(y=b11, xmin=np.arange(len(x1)) - 0.03, xmax=np.arange(len(x1)) + 0.03, color='k', alpha=0.6, linewidth=2,
#               zorder=12)
#     ax.hlines(y=b21, xmin=np.arange(len(x1)) + bar_width + 0.04 - 0.03,
#               xmax=np.arange(len(x1)) + bar_width + 0.04 + 0.03,
#               color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=b31, xmin=np.arange(len(x1)) + 2 * bar_width + 0.08 - 0.03,
#               xmax=np.arange(len(x1)) + 2 * bar_width + 0.08 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=b41, xmin=np.arange(len(x1)) + 3 * bar_width + 0.12 - 0.03,
#               xmax=np.arange(len(x1)) + 3 * bar_width + 0.12 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=b51, xmin=np.arange(len(x1)) + 4 * bar_width + 0.16 - 0.03,
#               xmax=np.arange(len(x1)) + 4 * bar_width + 0.16 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=b61, xmin=np.arange(len(x1)) + 5 * bar_width + 0.2 - 0.03,
#               xmax=np.arange(len(x1)) + 5 * bar_width + 0.2 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#
#     ax.vlines(x=np.arange(len(x1)), ymin=s11, ymax=b11, color='k', alpha=0.6, linewidth=2, zorder=12)
#     ax.vlines(x=np.arange(len(x1)) + 1 * bar_width + 0.04, ymin=s21, ymax=b21, color='k', alpha=0.6, linewidth=2,
#               zorder=12)
#     ax.vlines(x=np.arange(len(x1)) + 2 * bar_width + 0.08, ymin=s31, ymax=b31, color='k', alpha=0.6, linewidth=2,
#               zorder=12)
#     ax.vlines(x=np.arange(len(x1)) + 3 * bar_width + 0.12, ymin=s41, ymax=b41, color='k', alpha=0.6, linewidth=2,
#               zorder=12)
#     ax.vlines(x=np.arange(len(x1)) + 4 * bar_width + 0.16, ymin=s51, ymax=b51, color='k', alpha=0.6, linewidth=2,
#               zorder=12)
#     ax.vlines(x=np.arange(len(x1)) + 5 * bar_width + 0.2, ymin=s61, ymax=b61, color='k', alpha=0.6, linewidth=2,
#               zorder=12)
#
#     font = {'family': 'Times New Roman',
#             'weight': 'light',
#             'size': 17
#             }
#
#     box = ax.get_position()
#     ax.set_position([box.x0, box.y0, box.width, box.height * 0.8])
#     ax.legend(loc='center left', bbox_to_anchor=(-0.05, 1.22), ncol=6, prop=font)
#     plt.grid(axis="y", alpha=0.8, linestyle=':')
#
#     plt.savefig(str(name) + '.pdf')
#
#     plt.show()
#
#
# ##===========================sard->sard 的mean,正负轴===========================
# def graphSM2(path, name):
#     df = pd.read_excel(path)
#     x = df['value'].values
#     # 平均值
#     y1 = df['Deepbugs'].values
#     y2 = df['VUDDY'].values
#     y3 = df['vuldeepecker'].values
#     y4 = df['μvuldeepecker'].values
#     y5 = df['Lin'].values
#     y6 = df['LACUNA'].values
#     # 最小值
#     s1 = df['sDeepbugs'].values
#     s2 = df['sVUDDY'].values
#     s3 = df['svuldeepecker'].values
#     s4 = df['sμvuldeepecker'].values
#     s5 = df['sLin'].values
#     s6 = df['sLACUNA'].values
#     # 最大值
#     b1 = df['bDeepbugs'].values
#     b2 = df['bVUDDY'].values
#     b3 = df['bvuldeepecker'].values
#     b4 = df['bμvuldeepecker'].values
#     b5 = df['bLin'].values
#     b6 = df['bLACUNA'].values
#
#     fig = plt.figure(figsize=(15, 3.5), dpi=80)
#     ax = fig.add_axes([0.12, 0.25, 0.8, 0.5], zorder=11)
#
#     ax.set_xticks(np.arange(0, 4, 1) + 0.33)
#     ax.set_xticklabels(x, fontdict={'horizontalalignment': 'center', 'size': 20})
#     ax.set_yticks(np.arange(0, 0.32, 0.05))
#     ax.set_yticklabels(['0%', '40%', '80%', '85%', '90%', '95%', '100%'],
#                        fontdict={'horizontalalignment': 'right', 'size': 20})
#     ax.set_ylim((0, 0.32))
#
#     bar_width = 0.1
#     ax.bar(x=np.arange(len(x)), height=y1, label='Deepbugs', width=bar_width, edgecolor=seaborn.xkcd_rgb['coffee'],
#            linewidth=1, color=seaborn.xkcd_rgb['very light brown'], zorder=10,
#            alpha=0.9, hatch="xx", align="center")
#     ax.bar(x=np.arange(len(x)) + bar_width + 0.04, height=y2, label='VUDDY', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['tan'],
#            linewidth=1, color=seaborn.xkcd_rgb['yellow tan'], zorder=10, alpha=0.9, hatch="//")
#     ax.bar(x=np.arange(len(x)) + 2 * bar_width + 0.08, height=y3, label='Vuldeepecker', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey green'],
#            linewidth=1, color=seaborn.xkcd_rgb['light grey green'], zorder=10, alpha=0.9, hatch="||")
#     ax.bar(x=np.arange(len(x)) + 3 * bar_width + 0.12, height=y4, label='μVuldeepecker', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey purple'], linewidth=1, color=seaborn.xkcd_rgb['pale purple'], zorder=10,
#            alpha=0.9, hatch="++")
#     ax.bar(x=np.arange(len(x)) + 4 * bar_width + 0.16, height=y5, label='Lin et al.', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey blue'], linewidth=1, color=seaborn.xkcd_rgb['light grey blue'], zorder=10,
#            alpha=0.9, hatch="")
#     ax.bar(x=np.arange(len(x)) + 5 * bar_width + 0.2, height=y6, label='FENCED', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['rose'], linewidth=1, color=seaborn.xkcd_rgb['faded pink'], zorder=10,
#            alpha=0.9, hatch="\\\\")
#
#     # 最大最小值
#     ax.hlines(y=s1, xmin=np.arange(len(x)) - 0.03, xmax=np.arange(len(x)) + 0.03, color='k', alpha=0.6, linewidth=2,
#               zorder=12)
#     ax.hlines(y=s2, xmin=np.arange(len(x)) + bar_width + 0.04 - 0.03, xmax=np.arange(len(x)) + bar_width + 0.04 + 0.03,
#               color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=s3, xmin=np.arange(len(x)) + 2 * bar_width + 0.08 - 0.03,
#               xmax=np.arange(len(x)) + 2 * bar_width + 0.08 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=s4, xmin=np.arange(len(x)) + 3 * bar_width + 0.12 - 0.03,
#               xmax=np.arange(len(x)) + 3 * bar_width + 0.12 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=s5, xmin=np.arange(len(x)) + 4 * bar_width + 0.16 - 0.03,
#               xmax=np.arange(len(x)) + 4 * bar_width + 0.16 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=s6, xmin=np.arange(len(x)) + 5 * bar_width + 0.2 - 0.03,
#               xmax=np.arange(len(x)) + 5 * bar_width + 0.2 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#
#     ax.hlines(y=b1, xmin=np.arange(len(x)) - 0.03, xmax=np.arange(len(x)) + 0.03, color='k', alpha=0.6, linewidth=2,
#               zorder=12)
#     ax.hlines(y=b2, xmin=np.arange(len(x)) + bar_width + 0.04 - 0.03, xmax=np.arange(len(x)) + bar_width + 0.04 + 0.03,
#               color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=b3, xmin=np.arange(len(x)) + 2 * bar_width + 0.08 - 0.03,
#               xmax=np.arange(len(x)) + 2 * bar_width + 0.08 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=b4, xmin=np.arange(len(x)) + 3 * bar_width + 0.12 - 0.03,
#               xmax=np.arange(len(x)) + 3 * bar_width + 0.12 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=b5, xmin=np.arange(len(x)) + 4 * bar_width + 0.16 - 0.03,
#               xmax=np.arange(len(x)) + 4 * bar_width + 0.16 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=b6, xmin=np.arange(len(x)) + 5 * bar_width + 0.2 - 0.03,
#               xmax=np.arange(len(x)) + 5 * bar_width + 0.2 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#
#     ax.vlines(x=np.arange(len(x)), ymin=s1, ymax=b1, color='k', alpha=0.6, linewidth=2, zorder=12)
#     ax.vlines(x=np.arange(len(x)) + 1 * bar_width + 0.04, ymin=s2, ymax=b2, color='k', alpha=0.6, linewidth=2,
#               zorder=12)
#     ax.vlines(x=np.arange(len(x)) + 2 * bar_width + 0.08, ymin=s3, ymax=b3, color='k', alpha=0.6, linewidth=2,
#               zorder=12)
#     ax.vlines(x=np.arange(len(x)) + 3 * bar_width + 0.12, ymin=s4, ymax=b4, color='k', alpha=0.6, linewidth=2,
#               zorder=12)
#     ax.vlines(x=np.arange(len(x)) + 4 * bar_width + 0.16, ymin=s5, ymax=b5, color='k', alpha=0.6, linewidth=2,
#               zorder=12)
#     ax.vlines(x=np.arange(len(x)) + 5 * bar_width + 0.2, ymin=s6, ymax=b6, color='k', alpha=0.6, linewidth=2, zorder=12)
#
#     font = {'family': 'Times New Roman',
#             'weight': 'light',
#             'size': 17
#             }
#
#     box = ax.get_position()
#     ax.set_position([box.x0, box.y0, box.width, box.height * 0.8])
#     ax.legend(loc='center left', bbox_to_anchor=(-0.05, 1.22), ncol=6, prop=font)
#     plt.grid(axis="y", alpha=0.8, linestyle=':')
#
#     plt.savefig(str(name) + '.pdf')
#
#     plt.show()
#
#
# ##===========================c->java===========================
# def graphCJ(path, name):
#     df = pd.read_excel(path)
#     x = df['value'].values
#     # 平均值
#     y1 = df['VUDDY'].values
#     y2 = df['Lin'].values
#     y3 = df['vuldeepecker'].values
#     y4 = df['μvuldeepecker'].values
#     y5 = df['Deepbugs'].values
#     y6 = df['LACUNA'].values
#     # 最小值
#     s1 = df['sVUDDY'].values
#     s2 = df['sLin'].values
#     s3 = df['svuldeepecker'].values
#     s4 = df['sμvuldeepecker'].values
#     s5 = df['sDeepbugs'].values
#     s6 = df['sLACUNA'].values
#     # 最大值
#     b1 = df['bVUDDY'].values
#     b2 = df['bLin'].values
#     b3 = df['bvuldeepecker'].values
#     b4 = df['bμvuldeepecker'].values
#     b5 = df['bDeepbugs'].values
#     b6 = df['bLACUNA'].values
#
#     fig = plt.figure(figsize=(15, 3), dpi=80)
#     ax = fig.add_axes([0.12, 0.25, 0.8, 0.5], zorder=11)
#
#     ax.set_xticks(np.arange(0, 4, 1) + 0.35)
#     ax.set_xticklabels(x, fontdict={'horizontalalignment': 'center', 'size': 16})
#     ax.set_yticks(np.arange(0, 1.02, 0.2))
#     ax.set_yticklabels(['0%', '20%', '40%', '60%', '80%', '100%'],
#                        fontdict={'horizontalalignment': 'right', 'size': 16})
#     ax.set_ylim((0, 1.02))
#     # ax.set_ylabel('% of value', fontsize=14)
#
#     bar_width = 0.1
#     ax.bar(x=np.arange(len(x)), height=y1, label='VUDDY', width=bar_width, edgecolor=seaborn.xkcd_rgb['tan'],
#            linewidth=1, color=seaborn.xkcd_rgb['yellow tan'], zorder=10, alpha=0.9, hatch="//")
#     ax.bar(x=np.arange(len(x)) + bar_width + 0.04, height=y2, label='Lin', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey green'],
#            linewidth=1, color=seaborn.xkcd_rgb['light grey green'], zorder=10, alpha=0.9, hatch="||")
#     ax.bar(x=np.arange(len(x)) + 2 * bar_width + 0.08, height=y3, label='Vuldeepecker', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['coffee'], linewidth=1, color=seaborn.xkcd_rgb['very light brown'], zorder=10,
#            alpha=0.9, hatch="xx", align="center")
#     ax.bar(x=np.arange(len(x)) + 3 * bar_width + 0.12, height=y4, label='μVuldeepecker', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey blue'], linewidth=1, color=seaborn.xkcd_rgb['light grey blue'], zorder=10,
#            alpha=0.9, hatch="")
#     ax.bar(x=np.arange(len(x)) + 4 * bar_width + 0.16, height=y5, label='Deepbugs', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey purple'], linewidth=1, color=seaborn.xkcd_rgb['pale purple'], zorder=10,
#            alpha=0.9, hatch="++")
#     ax.bar(x=np.arange(len(x)) + 5 * bar_width + 0.2, height=y6, label='LACUNA', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['rose'], linewidth=1, color=seaborn.xkcd_rgb['faded pink'], zorder=10,
#            alpha=0.9, hatch="\\\\")
#
#     # 最大最小值
#     ax.hlines(y=s1, xmin=np.arange(len(x)) - 0.03, xmax=np.arange(len(x)) + 0.03, color='k', alpha=0.6, linewidth=2,
#               zorder=12)
#     ax.hlines(y=s2, xmin=np.arange(len(x)) + bar_width + 0.04 - 0.03, xmax=np.arange(len(x)) + bar_width + 0.04 + 0.03,
#               color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=s3, xmin=np.arange(len(x)) + 2 * bar_width + 0.08 - 0.03,
#               xmax=np.arange(len(x)) + 2 * bar_width + 0.08 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=s4, xmin=np.arange(len(x)) + 3 * bar_width + 0.12 - 0.03,
#               xmax=np.arange(len(x)) + 3 * bar_width + 0.12 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=s5, xmin=np.arange(len(x)) + 4 * bar_width + 0.16 - 0.03,
#               xmax=np.arange(len(x)) + 4 * bar_width + 0.16 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=s6, xmin=np.arange(len(x)) + 5 * bar_width + 0.2 - 0.03,
#               xmax=np.arange(len(x)) + 5 * bar_width + 0.2 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#
#     ax.hlines(y=b1, xmin=np.arange(len(x)) - 0.03, xmax=np.arange(len(x)) + 0.03, color='k', alpha=0.6, linewidth=2,
#               zorder=12)
#     ax.hlines(y=b2, xmin=np.arange(len(x)) + bar_width + 0.04 - 0.03, xmax=np.arange(len(x)) + bar_width + 0.04 + 0.03,
#               color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=b3, xmin=np.arange(len(x)) + 2 * bar_width + 0.08 - 0.03,
#               xmax=np.arange(len(x)) + 2 * bar_width + 0.08 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=b4, xmin=np.arange(len(x)) + 3 * bar_width + 0.12 - 0.03,
#               xmax=np.arange(len(x)) + 3 * bar_width + 0.12 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=b5, xmin=np.arange(len(x)) + 4 * bar_width + 0.16 - 0.03,
#               xmax=np.arange(len(x)) + 4 * bar_width + 0.16 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=b6, xmin=np.arange(len(x)) + 5 * bar_width + 0.2 - 0.03,
#               xmax=np.arange(len(x)) + 5 * bar_width + 0.2 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#
#     ax.vlines(x=np.arange(len(x)), ymin=s1, ymax=b1, color='k', alpha=0.6, linewidth=2, zorder=12)
#     ax.vlines(x=np.arange(len(x)) + 1 * bar_width + 0.04, ymin=s2, ymax=b2, color='k', alpha=0.6, linewidth=2,
#               zorder=12)
#     ax.vlines(x=np.arange(len(x)) + 2 * bar_width + 0.08, ymin=s3, ymax=b3, color='k', alpha=0.6, linewidth=2,
#               zorder=12)
#     ax.vlines(x=np.arange(len(x)) + 3 * bar_width + 0.12, ymin=s4, ymax=b4, color='k', alpha=0.6, linewidth=2,
#               zorder=12)
#     ax.vlines(x=np.arange(len(x)) + 4 * bar_width + 0.16, ymin=s5, ymax=b5, color='k', alpha=0.6, linewidth=2,
#               zorder=12)
#     ax.vlines(x=np.arange(len(x)) + 5 * bar_width + 0.2, ymin=s6, ymax=b6, color='k', alpha=0.6, linewidth=2, zorder=12)
#
#     font = {'family': 'Times New Roman',
#             'weight': 'light',
#             'size': 17
#             }
#
#     box = ax.get_position()
#     ax.set_position([box.x0, box.y0, box.width, box.height * 0.8])
#     ax.legend(loc='center left', bbox_to_anchor=(-0.05, 1.22), ncol=6, prop=font)
#     plt.grid(axis="y", alpha=0.8, linestyle=':')
#
#     plt.savefig(str(name) + '.pdf')
#
#     plt.show()
#
#
# ##===========================c->swift===========================
# def graphCS(path, name):
#     df = pd.read_excel(path)
#     x = df['value'].values
#     # 平均值
#     y1 = df['VUDDY'].values
#     y2 = df['vuldeepecker'].values
#     y3 = df['μvuldeepecker'].values
#     y4 = df['Lin'].values
#     y5 = df['Deepbugs'].values
#     y6 = df['LACUNA'].values
#     # 最小值
#     s1 = df['sVUDDY'].values
#     s2 = df['svuldeepecker'].values
#     s3 = df['sμvuldeepecker'].values
#     s4 = df['sLin'].values
#     s5 = df['sDeepbugs'].values
#     s6 = df['sLACUNA'].values
#     # 最大值
#     b1 = df['bVUDDY'].values
#     b2 = df['bvuldeepecker'].values
#     b3 = df['bμvuldeepecker'].values
#     b4 = df['bLin'].values
#     b5 = df['bDeepbugs'].values
#     b6 = df['bLACUNA'].values
#
#     fig = plt.figure(figsize=(15, 3), dpi=80)
#     ax = fig.add_axes([0.12, 0.25, 0.8, 0.5], zorder=11)
#
#     ax.set_xticks(np.arange(0, 4, 1) + 0.35)
#     ax.set_xticklabels(x, fontdict={'horizontalalignment': 'center', 'size': 16})
#     ax.set_yticks(np.arange(0, 1.02, 0.2))
#     ax.set_yticklabels(['0%', '20%', '40%', '60%', '80%', '100%'],
#                        fontdict={'horizontalalignment': 'right', 'size': 16})
#     ax.set_ylim((0, 1.02))
#     # ax.set_ylabel('% of value', fontsize=14)
#
#     bar_width = 0.1
#     ax.bar(x=np.arange(len(x)), height=y1, label='VUDDY', width=bar_width, edgecolor=seaborn.xkcd_rgb['tan'],
#            linewidth=1, color=seaborn.xkcd_rgb['yellow tan'], zorder=10, alpha=0.9, hatch="//")
#     ax.bar(x=np.arange(len(x)) + bar_width + 0.04, height=y2, label='Vuldeepecker', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey green'],
#            linewidth=1, color=seaborn.xkcd_rgb['light grey green'], zorder=10, alpha=0.9, hatch="||")
#     ax.bar(x=np.arange(len(x)) + 2 * bar_width + 0.08, height=y3, label='μVuldeepecker', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['coffee'], linewidth=1, color=seaborn.xkcd_rgb['very light brown'], zorder=10,
#            alpha=0.9, hatch="xx", align="center")
#     ax.bar(x=np.arange(len(x)) + 3 * bar_width + 0.12, height=y4, label='Lin', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey blue'], linewidth=1, color=seaborn.xkcd_rgb['light grey blue'], zorder=10,
#            alpha=0.9, hatch="")
#     ax.bar(x=np.arange(len(x)) + 4 * bar_width + 0.16, height=y5, label='Deepbugs', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey purple'], linewidth=1, color=seaborn.xkcd_rgb['pale purple'], zorder=10,
#            alpha=0.9, hatch="++")
#     ax.bar(x=np.arange(len(x)) + 5 * bar_width + 0.2, height=y6, label='LACUNA', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['rose'], linewidth=1, color=seaborn.xkcd_rgb['faded pink'], zorder=10,
#            alpha=0.9, hatch="\\\\")
#
#     # 最大最小值
#     ax.hlines(y=s1, xmin=np.arange(len(x)) - 0.03, xmax=np.arange(len(x)) + 0.03, color='k', alpha=0.6, linewidth=2,
#               zorder=12)
#     ax.hlines(y=s2, xmin=np.arange(len(x)) + bar_width + 0.04 - 0.03, xmax=np.arange(len(x)) + bar_width + 0.04 + 0.03,
#               color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=s3, xmin=np.arange(len(x)) + 2 * bar_width + 0.08 - 0.03,
#               xmax=np.arange(len(x)) + 2 * bar_width + 0.08 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=s4, xmin=np.arange(len(x)) + 3 * bar_width + 0.12 - 0.03,
#               xmax=np.arange(len(x)) + 3 * bar_width + 0.12 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=s5, xmin=np.arange(len(x)) + 4 * bar_width + 0.16 - 0.03,
#               xmax=np.arange(len(x)) + 4 * bar_width + 0.16 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=s6, xmin=np.arange(len(x)) + 5 * bar_width + 0.2 - 0.03,
#               xmax=np.arange(len(x)) + 5 * bar_width + 0.2 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#
#     ax.hlines(y=b1, xmin=np.arange(len(x)) - 0.03, xmax=np.arange(len(x)) + 0.03, color='k', alpha=0.6, linewidth=2,
#               zorder=12)
#     ax.hlines(y=b2, xmin=np.arange(len(x)) + bar_width + 0.04 - 0.03, xmax=np.arange(len(x)) + bar_width + 0.04 + 0.03,
#               color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=b3, xmin=np.arange(len(x)) + 2 * bar_width + 0.08 - 0.03,
#               xmax=np.arange(len(x)) + 2 * bar_width + 0.08 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=b4, xmin=np.arange(len(x)) + 3 * bar_width + 0.12 - 0.03,
#               xmax=np.arange(len(x)) + 3 * bar_width + 0.12 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=b5, xmin=np.arange(len(x)) + 4 * bar_width + 0.16 - 0.03,
#               xmax=np.arange(len(x)) + 4 * bar_width + 0.16 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=b6, xmin=np.arange(len(x)) + 5 * bar_width + 0.2 - 0.03,
#               xmax=np.arange(len(x)) + 5 * bar_width + 0.2 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#
#     ax.vlines(x=np.arange(len(x)), ymin=s1, ymax=b1, color='k', alpha=0.6, linewidth=2, zorder=12)
#     ax.vlines(x=np.arange(len(x)) + 1 * bar_width + 0.04, ymin=s2, ymax=b2, color='k', alpha=0.6, linewidth=2,
#               zorder=12)
#     ax.vlines(x=np.arange(len(x)) + 2 * bar_width + 0.08, ymin=s3, ymax=b3, color='k', alpha=0.6, linewidth=2,
#               zorder=12)
#     ax.vlines(x=np.arange(len(x)) + 3 * bar_width + 0.12, ymin=s4, ymax=b4, color='k', alpha=0.6, linewidth=2,
#               zorder=12)
#     ax.vlines(x=np.arange(len(x)) + 4 * bar_width + 0.16, ymin=s5, ymax=b5, color='k', alpha=0.6, linewidth=2,
#               zorder=12)
#     ax.vlines(x=np.arange(len(x)) + 5 * bar_width + 0.2, ymin=s6, ymax=b6, color='k', alpha=0.6, linewidth=2, zorder=12)
#
#     font = {'family': 'Times New Roman',
#             'weight': 'light',
#             'size': 17
#             }
#
#     box = ax.get_position()
#     ax.set_position([box.x0, box.y0, box.width, box.height * 0.8])
#     ax.legend(loc='center left', bbox_to_anchor=(-0.05, 1.22), ncol=6, prop=font)
#     plt.grid(axis="y", alpha=0.8, linestyle=':')
#
#     plt.savefig(str(name) + '.pdf')
#
#     plt.show()
#
#
# ##===========================java->php===========================
# def graphJP(path, name):
#     df = pd.read_excel(path)
#     x = df['value'].values
#     # 平均值
#     y1 = df['VUDDY'].values
#     y2 = df['μvuldeepecker'].values
#     y3 = df['vuldeepecker'].values
#     y4 = df['Lin'].values
#     y5 = df['Deepbugs'].values
#     y6 = df['LACUNA'].values
#     # 最小值
#     s1 = df['sVUDDY'].values
#     s2 = df['sμvuldeepecker'].values
#     s3 = df['svuldeepecker'].values
#     s4 = df['sLin'].values
#     s5 = df['sDeepbugs'].values
#     s6 = df['sLACUNA'].values
#     # 最大值
#     b1 = df['bVUDDY'].values
#     b2 = df['bμvuldeepecker'].values
#     b3 = df['bvuldeepecker'].values
#     b4 = df['bLin'].values
#     b5 = df['bDeepbugs'].values
#     b6 = df['bLACUNA'].values
#
#     fig = plt.figure(figsize=(15, 3), dpi=80)
#     ax = fig.add_axes([0.12, 0.25, 0.8, 0.5], zorder=11)
#
#     ax.set_xticks(np.arange(0, 4, 1) + 0.35)
#     ax.set_xticklabels(x, fontdict={'horizontalalignment': 'center', 'size': 16})
#     ax.set_yticks(np.arange(0, 1.02, 0.2))
#     ax.set_yticklabels(['0%', '20%', '40%', '60%', '80%', '100%'],
#                        fontdict={'horizontalalignment': 'right', 'size': 16})
#     ax.set_ylim((0, 1.02))
#     # ax.set_ylabel('% of value', fontsize=14)
#
#     bar_width = 0.1
#     ax.bar(x=np.arange(len(x)), height=y1, label='VUDDY', width=bar_width, edgecolor=seaborn.xkcd_rgb['tan'],
#            linewidth=1, color=seaborn.xkcd_rgb['yellow tan'], zorder=10, alpha=0.9, hatch="//")
#     ax.bar(x=np.arange(len(x)) + bar_width + 0.04, height=y2, label='μVuldeepecker', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey green'],
#            linewidth=1, color=seaborn.xkcd_rgb['light grey green'], zorder=10, alpha=0.9, hatch="||")
#     ax.bar(x=np.arange(len(x)) + 2 * bar_width + 0.08, height=y3, label='Vuldeepecker', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['coffee'], linewidth=1, color=seaborn.xkcd_rgb['very light brown'], zorder=10,
#            alpha=0.9, hatch="xx", align="center")
#     ax.bar(x=np.arange(len(x)) + 3 * bar_width + 0.12, height=y4, label='Lin', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey blue'], linewidth=1, color=seaborn.xkcd_rgb['light grey blue'], zorder=10,
#            alpha=0.9, hatch="")
#     ax.bar(x=np.arange(len(x)) + 4 * bar_width + 0.16, height=y5, label='Deepbugs', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey purple'], linewidth=1, color=seaborn.xkcd_rgb['pale purple'], zorder=10,
#            alpha=0.9, hatch="++")
#     ax.bar(x=np.arange(len(x)) + 5 * bar_width + 0.2, height=y6, label='LACUNA', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['rose'], linewidth=1, color=seaborn.xkcd_rgb['faded pink'], zorder=10,
#            alpha=0.9, hatch="\\\\")
#
#     # 最大最小值
#     ax.hlines(y=s1, xmin=np.arange(len(x)) - 0.03, xmax=np.arange(len(x)) + 0.03, color='k', alpha=0.6, linewidth=2,
#               zorder=12)
#     ax.hlines(y=s2, xmin=np.arange(len(x)) + bar_width + 0.04 - 0.03, xmax=np.arange(len(x)) + bar_width + 0.04 + 0.03,
#               color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=s3, xmin=np.arange(len(x)) + 2 * bar_width + 0.08 - 0.03,
#               xmax=np.arange(len(x)) + 2 * bar_width + 0.08 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=s4, xmin=np.arange(len(x)) + 3 * bar_width + 0.12 - 0.03,
#               xmax=np.arange(len(x)) + 3 * bar_width + 0.12 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=s5, xmin=np.arange(len(x)) + 4 * bar_width + 0.16 - 0.03,
#               xmax=np.arange(len(x)) + 4 * bar_width + 0.16 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=s6, xmin=np.arange(len(x)) + 5 * bar_width + 0.2 - 0.03,
#               xmax=np.arange(len(x)) + 5 * bar_width + 0.2 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#
#     ax.hlines(y=b1, xmin=np.arange(len(x)) - 0.03, xmax=np.arange(len(x)) + 0.03, color='k', alpha=0.6, linewidth=2,
#               zorder=12)
#     ax.hlines(y=b2, xmin=np.arange(len(x)) + bar_width + 0.04 - 0.03, xmax=np.arange(len(x)) + bar_width + 0.04 + 0.03,
#               color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=b3, xmin=np.arange(len(x)) + 2 * bar_width + 0.08 - 0.03,
#               xmax=np.arange(len(x)) + 2 * bar_width + 0.08 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=b4, xmin=np.arange(len(x)) + 3 * bar_width + 0.12 - 0.03,
#               xmax=np.arange(len(x)) + 3 * bar_width + 0.12 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=b5, xmin=np.arange(len(x)) + 4 * bar_width + 0.16 - 0.03,
#               xmax=np.arange(len(x)) + 4 * bar_width + 0.16 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=b6, xmin=np.arange(len(x)) + 5 * bar_width + 0.2 - 0.03,
#               xmax=np.arange(len(x)) + 5 * bar_width + 0.2 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#
#     ax.vlines(x=np.arange(len(x)), ymin=s1, ymax=b1, color='k', alpha=0.6, linewidth=2, zorder=12)
#     ax.vlines(x=np.arange(len(x)) + 1 * bar_width + 0.04, ymin=s2, ymax=b2, color='k', alpha=0.6, linewidth=2,
#               zorder=12)
#     ax.vlines(x=np.arange(len(x)) + 2 * bar_width + 0.08, ymin=s3, ymax=b3, color='k', alpha=0.6, linewidth=2,
#               zorder=12)
#     ax.vlines(x=np.arange(len(x)) + 3 * bar_width + 0.12, ymin=s4, ymax=b4, color='k', alpha=0.6, linewidth=2,
#               zorder=12)
#     ax.vlines(x=np.arange(len(x)) + 4 * bar_width + 0.16, ymin=s5, ymax=b5, color='k', alpha=0.6, linewidth=2,
#               zorder=12)
#     ax.vlines(x=np.arange(len(x)) + 5 * bar_width + 0.2, ymin=s6, ymax=b6, color='k', alpha=0.6, linewidth=2, zorder=12)
#
#     font = {'family': 'Times New Roman',
#             'weight': 'light',
#             'size': 17
#             }
#
#     box = ax.get_position()
#     ax.set_position([box.x0, box.y0, box.width, box.height * 0.8])
#     ax.legend(loc='center left', bbox_to_anchor=(-0.05, 1.22), ncol=6, prop=font)
#     plt.grid(axis="y", alpha=0.8, linestyle=':')
#
#     plt.savefig(str(name) + '.pdf')
#
#     plt.show()
#
#
# ##===========================sard->github 的mean,按大小===========================
# def graphSGM1(path, name):
#     df = pd.read_excel(path)
#     x = df['value'].values
#     # 平均值
#     y1 = df['VUDDY'].values
#     y2 = df['vuldeepecker'].values
#     y3 = df['Deepbugs'].values
#     y4 = df['μvuldeepecker'].values
#     y5 = df['Lin'].values
#     y6 = df['LACUNA'].values
#     # 最小值
#     s1 = df['sVUDDY'].values
#     s2 = df['svuldeepecker'].values
#     s3 = df['sDeepbugs'].values
#     s4 = df['sμvuldeepecker'].values
#     s5 = df['sLin'].values
#     s6 = df['sLACUNA'].values
#     # 最大值
#     b1 = df['bVUDDY'].values
#     b2 = df['bvuldeepecker'].values
#     b3 = df['bDeepbugs'].values
#     b4 = df['bμvuldeepecker'].values
#     b5 = df['bLin'].values
#     b6 = df['bLACUNA'].values
#
#     fig = plt.figure(figsize=(15, 3), dpi=80)
#     ax = fig.add_axes([0.12, 0.25, 0.8, 0.5], zorder=11)
#
#     ax.set_xticks(np.arange(0, 4, 1) + 0.33)
#     ax.set_xticklabels(x, fontdict={'horizontalalignment': 'center', 'size': 16})
#     ax.set_yticks(np.arange(0, 1.02, 0.2))
#     ax.set_yticklabels(['0%', '20%', '40%', '60%', '80%', '100%'],
#                        fontdict={'horizontalalignment': 'right', 'size': 16})
#     ax.set_ylim((0, 1.02))
#     # ax.set_ylabel('% of value', fontsize=14)
#
#     bar_width = 0.1
#     ax.bar(x=np.arange(len(x)), height=y1, label='VUDDY', width=bar_width, edgecolor=seaborn.xkcd_rgb['tan'],
#            linewidth=1, color=seaborn.xkcd_rgb['yellow tan'], zorder=10, alpha=0.9, hatch="//")
#     ax.bar(x=np.arange(len(x)) + bar_width + 0.04, height=y2, label='Vuldeepecker', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey green'],
#            linewidth=1, color=seaborn.xkcd_rgb['light grey green'], zorder=10, alpha=0.9, hatch="||")
#     ax.bar(x=np.arange(len(x)) + 2 * bar_width + 0.08, height=y3, label='Deepbugs', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['coffee'], linewidth=1, color=seaborn.xkcd_rgb['very light brown'], zorder=10,
#            alpha=0.9, hatch="xx", align="center")
#     ax.bar(x=np.arange(len(x)) + 3 * bar_width + 0.12, height=y4, label='μVuldeepecker', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey blue'], linewidth=1, color=seaborn.xkcd_rgb['light grey blue'], zorder=10,
#            alpha=0.9, hatch="")
#     ax.bar(x=np.arange(len(x)) + 4 * bar_width + 0.16, height=y5, label='Lin', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey purple'], linewidth=1, color=seaborn.xkcd_rgb['pale purple'], zorder=10,
#            alpha=0.9, hatch="++")
#     ax.bar(x=np.arange(len(x)) + 5 * bar_width + 0.2, height=y6, label='LACUNA', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['rose'], linewidth=1, color=seaborn.xkcd_rgb['faded pink'], zorder=10,
#            alpha=0.9, hatch="\\\\")
#
#     # 最大最小值
#     ax.hlines(y=s1, xmin=np.arange(len(x)) - 0.03, xmax=np.arange(len(x)) + 0.03, color='k', alpha=0.6, linewidth=2,
#               zorder=12)
#     ax.hlines(y=s2, xmin=np.arange(len(x)) + bar_width + 0.04 - 0.03, xmax=np.arange(len(x)) + bar_width + 0.04 + 0.03,
#               color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=s3, xmin=np.arange(len(x)) + 2 * bar_width + 0.08 - 0.03,
#               xmax=np.arange(len(x)) + 2 * bar_width + 0.08 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=s4, xmin=np.arange(len(x)) + 3 * bar_width + 0.12 - 0.03,
#               xmax=np.arange(len(x)) + 3 * bar_width + 0.12 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=s5, xmin=np.arange(len(x)) + 4 * bar_width + 0.16 - 0.03,
#               xmax=np.arange(len(x)) + 4 * bar_width + 0.16 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=s6, xmin=np.arange(len(x)) + 5 * bar_width + 0.2 - 0.03,
#               xmax=np.arange(len(x)) + 5 * bar_width + 0.2 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#
#     ax.hlines(y=b1, xmin=np.arange(len(x)) - 0.03, xmax=np.arange(len(x)) + 0.03, color='k', alpha=0.6, linewidth=2,
#               zorder=12)
#     ax.hlines(y=b2, xmin=np.arange(len(x)) + bar_width + 0.04 - 0.03, xmax=np.arange(len(x)) + bar_width + 0.04 + 0.03,
#               color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=b3, xmin=np.arange(len(x)) + 2 * bar_width + 0.08 - 0.03,
#               xmax=np.arange(len(x)) + 2 * bar_width + 0.08 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=b4, xmin=np.arange(len(x)) + 3 * bar_width + 0.12 - 0.03,
#               xmax=np.arange(len(x)) + 3 * bar_width + 0.12 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=b5, xmin=np.arange(len(x)) + 4 * bar_width + 0.16 - 0.03,
#               xmax=np.arange(len(x)) + 4 * bar_width + 0.16 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=b6, xmin=np.arange(len(x)) + 5 * bar_width + 0.2 - 0.03,
#               xmax=np.arange(len(x)) + 5 * bar_width + 0.2 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#
#     ax.vlines(x=np.arange(len(x)), ymin=s1, ymax=b1, color='k', alpha=0.6, linewidth=2, zorder=12)
#     ax.vlines(x=np.arange(len(x)) + 1 * bar_width + 0.04, ymin=s2, ymax=b2, color='k', alpha=0.6, linewidth=2,
#               zorder=12)
#     ax.vlines(x=np.arange(len(x)) + 2 * bar_width + 0.08, ymin=s3, ymax=b3, color='k', alpha=0.6, linewidth=2,
#               zorder=12)
#     ax.vlines(x=np.arange(len(x)) + 3 * bar_width + 0.12, ymin=s4, ymax=b4, color='k', alpha=0.6, linewidth=2,
#               zorder=12)
#     ax.vlines(x=np.arange(len(x)) + 4 * bar_width + 0.16, ymin=s5, ymax=b5, color='k', alpha=0.6, linewidth=2,
#               zorder=12)
#     ax.vlines(x=np.arange(len(x)) + 5 * bar_width + 0.2, ymin=s6, ymax=b6, color='k', alpha=0.6, linewidth=2, zorder=12)
#
#     font = {'family': 'Times New Roman',
#             'weight': 'light',
#             'size': 17
#             }
#
#     df1 = pd.read_excel(r'C:\Users\WHT\Desktop\不能颓鸭\gra\gra\SGM1_P.xlsx')
#     x1 = df1['value'].values
#     # 平均值
#     y11 = df1['Deepbugs'].values
#     y21 = df1['Lin'].values
#     y31 = df1['vuldeepecker'].values
#     y41 = df1['μvuldeepecker'].values
#     y51 = df1['LACUNA'].values
#     y61 = df1['VUDDY'].values
#     # 最小值
#     s11 = df1['sDeepbugs'].values
#     s21 = df1['sLin'].values
#     s31 = df1['svuldeepecker'].values
#     s41 = df1['sμvuldeepecker'].values
#     s51 = df1['sLACUNA'].values
#     s61 = df1['sVUDDY'].values
#     # 最大值
#     b11 = df1['bDeepbugs'].values
#     b21 = df1['bLin'].values
#     b31 = df1['bvuldeepecker'].values
#     b41 = df1['bμvuldeepecker'].values
#     b51 = df1['bLACUNA'].values
#     b61 = df1['bVUDDY'].values
#
#     ax.bar(x=np.arange(len(x1)), height=y11, width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['coffee'], linewidth=1, color=seaborn.xkcd_rgb['very light brown'], zorder=10,
#            alpha=0.9, hatch="xx", align="center")
#     ax.bar(x=np.arange(len(x1)) + 1 * bar_width + 0.04, height=y21, width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey purple'], linewidth=1, color=seaborn.xkcd_rgb['pale purple'], zorder=10,
#            alpha=0.9, hatch="++")
#     ax.bar(x=np.arange(len(x1)) + 2 * bar_width + 0.08, height=y31, width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey green'],
#            linewidth=1, color=seaborn.xkcd_rgb['light grey green'], zorder=10, alpha=0.9, hatch="||")
#     ax.bar(x=np.arange(len(x1)) + 3 * bar_width + 0.12, height=y41, width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey blue'], linewidth=1, color=seaborn.xkcd_rgb['light grey blue'], zorder=10,
#            alpha=0.9, hatch="")
#     ax.bar(x=np.arange(len(x1)) + 4 * bar_width + 0.16, height=y51, width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['rose'], linewidth=1, color=seaborn.xkcd_rgb['faded pink'], zorder=10,
#            alpha=0.9, hatch="\\\\")
#     ax.bar(x=np.arange(len(x1)) + 5 * bar_width + 0.2, height=y61, width=bar_width, edgecolor=seaborn.xkcd_rgb['tan'],
#            linewidth=1, color=seaborn.xkcd_rgb['yellow tan'], zorder=10, alpha=0.9, hatch="//")
#
#     ax.hlines(y=s11, xmin=np.arange(len(x1)) - 0.03, xmax=np.arange(len(x1)) + 0.03, color='k', alpha=0.6, linewidth=2,
#               zorder=12)
#     ax.hlines(y=s21, xmin=np.arange(len(x1)) + bar_width + 0.04 - 0.03,
#               xmax=np.arange(len(x1)) + bar_width + 0.04 + 0.03,
#               color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=s31, xmin=np.arange(len(x1)) + 2 * bar_width + 0.08 - 0.03,
#               xmax=np.arange(len(x1)) + 2 * bar_width + 0.08 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=s41, xmin=np.arange(len(x1)) + 3 * bar_width + 0.12 - 0.03,
#               xmax=np.arange(len(x1)) + 3 * bar_width + 0.12 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=s51, xmin=np.arange(len(x1)) + 4 * bar_width + 0.16 - 0.03,
#               xmax=np.arange(len(x1)) + 4 * bar_width + 0.16 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=s61, xmin=np.arange(len(x1)) + 5 * bar_width + 0.2 - 0.03,
#               xmax=np.arange(len(x1)) + 5 * bar_width + 0.2 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#
#     ax.hlines(y=b11, xmin=np.arange(len(x1)) - 0.03, xmax=np.arange(len(x1)) + 0.03, color='k', alpha=0.6, linewidth=2,
#               zorder=12)
#     ax.hlines(y=b21, xmin=np.arange(len(x1)) + bar_width + 0.04 - 0.03,
#               xmax=np.arange(len(x1)) + bar_width + 0.04 + 0.03,
#               color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=b31, xmin=np.arange(len(x1)) + 2 * bar_width + 0.08 - 0.03,
#               xmax=np.arange(len(x1)) + 2 * bar_width + 0.08 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=b41, xmin=np.arange(len(x1)) + 3 * bar_width + 0.12 - 0.03,
#               xmax=np.arange(len(x1)) + 3 * bar_width + 0.12 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=b51, xmin=np.arange(len(x1)) + 4 * bar_width + 0.16 - 0.03,
#               xmax=np.arange(len(x1)) + 4 * bar_width + 0.16 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#     ax.hlines(y=b61, xmin=np.arange(len(x1)) + 5 * bar_width + 0.2 - 0.03,
#               xmax=np.arange(len(x1)) + 5 * bar_width + 0.2 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
#
#     ax.vlines(x=np.arange(len(x1)), ymin=s11, ymax=b11, color='k', alpha=0.6, linewidth=2, zorder=12)
#     ax.vlines(x=np.arange(len(x1)) + 1 * bar_width + 0.04, ymin=s21, ymax=b21, color='k', alpha=0.6, linewidth=2,
#               zorder=12)
#     ax.vlines(x=np.arange(len(x1)) + 2 * bar_width + 0.08, ymin=s31, ymax=b31, color='k', alpha=0.6, linewidth=2,
#               zorder=12)
#     ax.vlines(x=np.arange(len(x1)) + 3 * bar_width + 0.12, ymin=s41, ymax=b41, color='k', alpha=0.6, linewidth=2,
#               zorder=12)
#     ax.vlines(x=np.arange(len(x1)) + 4 * bar_width + 0.16, ymin=s51, ymax=b51, color='k', alpha=0.6, linewidth=2,
#               zorder=12)
#     ax.vlines(x=np.arange(len(x1)) + 5 * bar_width + 0.2, ymin=s61, ymax=b61, color='k', alpha=0.6, linewidth=2,
#               zorder=12)
#
#     box = ax.get_position()
#     ax.set_position([box.x0, box.y0, box.width, box.height * 0.8])
#     ax.legend(loc='center left', bbox_to_anchor=(-0.05, 1.22), ncol=6, prop=font)
#     plt.grid(axis="y", alpha=0.8, linestyle=':')
#
#     plt.savefig(str(name) + '.pdf')
#
#     plt.show()


##===========================c->java===========================
#画不同模型的不同指标的不同CWE类型平均数的对比(c语言迁移java),并标有最大最小值
def graphCJ1(path, name):
    df = pd.read_excel(path)
    x = df['value'].values
    # 平均值
    y1 = df['VUDDY'].values
    y2 = df['μvuldeepecker'].values
    y3 = df['vuldeepecker'].values
    y4 = df['TDSC'].values
    y5 = df['Lin'].values
    y6 = df['NIPS'].values
    y7 = df['RGIN'].values
    # 最小值
    s1 = df['sVUDDY'].values
    s2 = df['sμvuldeepecker'].values
    s3 = df['svuldeepecker'].values
    s4 = df['sTDSC'].values
    s5 = df['sLin'].values
    s6 = df['sNIPS'].values
    s7 = df['sRGIN'].values
    # 最大值
    b1 = df['bVUDDY'].values
    b2 = df['bμvuldeepecker'].values
    b3 = df['bvuldeepecker'].values
    b4 = df['bTDSC'].values
    b5 = df['bLin'].values
    b6 = df['bNIPS'].values
    b7 = df['bRGIN'].values

    fig = plt.figure(figsize=(15, 3), dpi=80)
    ax = fig.add_axes([0.12, 0.25, 0.8, 0.6], zorder=11)

    ax.set_xticks(np.arange(0, 4, 1) + 0.33)
    ax.set_xticklabels(x, fontdict={'horizontalalignment': 'center', 'size': 28,'family': 'Arial'})
    ax.set_yticks(np.arange(0, 1.02, 0.2))
    ax.set_yticklabels([0, 0.2, 0.4, 0.6, 0.8, 1],
                       fontdict={'horizontalalignment': 'right', 'size': 24,'family': 'Arial'})
    ax.set_ylim((0, 1.02))
    # ax.set_ylabel('% of value', fontsize=14)
    bar_width = 0.08
    ax.bar(x=np.arange(len(x)), height=y1, label='VUDDY',
           width=bar_width, edgecolor='#D3D3D3',
           linewidth=1, color='#83bccc', zorder=10,
           alpha=0.9, align="center")
    ax.bar(x=np.arange(len(x)) + bar_width + 0.03, height=y2, label='μVULDEEPECKER', width=bar_width,
           edgecolor='#6ea1af',
           linewidth=1, color='#72aaba', zorder=10, alpha=0.9)
    ax.bar(x=np.arange(len(x)) + 2 * bar_width + 0.06, height=y3, label='VULDEEPECKER', width=bar_width,
           edgecolor='#598692',
           linewidth=1, color='#6299a8', zorder=10, alpha=0.9)
    ax.bar(x=np.arange(len(x)) + 3 * bar_width + 0.09, height=y4, label='LIN et al.', width=bar_width,
           edgecolor='#456c77', linewidth=1, color='#518896', zorder=10,
           alpha=0.9)
    ax.bar(x=np.arange(len(x)) + 4 * bar_width + 0.12, height=y5, label='DEEPBUGS', width=bar_width,
           edgecolor='#32545d', linewidth=1, color='#417785', zorder=10,
           alpha=0.9,)
    ax.bar(x=np.arange(len(x)) + 5 * bar_width + 0.15, height=y6, label='DEVIGN', width=bar_width,
           edgecolor='#1f3c44', linewidth=1, color='#316774', zorder=10,
           alpha=0.9)
    ax.bar(x=np.arange(len(x)) + 6 * bar_width + 0.18, height=y7, label='FUNDED', width=bar_width,
           edgecolor='#0e262c', linewidth=1, color='#205764', zorder=10,
           alpha=0.9)

    # 最大最小值
    ax.hlines(y=s1, xmin=np.arange(len(x)) - 0.03, xmax=np.arange(len(x)) + 0.03, color='k', alpha=0.6, linewidth=2,
              zorder=12)
    ax.hlines(y=s2, xmin=np.arange(len(x)) + bar_width + 0.03 - 0.03, xmax=np.arange(len(x)) + bar_width + 0.04 + 0.03,
              color='k', alpha=0.6, linewidth=2.5, zorder=12)
    ax.hlines(y=s3, xmin=np.arange(len(x)) + 2 * bar_width + 0.06 - 0.03,
              xmax=np.arange(len(x)) + 2 * bar_width + 0.06 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
    ax.hlines(y=s4, xmin=np.arange(len(x)) + 3 * bar_width + 0.09 - 0.03,
              xmax=np.arange(len(x)) + 3 * bar_width + 0.09 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
    ax.hlines(y=s5, xmin=np.arange(len(x)) + 4 * bar_width + 0.12 - 0.03,
              xmax=np.arange(len(x)) + 4 * bar_width + 0.12 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
    ax.hlines(y=s6, xmin=np.arange(len(x)) + 5 * bar_width + 0.15 - 0.03,
              xmax=np.arange(len(x)) + 5 * bar_width + 0.15 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
    ax.hlines(y=s7, xmin=np.arange(len(x)) + 6 * bar_width + 0.18 - 0.03,
              xmax=np.arange(len(x)) + 6 * bar_width + 0.18 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)

    ax.hlines(y=b1, xmin=np.arange(len(x)) - 0.03, xmax=np.arange(len(x)) + 0.03, color='k', alpha=0.6, linewidth=2,
              zorder=12)
    ax.hlines(y=b2, xmin=np.arange(len(x)) + bar_width + 0.03 - 0.03, xmax=np.arange(len(x)) + bar_width + 0.04 + 0.03,
              color='k', alpha=0.6, linewidth=2.5, zorder=12)
    ax.hlines(y=b3, xmin=np.arange(len(x)) + 2 * bar_width + 0.06 - 0.03,
              xmax=np.arange(len(x)) + 2 * bar_width + 0.06 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
    ax.hlines(y=b4, xmin=np.arange(len(x)) + 3 * bar_width + 0.09 - 0.03,
              xmax=np.arange(len(x)) + 3 * bar_width + 0.09 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
    ax.hlines(y=b5, xmin=np.arange(len(x)) + 4 * bar_width + 0.12 - 0.03,
              xmax=np.arange(len(x)) + 4 * bar_width + 0.12 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
    ax.hlines(y=b6, xmin=np.arange(len(x)) + 5 * bar_width + 0.15 - 0.03,
              xmax=np.arange(len(x)) + 5 * bar_width + 0.15 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
    ax.hlines(y=b7, xmin=np.arange(len(x)) + 6 * bar_width + 0.18 - 0.03,
              xmax=np.arange(len(x)) + 6 * bar_width + 0.18 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)

    ax.vlines(x=np.arange(len(x)), ymin=s1, ymax=b1, color='k', alpha=0.6, linewidth=2, zorder=12)
    ax.vlines(x=np.arange(len(x)) + 1 * bar_width + 0.03, ymin=s2, ymax=b2, color='k', alpha=0.6, linewidth=2,
              zorder=12)
    ax.vlines(x=np.arange(len(x)) + 2 * bar_width + 0.06, ymin=s3, ymax=b3, color='k', alpha=0.6, linewidth=2,
              zorder=12)
    ax.vlines(x=np.arange(len(x)) + 3 * bar_width + 0.09, ymin=s4, ymax=b4, color='k', alpha=0.6, linewidth=2,
              zorder=12)
    ax.vlines(x=np.arange(len(x)) + 4 * bar_width + 0.12, ymin=s5, ymax=b5, color='k', alpha=0.6, linewidth=2,
              zorder=12)
    ax.vlines(x=np.arange(len(x)) + 5 * bar_width + 0.15, ymin=s6, ymax=b6, color='k', alpha=0.6, linewidth=2,
              zorder=12)
    ax.vlines(x=np.arange(len(x)) + 6 * bar_width + 0.18, ymin=s7, ymax=b7, color='k', alpha=0.6, linewidth=2,
              zorder=12)

    font = {'family':'Arial',
            'weight': 'light',
            'size': 20.2
            }

    box = ax.get_position()
    # columnspacing=2
    ax.set_position([box.x0, box.y0, box.width, box.height * 0.8])
    ax.legend(loc='center left', bbox_to_anchor=(-0.06, 1.22), ncol=7, prop=font, columnspacing=0.1, handletextpad=0.01,
              handlelength=0.8)
    plt.grid(axis="y", alpha=0.8, linestyle=':')

    plt.savefig(str(name) + '.pdf')

    plt.show()


##===========================c->swift,带折线==========================
# 画不同模型的不同指标的不同CWE类型平均数的对比(c语言迁移swift),并标有最大最小值
def graphCS1(path, name):
    df = pd.read_excel(path)
    x = df['value'].values
    # 平均值
    y1 = df['VUDDY'].values
    y2 = df['TDSC'].values
    y3 = df['vuldeepecker'].values
    y4 = df['μvuldeepecker'].values
    y5 = df['Lin'].values
    y6 = df['NIPS'].values
    y7 = df['RGIN'].values
    # 最小值
    s1 = df['sVUDDY'].values
    s2 = df['sTDSC'].values
    s3 = df['svuldeepecker'].values
    s4 = df['sμvuldeepecker'].values
    s5 = df['sLin'].values
    s6 = df['sNIPS'].values
    s7 = df['sRGIN'].values
    # 最大值
    b1 = df['bVUDDY'].values
    b2 = df['bTDSC'].values
    b3 = df['bvuldeepecker'].values
    b4 = df['bμvuldeepecker'].values
    b5 = df['bLin'].values
    b6 = df['bNIPS'].values
    b7 = df['bRGIN'].values

    fig = plt.figure(figsize=(15, 3), dpi=80)
    ax = fig.add_axes([0.12, 0.25, 0.8, 0.6], zorder=11)

    ax.set_xticks(np.arange(0, 4, 1) + 0.33)
    ax.set_xticklabels(x, fontdict={'horizontalalignment': 'center', 'size': 28,'family': 'Arial'})
    ax.set_yticks(np.arange(0, 1.02, 0.2))
    ax.set_yticklabels([0, 0.2, 0.4, 0.6, 0.8, 1],
                       fontdict={'horizontalalignment': 'right', 'size': 24,'family': 'Arial'})
    ax.set_ylim((0, 1.02))
    # ax.set_ylabel('% of value', fontsize=14)
    bar_width = 0.08
    # ax.bar(x=np.arange(len(x)), height=y1, label='VUDDY', width=bar_width, edgecolor=seaborn.xkcd_rgb['coffee'],
    #        linewidth=1, color=seaborn.xkcd_rgb['very light brown'], zorder=10,
    #        alpha=0.9, hatch="xx", align="center")
    # ax.bar(x=np.arange(len(x)) + bar_width + 0.03, height=y2, label='LIN et al.', width=bar_width,
    #        edgecolor=seaborn.xkcd_rgb['perrywinkle'],
    #        linewidth=1, color=seaborn.xkcd_rgb['light violet'], zorder=10, alpha=0.9, hatch="|\\|")
    # ax.bar(x=np.arange(len(x)) + 2 * bar_width + 0.06, height=y3, label='VULDEEPECKER', width=bar_width,
    #        edgecolor=seaborn.xkcd_rgb['grey green'],
    #        linewidth=1, color=seaborn.xkcd_rgb['light grey green'], zorder=10, alpha=0.9, hatch="||")
    # ax.bar(x=np.arange(len(x)) + 3 * bar_width + 0.09, height=y4, label='μVULDEEPECKER', width=bar_width,
    #        edgecolor=seaborn.xkcd_rgb['grey purple'], linewidth=1, color=seaborn.xkcd_rgb['pale purple'], zorder=10,
    #        alpha=0.9, hatch="++")
    # ax.bar(x=np.arange(len(x)) + 4 * bar_width + 0.12, height=y5, label='DEEPBUGS', width=bar_width,
    #        edgecolor=seaborn.xkcd_rgb['grey blue'], linewidth=1, color=seaborn.xkcd_rgb['light grey blue'], zorder=10,
    #        alpha=0.9, hatch="\\\\")
    # ax.bar(x=np.arange(len(x)) + 5 * bar_width + 0.15, height=y6, label='DEVIGN', width=bar_width,
    #        edgecolor=seaborn.xkcd_rgb['rose'], linewidth=1, color=seaborn.xkcd_rgb['faded pink'], zorder=10,
    #        alpha=0.9, hatch="")
    # ax.bar(x=np.arange(len(x)) + 6 * bar_width + 0.18, height=y7, label='FUNDED', width=bar_width,
    #        edgecolor=seaborn.xkcd_rgb['orangeish'], linewidth=1, color=seaborn.xkcd_rgb['peach'], zorder=10,
    #        alpha=0.9, hatch="-/")

    # ax.bar(x=np.arange(len(x)), height=y1, label='VUDDY',
    #        width=bar_width, edgecolor='#D3D3D3',
    #        linewidth=1, color='#ede4fb', zorder=10,
    #        alpha=0.9, align="center")
    # ax.bar(x=np.arange(len(x)) + bar_width + 0.03, height=y2, label='LIN et al.', width=bar_width,
    #        edgecolor='#cabfdc',
    #        linewidth=1, color='#d2c4e9', zorder=10, alpha=0.9)
    # ax.bar(x=np.arange(len(x)) + 2 * bar_width + 0.06, height=y3, label='VULDEEPECKER', width=bar_width,
    #        edgecolor='#a79bbe',
    #        linewidth=1, color='#b7a5d8', zorder=10, alpha=0.9)
    # ax.bar(x=np.arange(len(x)) + 3 * bar_width + 0.09, height=y4, label='μVULDEEPECKER', width=bar_width,
    #        edgecolor='#8678a0', linewidth=1, color='#9c86c6', zorder=10,
    #        alpha=0.9)
    # ax.bar(x=np.arange(len(x)) + 4 * bar_width + 0.12, height=y5, label='DEEPBUGS', width=bar_width,
    #        edgecolor='#655784', linewidth=1, color='#8169b5', zorder=10,
    #        alpha=0.9, )
    # ax.bar(x=np.arange(len(x)) + 5 * bar_width + 0.15, height=y6, label='DEVIGN', width=bar_width,
    #        edgecolor='#453768', linewidth=1, color='#654ca3', zorder=10,
    #        alpha=0.9)
    # ax.bar(x=np.arange(len(x)) + 6 * bar_width + 0.18, height=y7, label='FUNDED', width=bar_width,
    #        edgecolor='#261a4d', linewidth=1, color='#473192', zorder=10,
    #        alpha=0.9)
    ax.bar(x=np.arange(len(x)), height=y1, label='VUDDY',
           width=bar_width, edgecolor='#D3D3D3',
           linewidth=1, color='#83bccc', zorder=10,
           alpha=0.9, align="center")
    ax.bar(x=np.arange(len(x)) + bar_width + 0.03, height=y2, label='LIN et al.', width=bar_width,
           edgecolor='#456c77',
           linewidth=1, color='#518896', zorder=10, alpha=0.9)
    ax.bar(x=np.arange(len(x)) + 2 * bar_width + 0.06, height=y3, label='VULDEEPECKER', width=bar_width,
           edgecolor='#598692',
           linewidth=1, color='#6299a8', zorder=10, alpha=0.9)
    ax.bar(x=np.arange(len(x)) + 3 * bar_width + 0.09, height=y4, label='μVULDEEPECKER', width=bar_width,
           edgecolor='#6ea1af', linewidth=1, color='#72aaba', zorder=10,
           alpha=0.9)
    ax.bar(x=np.arange(len(x)) + 4 * bar_width + 0.12, height=y5, label='DEEPBUGS', width=bar_width,
           edgecolor='#32545d', linewidth=1, color='#417785', zorder=10,
           alpha=0.9, )
    ax.bar(x=np.arange(len(x)) + 5 * bar_width + 0.15, height=y6, label='DEVIGN', width=bar_width,
           edgecolor='#1f3c44', linewidth=1, color='#316774', zorder=10,
           alpha=0.9)
    ax.bar(x=np.arange(len(x)) + 6 * bar_width + 0.18, height=y7, label='FUNDED', width=bar_width,
           edgecolor='#0e262c', linewidth=1, color='#205764', zorder=10,
           alpha=0.9)

    # 最大最小值
    ax.hlines(y=s1, xmin=np.arange(len(x)) - 0.03, xmax=np.arange(len(x)) + 0.03, color='k', alpha=0.6, linewidth=2,
              zorder=12)
    ax.hlines(y=s2, xmin=np.arange(len(x)) + bar_width + 0.03 - 0.03, xmax=np.arange(len(x)) + bar_width + 0.04 + 0.03,
              color='k', alpha=0.6, linewidth=2.5, zorder=12)
    ax.hlines(y=s3, xmin=np.arange(len(x)) + 2 * bar_width + 0.06 - 0.03,
              xmax=np.arange(len(x)) + 2 * bar_width + 0.06 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
    ax.hlines(y=s4, xmin=np.arange(len(x)) + 3 * bar_width + 0.09 - 0.03,
              xmax=np.arange(len(x)) + 3 * bar_width + 0.09 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
    ax.hlines(y=s5, xmin=np.arange(len(x)) + 4 * bar_width + 0.12 - 0.03,
              xmax=np.arange(len(x)) + 4 * bar_width + 0.12 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
    ax.hlines(y=s6, xmin=np.arange(len(x)) + 5 * bar_width + 0.15 - 0.03,
              xmax=np.arange(len(x)) + 5 * bar_width + 0.15 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
    ax.hlines(y=s7, xmin=np.arange(len(x)) + 6 * bar_width + 0.18 - 0.03,
              xmax=np.arange(len(x)) + 6 * bar_width + 0.18 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)

    ax.hlines(y=b1, xmin=np.arange(len(x)) - 0.03, xmax=np.arange(len(x)) + 0.03, color='k', alpha=0.6, linewidth=2,
              zorder=12)
    ax.hlines(y=b2, xmin=np.arange(len(x)) + bar_width + 0.03 - 0.03, xmax=np.arange(len(x)) + bar_width + 0.04 + 0.03,
              color='k', alpha=0.6, linewidth=2.5, zorder=12)
    ax.hlines(y=b3, xmin=np.arange(len(x)) + 2 * bar_width + 0.06 - 0.03,
              xmax=np.arange(len(x)) + 2 * bar_width + 0.06 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
    ax.hlines(y=b4, xmin=np.arange(len(x)) + 3 * bar_width + 0.09 - 0.03,
              xmax=np.arange(len(x)) + 3 * bar_width + 0.09 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
    ax.hlines(y=b5, xmin=np.arange(len(x)) + 4 * bar_width + 0.12 - 0.03,
              xmax=np.arange(len(x)) + 4 * bar_width + 0.12 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
    ax.hlines(y=b6, xmin=np.arange(len(x)) + 5 * bar_width + 0.15 - 0.03,
              xmax=np.arange(len(x)) + 5 * bar_width + 0.15 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
    ax.hlines(y=b7, xmin=np.arange(len(x)) + 6 * bar_width + 0.18 - 0.03,
              xmax=np.arange(len(x)) + 6 * bar_width + 0.18 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)

    ax.vlines(x=np.arange(len(x)), ymin=s1, ymax=b1, color='k', alpha=0.6, linewidth=2, zorder=12)
    ax.vlines(x=np.arange(len(x)) + 1 * bar_width + 0.03, ymin=s2, ymax=b2, color='k', alpha=0.6, linewidth=2,
              zorder=12)
    ax.vlines(x=np.arange(len(x)) + 2 * bar_width + 0.06, ymin=s3, ymax=b3, color='k', alpha=0.6, linewidth=2,
              zorder=12)
    ax.vlines(x=np.arange(len(x)) + 3 * bar_width + 0.09, ymin=s4, ymax=b4, color='k', alpha=0.6, linewidth=2,
              zorder=12)
    ax.vlines(x=np.arange(len(x)) + 4 * bar_width + 0.12, ymin=s5, ymax=b5, color='k', alpha=0.6, linewidth=2,
              zorder=12)
    ax.vlines(x=np.arange(len(x)) + 5 * bar_width + 0.15, ymin=s6, ymax=b6, color='k', alpha=0.6, linewidth=2,
              zorder=12)
    ax.vlines(x=np.arange(len(x)) + 6 * bar_width + 0.18, ymin=s7, ymax=b7, color='k', alpha=0.6, linewidth=2,
              zorder=12)

    font = {'family':'Arial',
            'weight': 'light',
            'size': 20.2
            }

    box = ax.get_position()
    # columnspacing=2
    ax.set_position([box.x0, box.y0, box.width, box.height * 0.8])
    ax.legend(loc='center left', bbox_to_anchor=(-0.06, 1.22), ncol=7, prop=font, columnspacing=0.1, handletextpad=0.01,
              handlelength=0.8)
    plt.grid(axis="y", alpha=0.8, linestyle=':')

    plt.savefig(str(name) + '.pdf')

    plt.show()


##===========================java->php,带折线==========================
# 画不同模型的不同指标的不同CWE类型平均数的对比(java语言迁移php),并标有最大最小值
def graphJP1(path, name):
    df = pd.read_excel(path)
    x = df['value'].values
    # 平均值
    y1 = df['μvuldeepecker'].values
    y2 = df['vuldeepecker'].values
    y3 = df['TDSC'].values
    y4 = df['VUDDY'].values
    y5 = df['Lin'].values
    y6 = df['NIPS'].values
    y7 = df['RGIN'].values
    # 最小值
    s1 = df['sμvuldeepecker'].values
    s2 = df['svuldeepecker'].values
    s3 = df['sTDSC'].values
    s4 = df['sVUDDY'].values
    s5 = df['sLin'].values
    s6 = df['sNIPS'].values
    s7 = df['sRGIN'].values
    # 最大值
    b1 = df['bμvuldeepecker'].values
    b2 = df['bvuldeepecker'].values
    b3 = df['bTDSC'].values
    b4 = df['bVUDDY'].values
    b5 = df['bLin'].values
    b6 = df['bNIPS'].values
    b7 = df['bRGIN'].values

    fig = plt.figure(figsize=(15, 3), dpi=80)
    ax = fig.add_axes([0.12, 0.25, 0.8, 0.6], zorder=11)

    ax.set_xticks(np.arange(0, 4, 1) + 0.33)
    ax.set_xticklabels(x, fontdict={'horizontalalignment': 'center', 'size': 28,'family': 'Arial'})
    ax.set_yticks(np.arange(0, 1.02, 0.2))
    ax.set_yticklabels([0, 0.2, 0.4, 0.6, 0.8, 1],
                       fontdict={'horizontalalignment': 'right', 'size': 24,'family': 'Arial'})
    ax.set_ylim((0, 1.02))
    # ax.set_ylabel('% of value', fontsize=14)
    bar_width = 0.08
    # ax.bar(x=np.arange(len(x)), height=y1, label='μVULDEEPECKER', width=bar_width, edgecolor=seaborn.xkcd_rgb['grey purple'],
    #        linewidth=1, color=seaborn.xkcd_rgb['pale purple'], zorder=10,
    #        alpha=0.9, hatch="++", align="center")
    # ax.bar(x=np.arange(len(x)) + bar_width + 0.03, height=y2, label='VULDEEPECKER', width=bar_width,
    #        edgecolor=seaborn.xkcd_rgb['grey green'],
    #        linewidth=1, color=seaborn.xkcd_rgb['light grey green'], zorder=10, alpha=0.9, hatch="||")
    # ax.bar(x=np.arange(len(x)) + 2 * bar_width + 0.06, height=y3, label='LIN et al.', width=bar_width,
    #        edgecolor=seaborn.xkcd_rgb['perrywinkle'],
    #        linewidth=1, color=seaborn.xkcd_rgb['light violet'], zorder=10, alpha=0.9, hatch="|\\|")
    # ax.bar(x=np.arange(len(x)) + 3 * bar_width + 0.09, height=y4, label='VUDDY', width=bar_width,
    #        edgecolor=seaborn.xkcd_rgb['coffee'], linewidth=1, color=seaborn.xkcd_rgb['very light brown'], zorder=10,
    #        alpha=0.9, hatch="xx")
    # ax.bar(x=np.arange(len(x)) + 4 * bar_width + 0.12, height=y5, label='DEEPBUGS', width=bar_width,
    #        edgecolor=seaborn.xkcd_rgb['grey blue'], linewidth=1, color=seaborn.xkcd_rgb['light grey blue'], zorder=10,
    #        alpha=0.9, hatch="\\\\")
    # ax.bar(x=np.arange(len(x)) + 5 * bar_width + 0.15, height=y6, label='DEVIGN', width=bar_width,
    #        edgecolor=seaborn.xkcd_rgb['rose'], linewidth=1, color=seaborn.xkcd_rgb['faded pink'], zorder=10,
    #        alpha=0.9, hatch="")
    # ax.bar(x=np.arange(len(x)) + 6 * bar_width + 0.18, height=y7, label='FUNDED', width=bar_width,
    #        edgecolor=seaborn.xkcd_rgb['orangeish'], linewidth=1, color=seaborn.xkcd_rgb['peach'], zorder=10,
    #        alpha=0.9, hatch="-/")

    # ax.bar(x=np.arange(len(x)), height=y1, label='μVULDEEPECKER',
    #        width=bar_width, edgecolor='#ede5fb',
    #        linewidth=1, color='#ede4fb', zorder=10,
    #        alpha=0.9, align="center")
    # ax.bar(x=np.arange(len(x)) + bar_width + 0.03, height=y2, label='VULDEEPECKER', width=bar_width,
    #        edgecolor='#cabfdc',
    #        linewidth=1, color='#d2c4e9', zorder=10, alpha=0.9)
    # ax.bar(x=np.arange(len(x)) + 2 * bar_width + 0.06, height=y3, label='LIN et al.', width=bar_width,
    #        edgecolor='#a79bbe',
    #        linewidth=1, color='#b7a5d8', zorder=10, alpha=0.9)
    # ax.bar(x=np.arange(len(x)) + 3 * bar_width + 0.09, height=y4, label='VUDDY', width=bar_width,
    #        edgecolor='#8678a0', linewidth=1, color='#9c86c6', zorder=10,
    #        alpha=0.9)
    # ax.bar(x=np.arange(len(x)) + 4 * bar_width + 0.12, height=y5, label='DEEPBUGS', width=bar_width,
    #        edgecolor='#655784', linewidth=1, color='#8169b5', zorder=10,
    #        alpha=0.9, )
    # ax.bar(x=np.arange(len(x)) + 5 * bar_width + 0.15, height=y6, label='DEVIGN', width=bar_width,
    #        edgecolor='#453768', linewidth=1, color='#654ca3', zorder=10,
    #        alpha=0.9)
    # ax.bar(x=np.arange(len(x)) + 6 * bar_width + 0.18, height=y7, label='FUNDED', width=bar_width,
    #        edgecolor='#261a4d', linewidth=1, color='#473192', zorder=10,
    #        alpha=0.9)

    ax.bar(x=np.arange(len(x)), height=y1, label='μVULDEEPECKER',
           width=bar_width, edgecolor='#6ea1af',
           linewidth=1, color='#72aaba', zorder=10,
           alpha=0.9, align="center")
    ax.bar(x=np.arange(len(x)) + bar_width + 0.03, height=y2, label='VULDEEPECKER', width=bar_width,
           edgecolor='#598692',
           linewidth=1, color='#6299a8', zorder=10, alpha=0.9)
    ax.bar(x=np.arange(len(x)) + 2 * bar_width + 0.06, height=y3, label='LIN et al.', width=bar_width,
           edgecolor='#456c77',
           linewidth=1, color='#518896', zorder=10, alpha=0.9)
    ax.bar(x=np.arange(len(x)) + 3 * bar_width + 0.09, height=y4, label='VUDDY', width=bar_width,
           edgecolor='#D3D3D3', linewidth=1, color='#83bccc', zorder=10,
           alpha=0.9)
    ax.bar(x=np.arange(len(x)) + 4 * bar_width + 0.12, height=y5, label='DEEPBUGS', width=bar_width,
           edgecolor='#32545d', linewidth=1, color='#417785', zorder=10,
           alpha=0.9, )
    ax.bar(x=np.arange(len(x)) + 5 * bar_width + 0.15, height=y6, label='DEVIGN', width=bar_width,
           edgecolor='#1f3c44', linewidth=1, color='#316774', zorder=10,
           alpha=0.9)
    ax.bar(x=np.arange(len(x)) + 6 * bar_width + 0.18, height=y7, label='FUNDED', width=bar_width,
           edgecolor='#0e262c', linewidth=1, color='#205764', zorder=10,
           alpha=0.9)

    # 最大最小值
    ax.hlines(y=s1, xmin=np.arange(len(x)) - 0.03, xmax=np.arange(len(x)) + 0.03, color='k', alpha=0.6, linewidth=2,
              zorder=12)
    ax.hlines(y=s2, xmin=np.arange(len(x)) + bar_width + 0.03 - 0.03, xmax=np.arange(len(x)) + bar_width + 0.04 + 0.03,
              color='k', alpha=0.6, linewidth=2.5, zorder=12)
    ax.hlines(y=s3, xmin=np.arange(len(x)) + 2 * bar_width + 0.06 - 0.03,
              xmax=np.arange(len(x)) + 2 * bar_width + 0.06 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
    ax.hlines(y=s4, xmin=np.arange(len(x)) + 3 * bar_width + 0.09 - 0.03,
              xmax=np.arange(len(x)) + 3 * bar_width + 0.09 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
    ax.hlines(y=s5, xmin=np.arange(len(x)) + 4 * bar_width + 0.12 - 0.03,
              xmax=np.arange(len(x)) + 4 * bar_width + 0.12 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
    ax.hlines(y=s6, xmin=np.arange(len(x)) + 5 * bar_width + 0.15 - 0.03,
              xmax=np.arange(len(x)) + 5 * bar_width + 0.15 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
    ax.hlines(y=s7, xmin=np.arange(len(x)) + 6 * bar_width + 0.18 - 0.03,
              xmax=np.arange(len(x)) + 6 * bar_width + 0.18 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)

    ax.hlines(y=b1, xmin=np.arange(len(x)) - 0.03, xmax=np.arange(len(x)) + 0.03, color='k', alpha=0.6, linewidth=2,
              zorder=12)
    ax.hlines(y=b2, xmin=np.arange(len(x)) + bar_width + 0.03 - 0.03, xmax=np.arange(len(x)) + bar_width + 0.04 + 0.03,
              color='k', alpha=0.6, linewidth=2.5, zorder=12)
    ax.hlines(y=b3, xmin=np.arange(len(x)) + 2 * bar_width + 0.06 - 0.03,
              xmax=np.arange(len(x)) + 2 * bar_width + 0.06 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
    ax.hlines(y=b4, xmin=np.arange(len(x)) + 3 * bar_width + 0.09 - 0.03,
              xmax=np.arange(len(x)) + 3 * bar_width + 0.09 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
    ax.hlines(y=b5, xmin=np.arange(len(x)) + 4 * bar_width + 0.12 - 0.03,
              xmax=np.arange(len(x)) + 4 * bar_width + 0.12 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
    ax.hlines(y=b6, xmin=np.arange(len(x)) + 5 * bar_width + 0.15 - 0.03,
              xmax=np.arange(len(x)) + 5 * bar_width + 0.15 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
    ax.hlines(y=b7, xmin=np.arange(len(x)) + 6 * bar_width + 0.18 - 0.03,
              xmax=np.arange(len(x)) + 6 * bar_width + 0.18 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)

    ax.vlines(x=np.arange(len(x)), ymin=s1, ymax=b1, color='k', alpha=0.6, linewidth=2, zorder=12)
    ax.vlines(x=np.arange(len(x)) + 1 * bar_width + 0.03, ymin=s2, ymax=b2, color='k', alpha=0.6, linewidth=2,
              zorder=12)
    ax.vlines(x=np.arange(len(x)) + 2 * bar_width + 0.06, ymin=s3, ymax=b3, color='k', alpha=0.6, linewidth=2,
              zorder=12)
    ax.vlines(x=np.arange(len(x)) + 3 * bar_width + 0.09, ymin=s4, ymax=b4, color='k', alpha=0.6, linewidth=2,
              zorder=12)
    ax.vlines(x=np.arange(len(x)) + 4 * bar_width + 0.12, ymin=s5, ymax=b5, color='k', alpha=0.6, linewidth=2,
              zorder=12)
    ax.vlines(x=np.arange(len(x)) + 5 * bar_width + 0.15, ymin=s6, ymax=b6, color='k', alpha=0.6, linewidth=2,
              zorder=12)
    ax.vlines(x=np.arange(len(x)) + 6 * bar_width + 0.18, ymin=s7, ymax=b7, color='k', alpha=0.6, linewidth=2,
              zorder=12)

    font = {'family': 'Arial',
            'weight': 'light',
            'size': 20.2
            }

    box = ax.get_position()
    # columnspacing=2
    ax.set_position([box.x0, box.y0, box.width, box.height * 0.8])
    ax.legend(loc='center left', bbox_to_anchor=(-0.06, 1.22), ncol=7, prop=font, columnspacing=0.1, handletextpad=0.01,
              handlelength=0.8)
    plt.grid(axis="y", alpha=0.8, linestyle=':')

    plt.savefig(str(name) + '.pdf')

    plt.show()


# def graphMC3(path, name):
#     df = pd.read_excel(path)
#     x = df['dataset'].values
#     y1 = df['μvuldeepecker'].values
#     y2 = df['LACUNA'].values
#
#     fig = plt.figure(figsize=(6, 3), dpi=80)
#     # 在bar之后添加线
#     # 0.28
#     ax = fig.add_axes([0.3, 0.3, 0.4, 0.4], zorder=11)
#
#     ax.set_xticks(np.arange(0, 2) + 0.12)
#     ax.set_xticklabels(x, fontdict={'horizontalalignment': 'center', 'size': 12,'family': 'Arial'})
#     ax.set_yticks(np.arange(0.2, 1.01, 0.2))
#     ax.set_yticklabels(['20%', '40%', '60%', '80%', '100%'],
#                        fontdict={'horizontalalignment': 'right', 'size': 12,'family': 'Arial'})
#     # plt.xlabel('SAP Dataset', fontsize=30, weight=700)
#     ax.set_ylabel('Top-3 accuracy', labelpad=0.5, fontsize=10.5)
#     ax.set_ylim((0.2, 1.01))
#     ax.set_xlim((-0.45, 1.75))
#
#     # hatch 内部填充形状{'/', '\', '|', '-', '+', 'x', 'o', 'O', '.', '*'}
#     bar_width = 0.165
#
#     ax.bar(x=np.arange(len(x)), height=y1, label='μVULDEEPECKER', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey green'],
#            linewidth=1, color=seaborn.xkcd_rgb['light grey green'], zorder=10, alpha=0.9, hatch="xxx")
#     ax.bar(x=np.arange(len(x)) + bar_width + 0.08, height=y2, label='FENCED', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey blue'],
#            linewidth=1, color=seaborn.xkcd_rgb['light grey blue'], zorder=10, alpha=0.9, hatch="")
#
#     font = {
#         'family':'Arial',
#         'weight': 'normal',
#         'size': 11
#     }
#     # plt.legend(loc='upper right', prop=font)
#     box = ax.get_position()
#     ax.set_position([box.x0, box.y0, box.width, box.height * 0.8])
#     ax.legend(loc='center left', bbox_to_anchor=(-0.1, 1.16), ncol=2, prop=font, columnspacing=1, handletextpad=0.1,
#               handlelength=1)
#     # ax.legend(loc='center left', bbox_to_anchor=(0.33, 0.7), ncol=1, prop=font)
#
#     plt.grid(axis="y", alpha=0.8, linestyle=':')
#     plt.savefig(str(name) + '.pdf')
#
#     plt.show()
#
#
# def graphMC5(path, name):
#     df = pd.read_excel(path)
#     x = df['model'].values
#     y1 = df['accuracy'].values
#
#     fig = plt.figure(figsize=(8.8, 2.5), dpi=80)
#     # 在bar之后添加线
#     # 0.28
#     ax = fig.add_axes([0.3, 0.3, 0.4, 0.4], zorder=11)
#
#     # ax.set_xticks(np.arange(0, 4))
#     # ax.set_xticklabels("", fontdict={'horizontalalignment': 'center', 'size': 12,'rotation':0})
#     ax.set_xticks([])
#     ax.set_yticks(np.arange(0.7, 1.01, 0.1))
#     ax.set_yticklabels(['70%','80%','90%','100%'],
#                        fontdict={'horizontalalignment': 'right', 'size': 15,'family': 'Arial'})
#     # plt.xlabel('SAP Dataset', fontsize=30, weight=700)
#     ax.set_ylabel('Accuracy', labelpad=0.5, fontsize=18,fontdict={'family': 'Arial'})
#     ax.set_ylim((0.7, 1.01))
#     # ax.set_xlim((-0.45, 1.75))
#
#     # hatch 内部填充形状{'/', '\', '|', '-', '+', 'x', 'o', 'O', '.', '*'}
#     bar_width = 0.35
#
#     ax.bar(x=np.arange(len(x)), height=y1,  width=bar_width,
#            edgecolor=[seaborn.xkcd_rgb['tan'],seaborn.xkcd_rgb['grey green'],seaborn.xkcd_rgb['grey blue'],seaborn.xkcd_rgb['grey purple']],
#            linewidth=1, color=[seaborn.xkcd_rgb['yellow tan'],seaborn.xkcd_rgb['light grey green'],seaborn.xkcd_rgb['light grey blue'],seaborn.xkcd_rgb['pale purple']],
#            zorder=10, alpha=0.9)
#
#     # font = {
#     #     'family': 'Times New Roman',
#     #     'weight': 'normal',
#     #     'size': 11
#     # }
#     # plt.legend(loc='upper right', prop=font)
#     # box = ax.get_position()
#     # ax.set_position([box.x0, box.y0, box.width, box.height * 0.8])
#     # ax.legend(loc='center left', bbox_to_anchor=(-0.1, 1.16), ncol=2, prop=font, columnspacing=1, handletextpad=0.1,
#     #           handlelength=1)
#     # ax.legend(loc='center left', bbox_to_anchor=(0.33, 0.7), ncol=1, prop=font)
#
#     plt.grid(axis="y", alpha=0.8, linestyle=':')
#     plt.savefig(str(name) + '.pdf')
#
#     plt.show()
#
#
# def demo(path, name):
#     df = pd.read_excel(path)
#     x = df['x'].values
#     y1 = df['y1'].values
#     y2 = df['y2'].values
#
#     fig = plt.figure(figsize=(6, 3), dpi=80)
#     # 参数1，参数2，参数3，参数4
#     ax = fig.add_axes([0.3, 0.3, 0.4, 0.4])
#
#     # 固定x轴有几个值（+0.xx是在调整这几个值的位置）
#     ax.set_xticks(np.arange(0, 2) + 0.12)
#     # 设置x轴的每个值的标签
#     ax.set_xticklabels(x, fontdict={'horizontalalignment': 'center', 'size': 12})
#     ax.set_yticks(np.arange(0.2, 1.01, 0.2))
#     ax.set_yticklabels(['20%', '40%', '60%', '80%', '100%'], fontdict={'horizontalalignment': 'right', 'size': 12})
#     # 设置x轴标题
#     ax.set_xlabel('X', fontsize=10.5, weight=700)
#     ax.set_ylabel('Y', labelpad=0.5, fontsize=10.5, weight=700)
#     # 设置x轴范围
#     ax.set_ylim((0.2, 1.01))
#     ax.set_xlim((-0.45, 1.75))
#
#     # hatch 内部填充形状{'/', '\', '|', '-', '+', 'x', 'o', 'O', '.', '*'}
#     bar_width = 0.165
#     ax.bar(x=np.arange(len(x)), height=y1, label='A', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey green'],
#            linewidth=1, color=seaborn.xkcd_rgb['light grey green'], zorder=10, alpha=0.9, hatch="xxx")
#     ax.bar(x=np.arange(len(x)) + bar_width + 0.08, height=y2, label='B', width=bar_width,
#            edgecolor=seaborn.xkcd_rgb['grey blue'],
#            linewidth=1, color=seaborn.xkcd_rgb['light grey blue'], zorder=10, alpha=0.9, hatch="")
#
#     # 显示数字标签为百分数
#     for a, b in enumerate(y1):
#         # ha为水平位置，va为垂直位置
#         plt.text(a, b, '%.0f%%' % (b * 100), ha='center', va='bottom', fontdict={'size': 9})
#     for a, b in enumerate(y2):
#         plt.text(a + 0.25, b, '%.0f%%' % (b * 100), ha='center', va='bottom', fontdict={'size': 9})
#
#     font = {
#         'family': 'Times New Roman',
#         'weight': 'normal',
#         'size': 11
#     }
#     plt.legend(loc='upper right', prop=font)
#     # box = ax.get_position()
#     # ax.set_position([box.x0, box.y0, box.width, box.height * 0.8])
#     # ax.legend(loc='center left', bbox_to_anchor=(-0.1, 1.16), ncol=2, prop=font,
#     #           columnspacing=1,handletextpad=0.1,handlelength=1)
#
#     plt.grid(axis="y", alpha=0.8, linestyle=':')
#
#     plt.savefig(str(name) + '.pdf')
#     plt.show()

#边的对比的实验
# 画FUNDED模型的不同边的不同指标的平均数的对比,并标有最大最小值
def graphEM(path, name):
    df = pd.read_excel(path)
    x = df['value'].values
    # 平均值
    y1 = df['AST'].values
    y2 = df['7Edges'].values
    y3 = df['c_cdfg'].values
    y4 = df['all'].values
    y5 = df['7Edges+CDFG'].values

    # 最小值
    s1 = df['sAST'].values
    s2 = df['s7Edges'].values
    s3 = df['sc_cdfg'].values
    s4 = df['sall'].values
    s5 = df['s7Edges+CDFG'].values
    # 最大值
    b1 = df['bAST'].values
    b2 = df['b7Edges'].values
    b3 = df['bc_cdfg'].values
    b4 = df['ball'].values
    b5 = df['b7Edges+CDFG'].values

    fig = plt.figure(figsize=(9, 3), dpi=80)
    ax = fig.add_axes([0.12, 0.15, 0.8, 0.6], zorder=11)

    ax.set_xticks(np.arange(0, 4, 1)+0.3)
    ax.set_xticklabels(x, fontdict={'horizontalalignment': 'center', 'size': 20,'family': 'Arial'})
    ax.set_yticks(np.arange(0.6, 1.02, 0.1))
    ax.set_yticklabels([0.6,0.7, 0.8,0.9, 1],
                       fontdict={'horizontalalignment': 'right', 'size': 20,'family': 'Arial'})
    ax.set_ylim((0.6, 1.02))
    # ax.set_ylabel('% of value', fontsize=14)
    bar_width = 0.12
    # ax.bar(x=np.arange(len(x)), height=y1, label='F-vanilla-AST', width=bar_width, edgecolor=seaborn.xkcd_rgb['tan'],
    #        linewidth=1, color=seaborn.xkcd_rgb['yellow tan'], zorder=10,
    #        alpha=0.9, hatch="//", align="center")
    # ax.bar(x=np.arange(len(x)) + bar_width + 0.03, height=y2, label='F-AST', width=bar_width,
    #        edgecolor=seaborn.xkcd_rgb['grey green'],
    #        linewidth=1, color=seaborn.xkcd_rgb['light grey green'], zorder=10, alpha=0.9, hatch="xx")
    # ax.bar(x=np.arange(len(x)) + 2 * bar_width + 0.06, height=y3, label='F-CDFG', width=bar_width,
    #        edgecolor=seaborn.xkcd_rgb['grey blue'],
    #        linewidth=1, color=seaborn.xkcd_rgb['light grey blue'], zorder=10, alpha=0.9, hatch="")
    # ax.bar(x=np.arange(len(x)) + 3 * bar_width + 0.09, height=y4, label='F-CONCAT', width=bar_width,
    #        edgecolor=seaborn.xkcd_rgb['grey purple'], linewidth=1, color=seaborn.xkcd_rgb['pale purple'], zorder=10,
    #        alpha=0.9, hatch="++")
    # ax.bar(x=np.arange(len(x)) + 4 * bar_width + 0.12, height=y5, label='FUNDED', width=bar_width,
    #        edgecolor=seaborn.xkcd_rgb['rose'], linewidth=1, color=seaborn.xkcd_rgb['faded pink'], zorder=10,
    #        alpha=0.9, hatch="\\\\")

    ax.bar(x=np.arange(len(x)), height=y1, label='F-vanilla-AST', width=bar_width,
           edgecolor='#D3D3D3',linewidth=1, color='#ede4fb', zorder=10,
           alpha=0.9, align="center")
    ax.bar(x=np.arange(len(x)) + bar_width + 0.03, height=y2, label='F-AST', width=bar_width,
           edgecolor='#b8adcd',
           linewidth=1, color='#c5b4e0', zorder=10, alpha=0.9,)
    ax.bar(x=np.arange(len(x)) + 2 * bar_width + 0.06, height=y3, label='F-CDFG', width=bar_width,
           edgecolor='#8678a0',
           linewidth=1, color='#9c86c6', zorder=10, alpha=0.9)
    ax.bar(x=np.arange(len(x)) + 3 * bar_width + 0.09, height=y4, label='F-CONCAT', width=bar_width,
           edgecolor='#554776', linewidth=1, color='#735bac', zorder=10,
           alpha=0.9)
    ax.bar(x=np.arange(len(x)) + 4 * bar_width + 0.12, height=y5, label='FUNDED', width=bar_width,
           edgecolor='#261a4d', linewidth=1, color='#473192', zorder=10,
           alpha=0.9)


    # 最大最小值
    ax.hlines(y=s1, xmin=np.arange(len(x)) - 0.03, xmax=np.arange(len(x)) + 0.03, color='k', alpha=0.6, linewidth=2,
              zorder=12)
    ax.hlines(y=s2, xmin=np.arange(len(x)) + bar_width + 0.03 - 0.03, xmax=np.arange(len(x)) + bar_width + 0.04 + 0.03,
              color='k', alpha=0.6, linewidth=2.5, zorder=12)
    ax.hlines(y=s3, xmin=np.arange(len(x)) + 2 * bar_width + 0.06 - 0.03,
              xmax=np.arange(len(x)) + 2 * bar_width + 0.06 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
    ax.hlines(y=s4, xmin=np.arange(len(x)) + 3 * bar_width + 0.09 - 0.03,
              xmax=np.arange(len(x)) + 3 * bar_width + 0.09 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
    ax.hlines(y=s5, xmin=np.arange(len(x)) + 4 * bar_width + 0.12 - 0.03,
              xmax=np.arange(len(x)) + 4 * bar_width + 0.12 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)


    ax.hlines(y=b1, xmin=np.arange(len(x)) - 0.03, xmax=np.arange(len(x)) + 0.03, color='k', alpha=0.6, linewidth=2,
              zorder=12)
    ax.hlines(y=b2, xmin=np.arange(len(x)) + bar_width + 0.03 - 0.03, xmax=np.arange(len(x)) + bar_width + 0.04 + 0.03,
              color='k', alpha=0.6, linewidth=2.5, zorder=12)
    ax.hlines(y=b3, xmin=np.arange(len(x)) + 2 * bar_width + 0.06 - 0.03,
              xmax=np.arange(len(x)) + 2 * bar_width + 0.06 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
    ax.hlines(y=b4, xmin=np.arange(len(x)) + 3 * bar_width + 0.09 - 0.03,
              xmax=np.arange(len(x)) + 3 * bar_width + 0.09 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)
    ax.hlines(y=b5, xmin=np.arange(len(x)) + 4 * bar_width + 0.12 - 0.03,
              xmax=np.arange(len(x)) + 4 * bar_width + 0.12 + 0.03, color='k', alpha=0.6, linewidth=2.5, zorder=12)


    ax.vlines(x=np.arange(len(x)), ymin=s1, ymax=b1, color='k', alpha=0.6, linewidth=2, zorder=12)
    ax.vlines(x=np.arange(len(x)) + 1 * bar_width + 0.03, ymin=s2, ymax=b2, color='k', alpha=0.6, linewidth=2,
              zorder=12)
    ax.vlines(x=np.arange(len(x)) + 2 * bar_width + 0.06, ymin=s3, ymax=b3, color='k', alpha=0.6, linewidth=2,
              zorder=12)
    ax.vlines(x=np.arange(len(x)) + 3 * bar_width + 0.09, ymin=s4, ymax=b4, color='k', alpha=0.6, linewidth=2,
              zorder=12)
    ax.vlines(x=np.arange(len(x)) + 4 * bar_width + 0.12, ymin=s5, ymax=b5, color='k', alpha=0.6, linewidth=2,
              zorder=12)


    font = {'family':'Arial',
            'weight': 'light',
            'size': 20
            }

    box = ax.get_position()
    # columnspacing=2
    ax.set_position([box.x0, box.y0, box.width, box.height * 0.8])
    ax.legend(loc='center left', bbox_to_anchor=(-0.09, 1.2), ncol=5, prop=font, columnspacing=0.15, handletextpad=0.05,
              handlelength=0.8)
    plt.grid(axis="y", alpha=0.8, linestyle=':')

    plt.savefig(str(name) + '.pdf')

    plt.show()

#画多分类的不同模型的accuracy的对比
def graphMul(path, name):
    df = pd.read_excel(path)
    x = df['x'].values
    # 平均值
    y1 = df['μVuldeepecker'].values
    y2 = df['RGCN'].values
    y3 = df['Devign'].values
    y4 = df['FUNDED'].values

    fig = plt.figure(figsize=(8, 3), dpi=80)
    # 在bar之后添加线
    # 0.28
    ax = fig.add_axes([0.3, 0.3, 0.4, 0.4], zorder=11)

    # ax.set_xticks(np.arange(0, 4))
    # ax.set_xticklabels("", fontdict={'horizontalalignment': 'center', 'size': 12,'rotation':0})
    ax.set_xticks([])
    ax.set_yticks(np.arange(0.7, 0.95, 0.1))
    ax.set_yticklabels(['70%', '80%', '90%'],
                       fontdict={'horizontalalignment': 'right', 'size': 13,'family': 'Arial'})
    # plt.xlabel('SAP Dataset', fontsize=30, weight=700)
    ax.set_ylabel('Accuracy', labelpad=0.5, fontsize=13,fontdict={'family': 'Arial'})
    ax.set_ylim((0.7, 0.95))

    bar_width = 0.01

    # ax.bar(x=np.arange(len(x)), height=y1, label='μVULDEEPECKER', width=bar_width, edgecolor=seaborn.xkcd_rgb['grey purple'],
    #        linewidth=1, color=seaborn.xkcd_rgb['pale purple'], zorder=10,
    #        alpha=0.9, hatch="++", align="center")
    # ax.bar(x=np.arange(len(x)) + bar_width + 0.015, height=y2, label='RGCN', width=bar_width,
    #        edgecolor=seaborn.xkcd_rgb['tan'],
    #        linewidth=1, color=seaborn.xkcd_rgb['yellow tan'], zorder=10, alpha=0.9, hatch="//")
    # ax.bar(x=np.arange(len(x)) + 2 * bar_width + 0.03, height=y3, label='DEVIGN', width=bar_width,
    #        edgecolor=seaborn.xkcd_rgb['rose'],
    #        linewidth=1, color=seaborn.xkcd_rgb['faded pink'], zorder=10, alpha=0.9, hatch="")
    # ax.bar(x=np.arange(len(x)) + 3 * bar_width + 0.045, height=y4, label='FUNDED', width=bar_width,
    #        edgecolor=seaborn.xkcd_rgb['orangeish'], linewidth=1, color=seaborn.xkcd_rgb['peach'], zorder=10,
    #        alpha=0.9, hatch="-/")

    ax.bar(x=np.arange(len(x)), height=y1, label='μVULDEEPECKER', width=bar_width,
           linewidth=1, edgecolor='#D3D3D3', color='#ede4fb', zorder=10, alpha=0.9, hatch="")
    ax.bar(x=np.arange(len(x)) + bar_width + 0.015, height=y2, label='RGCN', width=bar_width,
           linewidth=1, edgecolor='#a79bbe', color='#c5b4e0', zorder=10,
           alpha=0.9, hatch="")
    ax.bar(x=np.arange(len(x)) + 2 * bar_width + 0.03, height=y3, label='DEVIGN', width=bar_width,
           linewidth=1, edgecolor='#655784', color='#9c86c6', zorder=10,
           alpha=0.9, hatch="")
    ax.bar(x=np.arange(len(x)) + 3 * bar_width + 0.045, height=y4, label='FUNDED', width=bar_width,
           linewidth=1, color='#735bac', zorder=10)

    font = {'family': 'Arial',
            'weight': 'light',
            'size': 12
            }

    box = ax.get_position()
    # columnspacing=2
    ax.set_position([box.x0, box.y0, box.width, box.height * 0.8])
    # ax.legend(loc='center left', bbox_to_anchor=(-0.2, 1.5), ncol=2, prop=font, columnspacing=0.5, handletextpad=0.1,
    #           handlelength=2)
    #放在内部
    # ax.legend(loc='center left', bbox_to_anchor=(0, 0.7), ncol=2, prop=font, columnspacing=0.1, handletextpad=0.05,
    #           handlelength=1)
    #放在外部
    ax.legend(loc='center left', bbox_to_anchor=(-0.04, 1.3), ncol=2, prop=font, columnspacing=1, handletextpad=0.5,
              handlelength=2)
    plt.grid(axis="y", alpha=0.8, linestyle=':')

    plt.savefig(str(name) + '.pdf')

    plt.show()

if __name__ == '__main__':
    #画ccs的不同模型的不同CWE类型的accuracy的对比
    path = r"CCS_graph/histogram_linechart/CCS/accuracy1.xlsx"
    graphSA(path, 'CCS\\5_2\\Eva_SardAccuracy')

    #画不同模型的不同指标的不同CWE类型平均数的对比（github）,并标有最大最小值
    path = r"CCS_graph/histogram_linechart/CCS/SGM.xlsx"
    graphSGM(path, r'CCS\5_2\Eva_SardGithub')

    #画不同模型的不同指标的不同CWE类型平均数的对比（sard）,并标有最大最小值
    path = r"CCS_graph/histogram_linechart/CCS/SM.xlsx"
    graphSM(path, r'CCS/5_2\Eva_Sard_mean')

    #画不同模型的不同指标的不同CWE类型平均数的对比(c语言迁移java),并标有最大最小值
    path = r"CCS_graph/histogram_linechart/CCS/cj.xlsx"
    graphCJ1(path, r'CCS/5_2\Eva_QYcjava_mean')

    # 画不同模型的不同指标的不同CWE类型平均数的对比(c语言迁移swift),并标有最大最小值
    path = r"CCS_graph/histogram_linechart/CCS/cs.xlsx"
    graphCS1(path, r'CCS/5_2\Eva_QYcswift_mean')

    # 画不同模型的不同指标的不同CWE类型平均数的对比(java语言迁移php),并标有最大最小值
    path = r"CCS_graph/histogram_linechart/CCS/jp.xlsx"
    graphJP1(path, r'CCS/5_2\Eva_QYjavaphp_mean')

    # 画FUNDED模型的不同边的不同指标的平均数的对比,并标有最大最小值
    path = r"CCS_graph/histogram_linechart/CCS/EM.xlsx"
    graphEM(path, r'CCS/5_2\Eva_EM')

    #画多分类的不同模型的accuracy的对比
    path = r"CCS_graph/histogram_linechart/CCS/mul2.xlsx"
    graphMul(path, r'CCS/5_2\Eva_Multiclass')

    #画往不同模型中添加数据的不同指标的不同CWE类型平均数的对比（vuldeepecker）,并标有最大最小值
    path = r"CCS_graph/histogram_linechart/CCS/AV.xlsx"
    graphAV1(path,  r'CCS/5_2\Eva_addVul')

    # 画往不同模型中添加数据的不同指标的不同CWE类型平均数的对比（uvuldeepecker）,并标有最大最小值
    path = r"CCS_graph/histogram_linechart/CCS/AUV.xlsx"
    graphAUV1(path, r'CCS/5_2/Eva_addUvul')

    #画FUNDED模型的不同CWE的不同指标的对比
    path = r"CCS_graph/histogram_linechart/CCS/FUNDED.xlsx"
    graphLACUNA(path, r'CCS/5_2/Eva_FUNDED')