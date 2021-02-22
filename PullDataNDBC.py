import numpy as np
Buoy_List = ["46085","46084","46083","46082","46205","46145"]
Year_List = ["2007","2008","2009","2010","2011","2012","2014","2015","2016","2017","2018","2019","2020"]
# No 2013 in 46085
for i in Buoy_List:
    for j in Year_List:
        data = np.loadtxt("https://www.ndbc.noaa.gov/view_text_file.php?filename="+i+"h"+j+".txt.gz&dir=data/historical/stdmet/", comments='#',skiprows=2)
        print(i + ' ' + j)
        # wspd = data[:,6]
        # gst = data[:,7]
        # wvht = data[:,8]
        

