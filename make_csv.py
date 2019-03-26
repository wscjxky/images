import csv
import os

c=csv.writer(open('data.csv','w'))

c.writerow(['image_url'])

for i in os.listdir('adv'):
    c.writerow(['https://wscjxky.github.io/images/adv/'+i])