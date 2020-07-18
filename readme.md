# Social Scraper

## Summary

Project aims to help people to get some public information from social media. 

### Release Notes

#### 1.0

It supports Instagram. It requires a file that contains usernames to scrape at each line. It produces a tsv (tab seperated value) file for that usernames. Output file contains:

* Username

* Biography

* Business Category Name

* Follow Count

* Follower Count

* Last 12 Photos

## Installation

**Docker must be installed on your operating system.**

* Clone project.

* Open a terminal/command line in the root folder of project.

* Type: ```docker build --tag socialscraper:1.0 .```

## Run

Prepare a input.txt file that contains instagram username you would like to fetch informations each line.

### Windows

* For powershell: ```docker run -it --rm -v ${PWD}:/app/ socialscraper:1.0 python /app/main.py --input-file=input.txt --output-file=output.tsv```

* For command line: ```docker run -it --rm -v %cd%:/app/ socialscraper:1.0 python /app/main.py --input-file=input.txt --output-file=output.tsv```

### Unix

* ```docker run -it --rm -v $(pwd):/app/ socialscraper:1.0 python /app/main.py --input-file=input.txt --output-file=output.tsv```