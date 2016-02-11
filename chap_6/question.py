"""
the purpose of the assignment is to create our 
own class called ConfigKeyError to handdle 
potentail errors we can run into from the previous 
assignment.
"""

from assignment4 import ConfigDict

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