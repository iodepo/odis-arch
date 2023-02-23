import advertools as adv
import requests, sys, os
import yaml, yaql
from urllib.request import urlopen
import logging
import argparse
from typing import Tuple
import pandas as pd

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
            name = s["name"]
            pname = s["propername"]

            r, res = check_sitemapv2(smurl, stype, name)

            data = { 'name': name,  'propername': pname, 'code': r, 'description': res, 'url': smurl, 'type': stype}
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
