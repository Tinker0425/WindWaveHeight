import urllib.request  # the lib that handles the url stuff
c = ''

for line in urllib.request.urlopen('https://www.ndbc.noaa.gov/view_text_file.php?filename=46085h2020.txt.gz&dir=data/historical/stdmet/'):
    a = line.decode('utf-8')
    if not '9999' in a:
        b = a[21:35]
    c = c + b
    #wspd = b[21:21+4]
    #listWords = a.split("\t")
    #print(listWords)
    print(c)    
    #print(wspd)
#print(a[0:5])
#print(b)
