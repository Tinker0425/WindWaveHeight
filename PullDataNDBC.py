import urllib.request  # the lib that handles the url stuff
wspd_str = ''
wave_str = ''
for line in urllib.request.urlopen('https://www.ndbc.noaa.gov/view_text_file.php?filename=46085h2020.txt.gz&dir=data/historical/stdmet/'):
    a = line.decode('utf-8')
    wspd_str = wspd_str + a[21:25]
    gust_str = a[26:31]   
    wave_str = a[31:35]
wspd_float = float(wspd_str[9:11])
#gust_str = a[26:31]   
#wave_str = a[31:35]   

print(wspd_float)
