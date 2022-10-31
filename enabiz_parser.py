# -*- coding: utf-8 -*-
from codecs import utf_16_be_decode
from xml.etree.ElementTree import tostring
import requests

from lxml import html
from lxml.etree import XPath

request_url = 'https://rehber.enabiz.gov.tr/Home/PaketDetay'
s = requests.Session()
# packet_code = input("Please enter paket code")
# payload = {
#     'key': 'prod:'+packet_code
# }
payload = {
    'key': 'prod:276'
}
response = s.post(request_url,  data=payload)

print(response.status_code)


tree = html.fromstring(response.text)
print(tree)


code_xpath = XPath('//code')

print(code_xpath(tree)[0])
element_string = tostring(
    code_xpath(tree)[0], encoding="unicode")
print(element_string)


# all_rows_xpath = XPath('//tbody/tr')
# player_team_xpath = XPath('td/text()')

# row_list = tree.xpath('//tbody/tr')
# all_rows = all_rows_xpath(row_list[0])

# for item in all_rows:

#     print(item)
#     res = player_team_xpath(item)
#     print(player_team_xpath(item))
# td_list = player_team_xpath(item)

# print(row_list)
# print(player_team_xpath(row_list[0]))
# print(player_team_xpath(row_list))
