import os  

# 示例使用  
#删除已有文件再进行重命名
os.remove('./first_file.txt')
os.rename('./second_file.txt','./first_file.txt') 

#文件名对调
os.rename('./first_file.txt', './swap_file.txt')
os.rename('./second_file.txt','./first_file.txt') 
os.rename('./swap_file.txt',  './second_file.txt')