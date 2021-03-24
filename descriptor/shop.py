import json
import random
import string
from collections import Counter
from enum import Enum
# import pandas
from functools import reduce

from attrdict import AttrDict
from selenium import webdriver
from time import sleep
import os
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from pytz import timezone
import shutil
import tempfile
import unittest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from re import findall
import requests
import os
# import pandas as pd
import dictdiffer
# jquery_url = "http://code.jquery.com/jquery-1.11.2.min.js"
# driver = webdriver.Chrome("/Users/dmytro.maksymov/PycharmProjects/self/regular/drivers/chromedriver")
# # driver.get("https://www.seleniumeasy.com/test/drag-and-drop-demo.html")
# driver.get("http://the-internet.herokuapp.com/drag_and_drop")
# driver.set_script_timeout(30)
from selenium.webdriver.remote.file_detector import LocalFileDetector

# desiredCapabilities = {
#     "browserName": "firefox",
#     "version": "80.0",
#     "enableVNC": True,
#     "enableVideo": False,
#     "screenResolution": "1920x1080x24"
# }
#
# fireOptionsRemote = webdriver.FirefoxOptions()
# fireOptionsRemote.add_argument('--window-size=1920,1080')
# fireOptionsRemote.add_argument("--disable-session-crashed-bubble")
# driver = webdriver.Remote(options=fireOptionsRemote, command_executor='http://localhost'
#                                                                       ':4444/wd/hub',
#                           desired_capabilities=desiredCapabilities)
# driver.set_window_size(1920, 1080)
# driver.get('https://gofile.io/uploadFiles')
# _input = driver.find_element_by_css_selector("input[type='file']")
# # driver.execute_script("var x=  document.createElement('INPUT');x.setAttribute('type', 'file'); x.setAttribute('onchange','this.form.submit()');x.setAttribute('hidden', 'true'); arguments[0].appendChild(x);",_input)
# # driver.execute_script("arguments[0].style.display = 'block';", _input)
# # driver.file_detector = LocalFileDetector()
# a = f"/Users/dmytro.maksymov/PycharmProjects/self/files/photo/basketball.jpeg"
# b = "/Users/dmytro.maksymov/PycharmProjects/self/files/photo/football.jpeg"
#
# _input.send_keys(a + "\n " + b)

# _input.send_keys(a)

# driver.quit()
# driver.close()

# with open("/Users/dmytro.maksymov/PycharmProjects/self/regular/tests/drag_and_drop_helper.js") as js_file:
#     line = js_file.readline()
#     script = ''
#     while line:
#         script += line
#         line = js_file.readline()
#
# driver.execute_script(script + "$('#column-a').simulateDragDrop({ dropTarget: '#column-b'});")
# sleep(5)

# from csv import writer
#
#
# def append_list_as_row(file_name, list_of_elem):
#     # Open file in append mode
#     with open(file_name, 'a', newline='') as write_obj:
#         # Create a writer object from csv module
#         csv_writer = writer(write_obj)
#         # Add contents of list as last row in the csv file
#         csv_writer.writerow(list_of_elem)

# file_name = 'test.csv'
# columns = ['ID', 'GUID', 'Title', 'CallSign', 'Visible', 'Provider']
# my_csv = pd.read_csv('/Users/dmytro.maksymov/PycharmProjects/self/files/test.csv', names=columns)
# my_csv['Title'] = my_csv['Title'].replace(['test'], 'PRIMHD')
# my_csv['ID'] = my_csv['ID'].replace([1030], 1228)
# my_csv['GUID'] = my_csv['GUID'].replace(['test_guid'], '9c785d0afe0045a29e20489e6bd66347')
# my_csv.to_csv('/Users/dmytro.maksymov/PycharmProjects/self/files/test.csv', index=False)
# if os.path.getsize("/Users/dmytro.maksymov/PycharmProjects/self/files/test.csv") == 0:
#     print('YES')
# else:
#     print(os.stat("/Users/dmytro.maksymov/PycharmProjects/self/files/test.csv").st_size)
#     print('NO')

# lst_id = [[111, 'test', 'test', 'test', 'test'], [118, 'test', 'test', 'test', 'test']]
# for i in lst_id:
#     row_contents = i
#     append_list_as_row('/Users/dmytro.maksymov/PycharmProjects/self/regular/tests/csv/subpacks.csv', i)
# g = 3
# while g != 0:
#
#     f = open('/Users/dmytro.maksymov/PycharmProjects/self/regular/tests/csv/subpacks.csv', 'r+')
#     lines = f.readlines()
#     lines.pop()
#     f = open('/Users/dmytro.maksymov/PycharmProjects/self/regular/tests/csv/subpacks.csv', 'w+')
#     f.writelines(lines)
#     g -= 1

# with open('/Users/dmytro.maksymov/PycharmProjects/self/regular/tests/csv/screen2.json') as json_file2:
#     data2 = json.load(json_file2)
#     data2['test_key'] = 'tatatata'
#
# with open('/Users/dmytro.maksymov/PycharmProjects/self/regular/tests/csv/screen2.json', 'w') as json_file2:
#     # del data2['ribbon_references']
#     json.dump(data2, json_file2)
#
#
# from collections import Counter
#
# lst1 = ['One', 'Two', 'Three', 'Four']
# lst2 = ['One', 'Two']
#
# c1 = Counter(lst1)
# c2 = Counter(lst2)
# diff = list((c1 - c2).elements())
#
# print(diff)

# lst = ['a', 'b', 'c', 'd']
# for i, x in enumerate(lst):
#     print(i)
#     print(x)

# lst = ['a', 'b', 'c', 'd']
# print(lst[:3])

# a = '/Users/dmytro.maksymov/PycharmProjects/self/regular/tests/csv/screen.json'
# print(f"{a}\ntext")

# class A:
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return f"{self.name} Dima"
#
#     def print_hello(self):
#         print('Hello')
#
#
# a = A('Test')
# print(a)
# lst_2 = []
# lst = ['1', '3', '2', '1', '3']
# for i in lst:
#     if i == '3':
#         lst_2.append(i)
#         break
# print(lst_2)

# chars = string.ascii_uppercase + string.digits
# a = ''.join(random.choice(chars) for _ in range(6))
# print(a)
# var = (datetime.now() + timedelta(days=-10)).strftime('%Y-%m-%d')
# print(var)

# with open(f"/Users/dmytro.maksymov/PycharmProjects/self/files/ribbon.json") as json_file:
#     jsn_dict = json.load(json_file)['data']
# var = filter(lambda x: x['id'] == 10638864, jsn_dict)
# print(list(var))

# class Color(Enum):
#     my_profile = "cabinet"
#     notifications = "notifications"
#     about_us = "aboutUs"
#     support = "support"
#     companies = "companies"
#     language = "language"
#     logout = "logout"
#
# var = Color.my_profile.value
# print(var)


# class Person(object):
#
#     age = 23
#     name = "Dima"
#
#
# person = Person()
#
# print('The sex is:', getattr(person, 'sex', 'Male'))

# class Name:
#
#     def __init__(self, first="", second=""):
#         self.first = first
#         self.second = second
#
#
# class A:
#     test_attr = 'Hello!'
#
#     def __init__(self, name=None, age=int, city=None, tag=None):
#         if name is None:
#             name = [Name()]
#         if city is None:
#             city = []
#         self.name = name
#         self.age = age
#         self.city = city
#         self.tag = tag
#
#
# class B(A):
#
#     def __init__(self, name=None, age=int, city=None, tag=None):
#         if name is None:
#             name = [Name()]
#         if city is None:
#             city = []
#         self.name = name
#         self.age = age
#         self.city = city
#         self.tag = tag
#
#
# a = A(name=Name(first='a', second='c').__dict__)
# b = B(name=Name(first='a', second='b').__dict__)
# print(b.test_attr)
#
# diff = [i for i in list(dictdiffer.diff(a.__dict__, b.__dict__))]
# print(diff)
# try:
#     assert a.__dict__ == b.__dict__
# except AssertionError as e:
#     raise AssertionError(f"info:\n{diff}")

# var = '1 2 3 4'
# mas = list(map(int, input().split()))
# print(list(map(int, var.split())))
# print(f"{mas}*")

# from PIL import Image
# from PIL import ImageChops
# import math, operator
#
#
# def rmsdiff(im1, im2):
#     "Calculate the root-mean-square difference between two images"
#
#     h = ImageChops.difference(im1, im2).histogram()
#
#     # calculate rms
#     return math.sqrt(reduce(operator.add,
#         map(lambda h, i: h*(i**2), h, range(256))
#     ) / (float(im1.size[0]) * im1.size[1]))
# # def equal(im1, im2):
# #     return ImageChops.difference(im1, im2).getbbox() is None
#
# img1 = Image.open('/Users/dmytro.maksymov/Desktop/thumbnail_img.png')
# img2 = Image.open('/Users/dmytro.maksymov/Desktop/remote_thumbnail_img.png')
# print(rmsdiff(img1, img2))

# for i in range(1, 3):
#     print(i)
#
# a = [1, 2, 3, 4]
# print(a[1:3])

# i = 5
# lst = [1, 2]
# assert i in lst

dd = {
    "by": 'ID', "value": 'hello'
}

a = 1,
print(type(a))


