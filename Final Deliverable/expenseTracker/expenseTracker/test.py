import ibm_db

conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=98538591-7217-4024-b027-8baa776ffad1.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud;PORT=30875;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=fmc38180;PWD=A5C2mmOTBSeSPc9J;", "", "")
#conn = ibm_db.connect("bludb", "fmc38180", "A5C2mmOTBSeSPc9J")
print('connection established')
title = 'Gulab Jamun'
category = 'Food'
date = '2022-11-15'
amount = 40
id = 4
sql = f"update expense set title = '{title}', category = '{category}', amount = {amount}, date = '{date}' where id = {id}"
select = ibm_db.exec_immediate(conn, sql)
# tuple = ibm_db.fetch_tuple(select)

# while tuple != False:
#     print(f'ID: {tuple[0]} Title: {tuple[1]} Category:{tuple[2]} Amount:{tuple[3]} Date:{tuple[4]}\n')
#     tuple = ibm_db.fetch_tuple(select)

print('query done')
