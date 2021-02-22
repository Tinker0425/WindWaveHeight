import numpy as np
data = np.loadtxt("https://www.ndbc.noaa.gov/view_text_file.php?filename=46085h2020.txt.gz&dir=data/historical/stdmet/", comments='#',skiprows=2)
print(data)

