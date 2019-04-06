import csv
import os

c = csv.writer(open('data.csv', 'w'))

c.writerow(['image_url'])
dir_list = ['ori_type_1', 'ori_type_2', 'ori_type_3', 'codes/images/cnn_adv_all'
            ,'codes/images/ocr_adv_all','codes/images/ocr_adv_ori']
for dir in dir_list:
    for i in os.listdir(dir):
        c.writerow(['https://wscjxky.github.io/images/%s/%s'%(dir, i)])
