# nscompare

This functions similarly to **_nslookup_**, except the goal is to compare DNS responses between two queried servers rather than print the response from one queried server. It accepts names, in addition to IP addresses, for the target servers. This is useful for confirming parity during DNS migrations.

_**Input**_: <br>
_server1 dns.google_<br>
_server2 one.one.one.one_<br>
_set type=a_<br>
_google.com_<br><br>
_**Output**_: <br>
_Do not match_<br>
_Response from dns.google: ['142.251.116.100', '142.251.116.101', '142.251.116.102', '142.251.116.113', '142.251.116.138', '142.251.116.139']_ <br>
_Response from one.one.one.one: ['142.250.114.100', '142.250.114.101', '142.250.114.102', '142.250.114.113', '142.250.114.138', '142.250.114.139']_ <br>
<br><br>
_**Input**_: <br>
_server1 8.8.8.8_<br>
_server2 1.1.1.1_<br>
_set type=a_<br>
_nytimes.com_<br>
<br>
_**Output**_:<br>
_Match_
