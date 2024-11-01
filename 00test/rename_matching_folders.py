import os  
  
def read_folder_names_from_file(file_path):  
    """从文件中读取文件夹名字列表"""  
    with open(file_path, 'r', encoding='utf-8') as file:  
        folder_names = [line.strip() for line in file.readlines()]  
    return folder_names  
  
def rename_matching_folders(target_dir, folder_names):  
    """重命名指定目录下与目标文件夹名相同的文件夹"""  
    for item in os.listdir(target_dir):  
        item_path = os.path.join(target_dir, item)  
        if os.path.isdir(item_path) and item in folder_names:
        # if os.path.isdir(item_path) and folder_names in item: 
            # 生成新的文件夹名（这里简单地在原名后加"_renamed"，你可以根据需要修改）  
            new_name = f"1y_{item}"
            new_item_path = os.path.join(target_dir, new_name)  
              
            # 检查新文件夹名是否已存在，如果存在则继续修改直到不冲突（这里简化处理，只加后缀）  
            counter = 1  
            while os.path.exists(new_item_path):  
                new_name = f"{item}_renamed_{counter}"  
                new_item_path = os.path.join(target_dir, new_name)  
                counter += 1  
              
            # 重命名文件夹  
            os.rename(item_path, new_item_path)  
            print(f"Renamed folder '{item}' to '{new_name}' in {target_dir}")  
  
# 示例用法  
folder_names_file = '目标.txt'  # 目标文件夹名字列表的文件路径  
target_directory = './target_directory'  # 要搜索并重命名的目标目录路径  

# 读取文件夹名字列表  
folder_names = read_folder_names_from_file(folder_names_file)  
  
# 重命名匹配的文件夹  
rename_matching_folders(target_directory, folder_names)