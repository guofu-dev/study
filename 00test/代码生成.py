import pandas as pd
# 读取Excel文件 excel_file第1行留空.xlsx
# 信号名           类型   报文id
# FRS_AEBS_State_1  uint8 206
df = pd.read_excel('new_已评审_GEELY_CV_DHU_CANFD_V4.4_20240428.xlsx')    
df = df.iloc[0:]  # 只保留从第1行开始的数据
# 将第一列数据写入TXT文件  
signal_pre = 'OLD'
signal_name = 'NEW'

with open('output.c', 'w', encoding='utf-8') as f:  
  head_file = "#include \"obcm.h\"\n#include \"odo.h\"\n"
  f.write("%s\n" % head_file)
  for indexa, row in df.iterrows(): #从第一行开始遍历
    if(row['Signal Name'] != signal_pre) & (row['Launch Type'] == 'Cyclic'):

      # signal_name = row['信号名'].replace(' ', '_').replace('-', '_')  # 假设列名是“信号名” 将信号名中的空格和短横线替换为下划线 
      signal_name = row['Signal Name']
      data_type   = 'uint8'
      # data_type   = row['类型']  # 假设列名是“类型”（但在这个例子中我们实际上没有使用它）  
      message_id  = row['ID']  # 假设列名是“报文id”  
      signal_pre = signal_name
      
      #方法1 好理解，但代码视觉差
      # result1 = "static " + data_type + " Cansignal_" + signal_name + "(void)\n"\
      #           "{\n"\
      #           "  " + data_type + " req = 0;\n" \
      #           "  CanGenIf_Rx_" +  str(message_id) + "_Get_" +signal_name + "();\n"\
      #           "  return req;\n"\
      #           "}\n"
      # f.write("%s\n" % result1)
      # 方法2 构造C语言函数字符串
      result2 = f"""static {data_type} Cansignal_{signal_name}(void)
{{
  {data_type} req = 0;
  CanGenIf_Rx_{message_id}_Get_{signal_name}();
  return req;
}}
"""
      f.write(result2 + '\n\n')
print("output.c")
