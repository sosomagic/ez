#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pandas as pd
import logging

import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')


logger = logging.getLogger('filter')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('filter.log')
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)

file = r'/tmp/all.xls'
df = pd.read_excel(file, encoding='utf-8')

file = r'/tmp/has_id.xls'
df_has_id = pd.read_excel(file, encoding='utf-8')
# df = df[df['身份证状态'] != '身份证未上传']
# indexNames = df[ df['ID_STATUS'] == '身份证未上传' ].index
 
# # Delete these row indexes from dataFrame
# df_no_id = df.drop(indexNames , inplace=false)

phone_dict = {}
addr_dict = {}

dup_phone_set = set()
dup_addr_set = set()

df_sending = df_has_id.drop_duplicates(subset=u'收件人电话', keep='first', inplace=False).drop_duplicates(subset=u'收件人地址', keep='first', inplace=False)
df_no_sending = pd.concat([df,df_sending]).drop_duplicates(keep=False)

# df1.to_excel("sending.xlsx")
# df2.to_excel("not_sending.xlsx")

writer = pd.ExcelWriter("/tmp/sending.xlsx", engine='xlsxwriter')
df_sending.to_excel(writer, sheet_name='Sheet1')
workbook  = writer.book
worksheet = writer.sheets['Sheet1']
format1 = workbook.add_format({'num_format': '0'})
worksheet.set_column('B:B', 18, format1)
worksheet.set_column('M:M', 18, format1)
writer.save()

writer = pd.ExcelWriter("/tmp/not_sending.xlsx", engine='xlsxwriter')
df_no_sending.to_excel(writer, sheet_name='Sheet1')
workbook  = writer.book
worksheet = writer.sheets['Sheet1']
format1 = workbook.add_format({'num_format': '0'})
worksheet.set_column('B:B', 18, format1)
worksheet.set_column('M:M', 18, format1)
writer.save()


# print ("=========== DUPLICATE PHONE NUMBERS ===========")
# for index, row in df.iterrows():
#   order_numer = row[u'订单号']
#   recipient_name = row[u'收件人姓名']
#   recipient_phone = row[u'收件人电话']
#   recipient_addr = row[u'收件人地址']
#   # print ("%s: %s: %s: %s" % (order_numer, recipient_name, recipient_phone, recipient_addr))
#   logger.info("%s: %s: %s: %s" % (order_numer, recipient_name, recipient_phone, recipient_addr))
  
#   if recipient_phone in phone_dict:
#     dup_phone_set.add(recipient_phone)
#     # print ("!!![DUP] order_numer %s is duplicated with order number %s on recipient's phone: %s" % (order_numer, phone_dict[recipient_phone], recipient_phone))
#   else:
#     phone_dict[recipient_phone] = order_numer

# for phone in dup_phone_set:
#   print(phone)

# print ("=========== DUPLICATE ADDRESSES ===========")
# for index, row in df.iterrows():
#   order_numer = row[u'订单号']
#   recipient_name = row[u'收件人姓名']
#   recipient_phone = row[u'收件人电话']
#   recipient_addr = row[u'收件人地址']
#   if recipient_addr in addr_dict:
#     dup_addr_set.add(recipient_addr)
#     # print ("!!![DUP] order_numer %s is duplicated with order number %s on recipient's address: %s" % (order_numer, addr_dict[recipient_addr], recipient_addr))
#   else:
#     addr_dict[recipient_addr] = order_numer

# for addr in dup_addr_set:
#   print(addr)
