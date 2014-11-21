drnTracker
==========

Log historical downrightnow stats to see how bad yahoo mail really is

downrightnow.py is run hourly using cron (checks Hotmail. Gmail, and Yahoo! mail)

data is stored in the drnDict.p pickle file

stats.py displays summarized statistics for each provider

Sample output:
    
    HOTMAIL: 75 records from 2014-11-18 to 2014-11-21
    Likely Service Disruption         0 ( 0.00%)
    Possible Service Trouble          2 ( 2.67%)
    Recent Signs of Service Trouble   1 ( 1.33%)
    Up                               72 (96.00%)

    YAHOOMAIL: 75 records from 2014-11-18 to 2014-11-21
    Likely Service Disruption        26 (34.67%)
    Possible Service Trouble         10 (13.33%)
    Recent Signs of Service Trouble   2 ( 2.67%)
    Up                               37 (49.33%)

    GMAIL: 75 records from 2014-11-18 to 2014-11-21
    Likely Service Disruption         2 ( 2.67%)
    Possible Service Trouble          4 ( 5.33%)
    Recent Signs of Service Trouble   0 ( 0.00%)
    Up                               69 (92.00%)``
