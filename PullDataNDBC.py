import urllib.request  # the lib that handles the url stuff

wspd_str = ''
wspd_float = []
gust_str = ''
wave_str = ''

k = 0

for line in urllib.request.urlopen('https://www.ndbc.noaa.gov/view_text_file.php?filename=46085h2020.txt.gz&dir=data/historical/stdmet/'):
    if k > 1 & k < 5:
        a = line.decode('utf-8')
        wspd_str = a[21:25]
        wspd_float.append(float(a[21:25]))
        gust_str = a[26:31]   
        wave_str = a[31:35]
        print(wspd_float)
    k += 1

#wspd_float = wspd_float.*10
#gust_str = a[26:31]   
#wave_str = a[31:35]   

#print(wspd_float)
