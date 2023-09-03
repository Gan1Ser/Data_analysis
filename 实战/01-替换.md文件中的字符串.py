import re
import os
# 读取.md文件并替换链接
def replace_links(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    pattern = r"(https://blog\.gan1ser\.top)(/.*)" #分组吧，简单些
    replaced_content = re.sub(pattern, r'https://pic.gan1ser.top\2', content)

    # 将替换后的内容写回文件
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(replaced_content)

# 替换指定目录下的所有.md文件
def replace_links_in_directory(directory):
    for file in os.listdir(directory):
        if file.endswith(".md"):
            file_path = os.path.join(directory, file)
            replace_links(file_path)

# 使用示例
replace_links_in_directory('path')