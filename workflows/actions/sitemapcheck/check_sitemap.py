import advertools as adv
import requests, sys, os
import yaml
from urllib.request import urlopen

# sources = "https://raw.githubusercontent.com/iodepo/odis-arch/schema-dev-df/config/sources.yaml"
sources = "/home/fils/src/Projects/gleaner.io/scheduler/dagster/dagster-docker/src/implnet-eco/gleanerconfig.yaml"

def check_sitemap(target: str) -> int:
    # f = urlopen(sources)
    f = open(sources)
    fr = f.read()
    try:
        cfg = yaml.safe_load(fr)
        # cfg = yaml.load(file, Loader=yaml.FullLoader)
        # print(cfg)
        for x in cfg["sources"]:
            if x["name"] == target:
                smurl = x["url"]
                stype = x["sourcetype"]
                print(stype, " : ", smurl)
                if stype == "sitegraph":
                    x = requests.head(smurl)
                    # print(x.headers)
                    if x.status_code == 404:  # could check for 200 or 303?
                        print("Sitegrap URL is 404")
                        return 1 # sys.exit(os.EX_SOFTWARE)
                    else:
                        print("Sitegraph URL is ", x.status_code)
                        return 0 # sys.exit(os.EX_OK)
                else:
                    r = requests.get(smurl)
                    if r.status_code == 404:
                        print("Sitemap URL is 404")
                        return 1 # sys.exit(os.EX_SOFTWARE)
                    else:
                        try:
                            iow_sitemap = adv.sitemap_to_df(smurl)
                            usm = iow_sitemap.sitemap.unique()
                            uloc = iow_sitemap["loc"].unique()
                            print("{} unique sitemap XML file(s) pointing to {} unique resource(s).".format(len(usm), len(uloc)))
                            return 0 # sys.exit(os.EX_OK)
                        except:
                            print("error reading sitemap XML")
                            return 1
        # looped and didn't find target
        print("Target not found: returning 1")
        return 1
    except yaml.YAMLError as exc:
        print(exc)
        return 1 #  sys.exit(os.EX_SOFTWARE)


r = check_sitemap("r2r")
print(r)

