import urllib.request  # the lib that handles the url stuff

for line in urllib.request.urlopen('https://www.ndbc.noaa.gov/view_text_file.php?filename=46085h2020.txt.gz&dir=data/historical/stdmet/'):
    print(line.decode('utf-8'))
