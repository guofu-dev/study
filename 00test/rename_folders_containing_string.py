import os  

def rename_folders_containing_string(target_directory, search_string, suffix="1yang_"):  
    # 遍历目标目录下的所有项目  
    for item in os.listdir(target_directory):  
        # 构建项目的完整路径  
        item_path = os.path.join(target_directory, item)  
          
        # 检查项目是否是一个文件夹  
        if os.path.isdir(item_path):  
            # 检查文件夹名称是否包含目标字符串  
            if search_string in item:
                # 生成新的文件夹名称（在原名称后添加后缀）  
                new_name = f"{suffix}{item.rsplit(search_string, 1)[0]}{search_string}"  
                # 如果新名称与原名称相同（例如，当search_string是文件夹名称的末尾部分时），则避免重命名  
                if new_name != item:  
                    # 构建新名称的完整路径  
                    new_path = os.path.join(target_directory, new_name)  
                      
                    # 检查新名称是否已存在，如果存在，则避免覆盖（可选步骤，但推荐执行）  
                    if not os.path.exists(new_path):  
                        # 执行重命名操作  
                        os.rename(item_path, new_path)  
                        print(f"Renamed '{item}' to '{new_name}'")  
                    else:  
                        print(f"Cannot rename '{item}' to '{new_name}' because '{new_name}' already exists.")  
  
# 示例用法  
target_directory = './target_directory'  # 替换为您的目标目录路径

# 打开文件，使用'with'语句可以确保文件在使用后被正确关闭  
with open('目标.txt', 'r', encoding='utf-8') as file:  
    # 遍历文件的每一行  
    for line in file:  
        # 去除每行末尾的换行符（如果有的话）  
        line = line.rstrip()  
        # 打印当前行的内容  
        # print(line)
        rename_folders_containing_string(target_directory, line)