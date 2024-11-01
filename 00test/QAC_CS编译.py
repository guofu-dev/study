import pandas as pd
import os
import sys

define = 1 #选择1-6进行编译
suffix = 0
if len(sys.argv) > 1:  
    suffix = int(sys.argv[1])
else:
    suffix = define

# 判断文件是否存在
if suffix == 1 or suffix == 2 or suffix == 3:
    MdType = 'QAC'
    Cntt = 1
    sheet_name_in='warn'
    if suffix == 1:
        file_path_new = './NEW_DNKT_QACResult_QAC_result_detail_CR7_APP.xlsm'
        file_path_old = './OLD_DNKT_QACResult_QAC_result_detail_CR7_APP.xlsm'
        sheet_name_out='CR7'
    elif suffix == 2:
        file_path_new = './NEW_DNKT_QACResult_MET.xlsm'
        file_path_old = './OLD_DNKT_QACResult_MET.xlsm'
        sheet_name_out='MET'
    else:
        file_path_new = './NEW_DNKT_QACResult_HUD.xlsm'
        file_path_old = './OLD_DNKT_QACResult_HUD.xlsm'
        sheet_name_out='HUD'
elif suffix == 4 or suffix == 5 or suffix == 6:
    MdType = 'CodeSonar'
    Cntt = 0
    sheet_name_in='警告一覧'
    if suffix == 4:
        file_path_new = './NEW_DNKT_19PFv3_CR7_CS.xlsm'
        file_path_old = './OLD_DNKT_19PFv3_CR7_CS.xlsm'
        sheet_name_out='CR7'
    elif suffix == 5:
        file_path_new = './NEW_DNKT_19PFv3_SoC_gfx_agl_met_CS.xlsm'
        file_path_old = './OLD_DNKT_19PFv3_SoC_gfx_agl_met_CS.xlsm'
        sheet_name_out='MET'
    else:
        file_path_new = './NEW_DNKT_19PFv3_SoC_gfx_agl_hud_CS.xlsm'
        file_path_old = './OLD_DNKT_19PFv3_SoC_gfx_agl_hud_CS.xlsm'
        sheet_name_out='HUD'
else:
    MdType = 'Non'
    pass

if(MdType =='Non'):
    print("Pleas Input Valid Number !!!")
else:
    df_a = pd.read_excel(file_path_new, sheet_name=sheet_name_in)
    df_a = df_a.iloc[Cntt:]
    df_b = pd.read_excel(file_path_old, sheet_name=sheet_name_in)
    df_b = df_b.iloc[Cntt:]
    print("argv : {}\nQAC_CS : {}\nCR7_MET_HUD : {}".format(suffix, MdType, sheet_name_out))

flag = 0
############################ QAC CASE HEAD ################################
if(MdType == 'QAC'):
    for indexa, row_a in df_a.iterrows():
        if row_a[0]  == "相違":
            continue
        if (file_path_new == './NEW_DNKT_QACResult_QAC_result_detail_CR7_APP.xlsm') and (row_a[10] != "SoC R"): #适配NEW CR7
            continue
        if (file_path_new != './NEW_DNKT_QACResult_QAC_result_detail_CR7_APP.xlsm') and (row_a[10] != "src_folder"): #适配NEW A57
            continue
        flag = 0
        for indexb, row_b in df_b.iterrows():
            if (file_path_old == './OLD_DNKT_QACResult_QAC_result_detail_CR7_APP.xlsm') and (row_b[10] != "SoC R"): #适配OLD CR7
                continue
            if (file_path_old != './OLD_DNKT_QACResult_QAC_result_detail_CR7_APP.xlsm') and (row_b[10] != "src_folder"): #适配OLD A57
                continue
            # 检查"File"、"Line"、"Rule"列的内容是否相同
            if (row_a[1] == row_b[1]) and (row_a[2] == row_b[2]) and (row_a[6] == row_b[6]) and (row_a[5] == row_b[5]):  
                for i in range(12,20):
                    row_a[i] = row_b[i]
                row_a[20] = "SUCC0"
                break
            elif (row_a[1] == row_b[1]) and (row_a[6] == row_b[6]) and (row_a[5] == row_b[5]):
                for i in range(12,20):
                    row_a[i] = row_b[i]
                row_a[20] = "SUCC1"
                flag = 1
            elif (row_a[1] == row_b[1]) and (row_a[6] == row_b[6]):
                if(flag == 0):
                    for i in range(12,20):
                        row_a[i] = row_b[i]
                    row_a[20] = "SUCC2"
                    flag = 1
            elif (row_a[1] == row_b[1]):
                if(flag == 0):
                    row_a[20] = "MDY1"
            else:
                pass
############################ QAC CASE TAIL ################################

elif(MdType == 'CodeSonar'):
############################ CodeSonar CASE HEAD ################################
    for indexa, row_a in df_a.iterrows():
        if row_a[14] == "有り":
            continue
        if row_a[17] == "対象外":
            continue
        if (file_path_new == './NEW_DNKT_19PFv3_CR7_CS.xlsm') and (row_a[18] != "SoC R"): #适配NEW CR7
            continue
        flag = 0
        for indexb, row_b in df_b.iterrows():  
            if row_b[17] == "対象外":
                continue
            if (file_path_old == './OLD_DNKT_19PFv3_CR7_CS.xlsm') and (row_b[18] != "SoC R"): #适配OLD CR7
                continue
            # 检查"File"、"Line"、"Rule"列的内容是否相同  
            if (row_a[4] == row_b[4]) and (row_a[6] == row_b[6]) and (row_a[2] == row_b[2]) and (row_a[7] == row_b[7]):
                for i in range(21,28):
                    df_a.at[indexa, i] = row_b[i]
                df_a.at[indexa, 28] = "SUCC0"
                break
            elif (row_a[4] == row_b[4]) and (row_a[2] == row_b[2]) and (row_a[7] == row_b[7]): 
                for i in range(21,28):
                    df_a.at[indexa, i] = row_b[i]
                df_a.at[indexa, 28] = "SUCC1" 
                flag = 1
            elif (row_a[4] == row_b[4]) and (row_a[7] == row_b[7]):
                if(flag == 0):
                    for i in range(21,28):
                        df_a.at[indexa, i] = row_b[i]
                    df_a.at[indexa, 28] = "SUCC2"
                    flag = 1
            elif (row_a[4] == row_b[4]):
                if(flag == 0):
                    df_a.at[indexa, 28] = "MDY1"
            else:
                pass
############################ CodeSonar CASE TAIL ################################

if(MdType !='Non'):           
    if not os.path.exists('update_{}_File.xlsx'.format(MdType)): #如果不存在则创建文件
        df = pd.DataFrame()
        df.to_excel('update_{}_File.xlsx'.format(MdType), index=False)
    with pd.ExcelWriter('update_{}_File.xlsx'.format(MdType), engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
        df_a.to_excel(writer, sheet_name=sheet_name_out, index=False)
        print("更新文件已保存为 updated_{}_Core_{}_File.xlsx".format(MdType,sheet_name_out))
    print("更新完成")
