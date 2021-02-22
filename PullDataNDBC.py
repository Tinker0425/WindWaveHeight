import urllib.request  # the lib that handles the url stuff

for line in urllib.request.urlopen('https://www.ndbc.noaa.gov/view_text_file.php?filename=46085h2020.txt.gz&dir=data/historical/stdmet/'):
    a = line.decode('utf-8')
    b = a[21:35]
    #listWords = a.split("\t")
    #print(listWords)
    print(b)
#print(a[0:5])
