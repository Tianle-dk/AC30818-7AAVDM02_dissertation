#
# import pandas as pd
#
#
# def xlsx_to_csv_pd():
#     data_xls = pd.read_excel('词频.xlsx', index_col=0)
#     data_xls.to_csv('词频.csv', encoding='utf-8')
#
#
# if __name__ == '__main__':
#     xlsx_to_csv_pd()

import pandas


# 格式转换
def Excel_to_Txt(input_path, output_path):
    df = pandas.read_excel(input_path, header=None)
    print('开始写入txt文件')
    df.to_csv(output_path, header=None, sep=',', index=False)  # sep指定分隔符，分隔单元格
    print('写入成功')


# 创建同路径同名TXT文件
def creat_txt(input_path):
    length = len(input_path)
    output_path = ''
    for i in range(length - 1, -1, -1):
        if input_path[i] == '.':
            break
    for j in range(0, i + 1):
        output_path = output_path + input_path[j]
    output_path = output_path + 'txt'
    # file = open(output_path,)
    return output_path


if __name__ == '__main__':
    # input_path = r'E:\pycharmfile\littleredbook\处理后词频.xlsx'
    input_path = r'E:\pycharmfile\littleredbook\词频.xlsx'

    output_path = creat_txt(input_path)
    Excel_to_Txt(input_path, output_path)
