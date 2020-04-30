import wget
import re
import os

regex = r"^!\[(img)\]\(.*?\)"
pic_path = r"C:\Users\sunguopeng\AppData\Roaming\Typora\typora-user-images"

with open('j1939_obd.md', 'r',encoding='utf-8') as md,  open("out.md", "w",encoding='utf-8') as output:
    for line in md:
        res = re.search(r"^!\[(img)\]\((.*?)\)", str(line), re.DOTALL)
        if res:
            img, url = res.groups()
            urls = url.split('/')
            img_name = urls[len(urls)-1]
            local_file_name = os.path.join(pic_path, img_name)
            line = r"![{0}]({1})".format(img_name, local_file_name) + r'\r\n'
            wget.download(url, local_file_name)
        output.write(line)
