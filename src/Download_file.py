# author: Kangyu (Mark) Wang
# date: 2020-11-22

"""This script reads our data from online source and save them as csv file.
Usage: Download_file.py --source=<source> --destination=<destination>

Options:
--source=<source>               Takes the unquoted url of the online source of data (this is a required option)
--destination=<destination>    Takes the unquoted relative path of destination csv file (this is a required option)
"""

from docopt import docopt
import requests
from os import path
import sys

opt = docopt(__doc__)


def main(opt):
    source = opt["--source"]
    destination = opt["--destination"]

    if path.exists(destination) == False:
        raise NameError("The path to destination file does not exist.")

    try:
        req = requests.get(source)
    except:
        print(
            "Failed to connect to the online source file. Please check whether it exists."
        )
        sys.exit(1)

    # req = requests.get(source)
    url_content = req.content
    csv_file = open(destination, "wb")
    csv_file.write(url_content)
    csv_file.close()


if __name__ == "__main__":
    main(opt)