# cpverify
cPanel license verification command line tool with basic IP validation.
Displays the output of the online check tool along with a direct link to the results.


```
[root]# cpverify 208.74.121.151
License data for IP address: 208.74.121.151
'46159957', '208.74.121.151', 'CPANEL-SERVERS-INTERNAL', 'cPanel, L.L.C.', '2018-11-07 12:17:41', 'active'
'45806421', '208.74.121.151', '15-DAY-TEST', 'cPanel, L.L.C.', '2018-10-10 14:42:19', 'expired on 2018-10-25 14:45:01'

https://verify.cpanel.net/app/verify?ip=208.74.121.151
```
