import advertools as adv
import requests, sys, os
import yaml, yaql
from datetime import datetime
from urllib.request import urlopen
import urllib.request
import logging
import argparse
from typing import Tuple
import pandas as pd
import numpy as np
import csv
import re
import advertools
from io import StringIO

# TODO   explore csv for the web and RML

def check_sitemapv2(smurl, stype, name: str) -> Tuple[int, str]:
    logging.getLogger('requests').setLevel(logging.ERROR)  # 'NOTSET', 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
    logging.getLogger('advertools').setLevel(logging.ERROR)

    if stype == "sitegraph":
        x = requests.head(smurl)
        if x.status_code == 404:  # could check for 200 or 303?
            res = str("ERROR {} : {} Sitegrap URL is 404".format(name, smurl))
            return 1, res  # sys.exit(os.EX_SOFTWARE)
        else:
            res = str("{} \t {} Sitegraph URL code is {} ".format(name, smurl, x.status_code))
            return 0, res  # sys.exit(os.EX_OK)
    else:
        try:
            r = requests.get(smurl)
        except:
            res = str("ERROR making request, no further information at this time")
            return 1, res
        if r.status_code == 404:
            res = str("ERROR {} : {} Sitemap URL is 404".format(name, smurl))
            return 1, res  # sys.exit(os.EX_SOFTWARE)
        else:
            try:
                iow_sitemap = adv.sitemap_to_df(smurl)
                usm = iow_sitemap.sitemap.unique()
                uloc = iow_sitemap["loc"].unique()
                res = str("{} : {} VALID {}  with {} sitemap URL(s)".format(len(uloc), name, smurl, len(usm)))
                return 0, res  # sys.exit(os.EX_OK)
            except:
                res = str("ERROR {} : {} reading sitemap XML".format(name, smurl))
                return 1, res

# TODO can I look for the <script type=application/ld+json>?
# TODO try beautiful soup for this testing
def sample_sitemap(smurl):
    print("sample the sitemap and test")

    iow_sitemap = adv.sitemap_to_df(smurl)
    usm = iow_sitemap.sitemap.unique()
    uloc = iow_sitemap["loc"].unique()
    print("{} unique sitemap XML file(s) pointing to {} unique resource(s).".format(len(usm), len(uloc)))

    # Break down all the URL into theor path parts
    urldf = adv.url_to_df(list(iow_sitemap['loc']))

    # sample the previously generated url data frame
    sample_size = 5
    sample_df = urldf.groupby("dir_1").sample(n=sample_size, random_state=1, replace=True)

    ul = sample_df["url"]

    for item in ul:
        # user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
        # headers={'User-Agent':user_agent,}

        headers= {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                               'AppleWebKit/537.11 (KHTML, like Gecko) '
                               'Chrome/23.0.1271.64 Safari/537.11',
                 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                 'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                 'Accept-Encoding': 'none',
                 'Accept-Language': 'en-US,en;q=0.8',
                 'Connection': 'keep-alive'}

        try:
            # x = requests.get(item)
            # code = x.status_code
            request=urllib.request.Request(url=item, headers=headers) #The assembled request
            with urllib.request.urlopen(request) as response:
                info = response.info()
                dtype = info.get_content_type()    # -> text/html
             # headers = x.headers()
             #    print("URL: {} \ninfo : {}\n --".format(item, info))
                # read n bytes until `buff` includes "</head>"
                # data = b''
                # i = 1
                # while True:
                #     buff = response.read(1024)
                #     data += buff
                #     if b'</head>' in buff:
                #         break
                #     elif buff == b'':
                #         raise AttributeError('Not head-tag found.')
                #     i += 1


            # head = str(data)

            # Search for a specific tag in the head
            # if re.search('application/ld+json', head):
            #     print('The json-ld tag was found in the head.')
            # else:
            #     print('The json-ld tag was not found in the head.')

            print("URL: {} ".format(item))
        except Exception as e:
            # code = x.status_code
            # dtype = info.get_content_type()
            print("Exception on: {} \nerrors : {}\n --".format(item, str(e)))

def main():
    # Read the command line arguments
    data_source = None
    # args = sys.argv[1:]
    # sources = args[0]

    # Initialize args  parser
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--source", help="Source: URL or file")
    parser.add_argument("-n", "--name", help="Optional name of single source, by name, to check")
    parser.add_argument("-f", "--file", help="Optional name of CSV file to save results to")

    args = parser.parse_args()

    sources = args.source
    name = args.name
    file = args.file

    if "://" in sources:
        # If the input is a URL, open it using urllib
        f = urlopen(sources)
        data_source = yaml.safe_load(f.read())
    else:
        # If the input is a file, open it
        data_source = yaml.safe_load(open(sources, 'r'))

    engine = yaql.factory.YaqlFactory().create()
    expression = engine('$.sources.name')
    order = expression.evaluate(data=data_source)

    if name is None:
        rl = []
        for s in data_source["sources"]:
            smurl = s["url"]
            stype = s["sourcetype"]

            # set name with date string
            today = datetime.now()
            date_string = today.strftime('%Y-%m-%d')
            name = date_string+s["name"]

            r, res = check_sitemapv2(smurl, stype, name)

            if r == 0 and stype == "sitemap":
                sample_sitemap(smurl)

            data = { 'name': name, 'code': r, 'description': res, 'url': smurl, 'type': stype}
            rl.append(data)

        # leverage pandas to convert to csv
        df = pd.DataFrame.from_dict(rl)

        if file is not None:
            df.to_csv(file, index=False)
        else:
            csv_data = df.to_csv(index=False)
            print(csv_data)

    else:
        rl = []
        for s in data_source["sources"]:
            if name == s["name"]:
            # if ("r2r" == s["name"]) or ("magic" == s["name"]):  // testing

                smurl = s["url"]
                stype = s["sourcetype"]
                name = s["name"]

                r, res = check_sitemapv2(smurl, stype, name)

                data = { 'name': name, 'code': r, 'description': res, 'url': smurl, 'type': stype}
                rl.append(data)

        # for row in rl:
        #     # formatted_string = f"Name: {row['name']} code: {row['code']} description: {row['description']} type: {row['type']} "
        #     print(row)

        # leverage pandas to convert to csv
        df = pd.DataFrame.from_dict(rl)

        if file is not None:
            df.to_csv(file, index=False)
        else:
            csv_data = df.to_csv(index=False)
            print(csv_data)

if __name__ == '__main__':
    main()
