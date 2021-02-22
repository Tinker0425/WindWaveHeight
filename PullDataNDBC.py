import urllib.request  # the lib that handles the url stuff
for line in urllib.request.urlopen('https://www.ndbc.noaa.gov/view_text_file.php?filename=46085h2020.txt.gz&dir=data/historical/stdmet/'):
    a = line.decode('utf-8')
    wspd = a[21:26]
    gust = a[26:31]   
    wave = a[31:35]
    
  
