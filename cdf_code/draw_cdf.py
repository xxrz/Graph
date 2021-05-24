# -- coding:UTF-8 --

import numpy as np
import statsmodels.api as sm # recommended import according to the docs
import matplotlib.pyplot as plt
import os
import re
import json
import pandas as pd
import seaborn

#画cdf图
# def draw_cdf(data, xlabel='x', ylabel='CDF', title=None):
#     sample = data
#     ecdf = sm.distributions.ECDF(sample)
#     # x = np.linspace(0, max(sample))
#     #控制横轴的坐标范围
#     x = np.linspace(0, 1000)
#     y = ecdf(x)
#     plt.plot(x, y, linewidth='1')
#     # plt.plot(x, y, linewidth='1', label='label')
#     plt.xlabel(xlabel)
#     plt.ylabel(ylabel)
#     plt.title(title)
#     # plt.legend(loc='upper left')
#     plt.show()
#
# #将数据写入excel,再用于画图（可废）
# def data_to_excel(data):
#     sample = data
#     ecdf = sm.distributions.ECDF(sample)
#     x = np.linspace(0, max(sample))
#     x = x.reshape(x.size,1)
#     y = ecdf(x)
#     y = y.reshape(y.size, 1)
#
#     data = np.hstack((x, y))
#     # 写入excel
#     data = pd.DataFrame(data,columns=['x','y'])
#     writer = pd.ExcelWriter(r'code.xlsx')  # 写入Excel文件
#     data.to_excel(writer, index=False)
#     writer.save()
#     writer.close()

#画cdf的code的图
def code(data, xlabel='x', ylabel='CDF', title=None):
    sample = data
    ecdf = sm.distributions.ECDF(sample)
    # x = np.linspace(0, max(sample))
    x = np.linspace(0, 200)
    y = ecdf(x)

    fig = plt.figure(figsize=(8, 4), dpi=80)
    ax = fig.add_axes([0.2, 0.3, 0.6, 0.6], zorder=11)
    ax.set_xticks(np.arange(0, 205, 40))
    ax.set_xticklabels(np.arange(0, 205, 40), fontdict={'horizontalalignment': 'center', 'size': 20,'family': 'Arial'})
    ax.set_yticks(np.arange(0, 1.02, 0.2))
    ax.set_yticklabels([0, 0.2, 0.4, 0.6, 0.8, 1],
                       fontdict={'horizontalalignment': 'right', 'size': 20,'family': 'Arial'})
    ax.set_xlabel('code_num', fontsize=22,fontdict={'family': 'Arial'})
    ax.set_ylabel('CDF', fontsize=22,fontdict={'family': 'Arial'})
    ax.set_xlim((0, 205))
    ax.set_ylim((0, 1.02))

    ax.plot(x, y, linestyle="-", linewidth=3, color='#8169b5')

    plt.grid(axis="y", alpha=0.8, linestyle=':')

    # 可以保存为svg这种矢量图片的格式,放大不会有锯齿
    plt.savefig('code_num.pdf')

    # 对保存的图片进行显示
    plt.show()

#画cdf的node的图
def node(data, xlabel='x', ylabel='CDF', title=None):
    sample = data
    ecdf = sm.distributions.ECDF(sample)
    # x = np.linspace(0, max(sample))
    x = np.linspace(0, 600)
    y = ecdf(x)

    fig = plt.figure(figsize=(8, 4), dpi=80)
    ax = fig.add_axes([0.2, 0.3, 0.6, 0.6], zorder=11)
    ax.set_xticks(np.arange(0, 610, 100))
    ax.set_xticklabels(np.arange(0, 610, 100), fontdict={'horizontalalignment': 'center', 'size': 20,'family': 'Arial'})
    ax.set_yticks(np.arange(0, 1.02, 0.2))
    ax.set_yticklabels([0, 0.2, 0.4, 0.6, 0.8, 1],
                       fontdict={'horizontalalignment': 'right', 'size': 20,})
    ax.set_xlabel('node_num', fontsize=22,fontdict={'family': 'Arial'})
    ax.set_ylabel('CDF', fontsize=22,fontdict={'family': 'Arial'})
    ax.set_xlim((0, 610))
    ax.set_ylim((0, 1.02))

    ax.plot(x, y, linestyle="-", linewidth=3, color='#8169b5')

    plt.grid(axis="y", alpha=0.8, linestyle=':')

    # 可以保存为svg这种矢量图片的格式,放大不会有锯齿
    plt.savefig('node_num.pdf')

    # 对保存的图片进行显示
    plt.show()

def get_code_and_node_num(cwe_path):
    file_num = 0
    max_file_num = float("inf")
    json_dict = {"dir_name":cwe_path.split('/')[-1],"details":[]}
    for file_name in os.listdir(cwe_path):
        # =======控制文件数量========
        file_num += 1
        if file_num>max_file_num:
            break
        # =========================
        # 初始化flag和统计值
        code_flag = False
        node_flag = False
        code_num = 0
        node_num = 0

        with open(os.path.join(cwe_path,file_name),'r') as f:
            for line in f.readlines():
                if re.search('-----children-----', line):
                    code_flag = False
                if re.search('-----joern-----',line):
                    node_flag = False
                if code_flag:
                    code_num += 1
                if node_flag:
                    node_num += 1
                if re.search('-----code-----', line):
                    code_flag= True
                if re.search('-----ast_node-----', line):
                    node_flag = True

        file_dict = {'file_name':file_name, 'code_num':code_num, 'node_num':node_num}
        json_dict["details"].append(file_dict)
    return json_dict

def write_json_to_file(data_path):
    json_data = []
    for dir_name in os.listdir(data_path):
        if re.match(r'CWE-[0-9]*$',dir_name):
            json_dict = get_code_and_node_num(os.path.join(data_path, dir_name))
            json_data.append(json_dict)
    with open('statistic.json','w') as f:
        json.dump(json_data,f)

def draw_cdf_for_json(json_path):
    node_num = []
    code_num = []
    with open(json_path, 'r') as f:
        json_data = json.load(f)
        for cwe in json_data:
            for txt in cwe['details']:
                code_num.append(txt['code_num'])
                node_num.append(txt['node_num'])
    #绘制cdf图
    node(node_num,xlabel='node_num')
    code(code_num,xlabel='code_num')

    # data_to_excel(node_num)
    # data_to_excel(code_num)


if __name__ == '__main__':
    # write_json_to_file('/CCS/sardc')
    # draw_cdf_for_json('sardc_statistic.json')
    #需要用于解析和画图的文件
    draw_cdf_for_json('statistic-github&sard.json')
