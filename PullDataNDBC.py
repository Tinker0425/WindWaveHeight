import urllib.request  # the lib that handles the url stuff

# Create a script that reads in the NDBC Buoy data and stores it
# Then a second to analyze data

# This is what I want because it creates an output array to use:
import numpy as np
data = np.loadtxt("https://www.ndbc.noaa.gov/view_text_file.php?filename=46085h2020.txt.gz&dir=data/historical/stdmet/", comments='#',skiprows=2)
print(data)


wspd_str = ''
wspd_float = []
gust_str = ''
wave_str = ''

k = 0

for line in urllib.request.urlopen('https://www.ndbc.noaa.gov/view_text_file.php?filename=46085h2020.txt.gz&dir=data/historical/stdmet/'):
    while 1 < k < 5 :
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

print(wspd_float)
