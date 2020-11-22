# author: Kangyu (Mark) Wang
# date: 2020-11-22

"""This script read our data from online source and save them as csv file.
Usage: docopt.py --source=<source> --destination=<destination>

Options:
--source=<source>               Takes the unquoted url of the online source of data (this is a required option)
--destination=<destination>    Takes the unquoted relative path of destination csv file (this is a required option)
"""

from docopt import docopt
import requests

opt = docopt(__doc__)


def main(opt):
    source = opt["--source"]
    destination = opt["--destination"]

    req = requests.get(source)
    url_content = req.content
    csv_file = open(destination, "wb")

    csv_file.write(url_content)
    csv_file.close()


if __name__ == "__main__":
    main(opt)