# -*- coding: utf-8 -*-
# pylint: disable=C0103
# pylint: disable=C0111
# pylint: disable=C0301
# pylint: disable=W0311

##  All credit here due to si9int  ##
## https://github.com/si9int/cc.py ##

import requests, json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('domain', help = 'domain which will be crawled for', type = str)

args = parser.parse_args()

indexes = [
    'CC-MAIN-2018-17',
    'CC-MAIN-2018-13',
    'CC-MAIN-2018-09',
    'CC-MAIN-2018-05',
    'CC-MAIN-2017-51',
    'CC-MAIN-2017-47',
    'CC-MAIN-2017-43',
    'CC-MAIN-2017-39',
    'CC-MAIN-2017-34',
    'CC-MAIN-2017-30',
    'CC-MAIN-2017-26',
    'CC-MAIN-2017-22',
    'CC-MAIN-2017-17',
    'CC-MAIN-2017-13',
    'CC-MAIN-2017-09',
    'CC-MAIN-2017-04'
]

output, links = ([] for i in range(2))
result = open('./' + args.domain + '.txt', 'w')


for index in indexes:
    print('[-] Getting: ' + index)
    data = requests.get('http://index.commoncrawl.org/' + index + '-index?url=*.' + args.domain + '&output=json')
    data = data.text.split('\n')[:-1]
    output.append(data)

Length_Of_Output = str(output).count(",") - str(output).count("[]") + 1

print "[+] Raw Length of Output is: " + str(Length_Of_Output)

for i, entry in enumerate(output):
    for link in entry:

        link = json.loads(link)['url']

        if link not in links:
            links.append(link + '\n')

    if i % 3 == 0 and i != 0:
        print "[*] We are " + str((float(i)/len(output))*100) + "%% done."


print "[+] Raw Result Link Count is: " + str(len(links))
print "[+] Deduplicated Result Link Count is: " + str(len(set(links)))
print '[+] Writing URLS to file'

for link in set(links):
    result.write(link)

print('[!] Done, file written: ' + args.domain + '.txt')





