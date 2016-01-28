"""
the purpose of the assignment is to create our 
own class that willinherit from dict, so out 
instances will behave like dict but when seting 
and getting from a text file that holds config values. 
"""

from assignment3 import ConfigDict

cc = ConfigDict('config_file.txt')

print(cc['sql_query'])
print(cc['email_to'])
cc['database'] = 'mysql_managed'

print cc

"""
sql_query=SELECT this FROM that WHERE condition
email_to=me@mydomain.com
num_retries=5
"""