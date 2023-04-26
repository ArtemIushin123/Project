import pyodbc


# WIN-MQA3LH805ND\MSSQLSERVER02 или LAPTOP-6J346A01 шоб не мучались
def get_all_clients():
    connection_string = 'DRIVER={SQL Server};SERVER=LAPTOP-6J346A01;DATABASE=DOCTOR;'
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()
    cursor.execute('select DataTime from timetable')
    result = cursor.fetchall()
    connection.commit()
    connection.close()
    return result





a13 = ['13:00']
a14 = ['14:00']
a15 = ['15:00']
a16 = ['16:00']
a17 = ['17:00']
a18 = ['18:00']
a19 = ['19:00']
a20 = ['20:00']

nn = 8
nk = nn + 7

b = get_all_clients()
i1 = ""
i2 = ""
dk = nn + 1
dt = 0
d = 0
for i in b:
    i1 = str(i)[19:]
    i1 = i1[:-7]
    i2 = i1.translate({ord(','): None})  # год ,  месяц , дата , время

    if int(i2[7:-3]) >= nn and int(i2[7:-3]) < nk:
        if "13" in i2[9:]:
            a13.append(1)
            d = 1
            dt = int(i2[7:-3])
            dk += 1
        if d == 0 and dk == int(i2[7:-3]):
            a13.append(0)
            dk += 1
        if d != 0 and dt != int(i2[7:-3]):
            d = 0
if len(a13) != 8:
    a13.append(0)
b = get_all_clients()
i1 = ""
i2 = ""
dk = nn + 1
dt = 0
d = 0
for i in b:
    i1 = str(i)[19:]
    i1 = i1[:-7]
    i2 = i1.translate({ord(','): None})  # год ,  месяц , дата , время
    if nn <= int(i2[7:-3]) < nk:
        if "14" in i2[9:]:
            # print("-------------11111",i2[7:-3])
            a14.append(1)
            d = 1
            dt = int(i2[7:-3])
            dk += 1
        # print(int(i2[7:-3]), dk, d)
        if d == 0 and dk == int(i2[7:-3]):
            # print("-------------00000",i2[7:-3])
            a14.append(0)
            dk += 1
        if d != 0 and dt != int(i2[7:-3]):
            # print("-------------d=0", i2[7:-3])
            d = 0
if len(a14) != 8:
    a14.append(0)

b = get_all_clients()
i1 = ""
i2 = ""
dk = nn + 1
dt = 0
d = 0
for i in b:
    i1 = str(i)[19:]
    i1 = i1[:-7]
    i2 = i1.translate({ord(','): None})  # год ,  месяц , дата , время
    if nn <= int(i2[7:-3]) < nk:
        if "15" in i2[9:]:
            a15.append(1)
            d = 1
            dt = int(i2[7:-3])
            dk += 1
        if d == 0 and dk == int(i2[7:-3]):
            a15.append(0)
            dk += 1
        if d != 0 and dt != int(i2[7:-3]):
            d = 0
if len(a15) != 8:
    a15.append(0)
b = get_all_clients()
i1 = ""
i2 = ""
dk = nn + 1
dt = 0
d = 0
for i in b:
    i1 = str(i)[19:]
    i1 = i1[:-7]
    i2 = i1.translate({ord(','): None})  # год ,  месяц , дата , время
    if nn <= int(i2[7:-3]) < nk:
        if "16" in i2[9:]:
            a16.append(1)
            d = 1
            dt = int(i2[7:-3])
            dk += 1
        if d == 0 and dk == int(i2[7:-3]):
            a16.append(0)
            dk += 1
        if d != 0 and dt != int(i2[7:-3]):
            d = 0
        # print("16",int(i2[7:-3]))
if len(a16) != 8:
    a16.append(0)
b = get_all_clients()
i1 = ""
i2 = ""
dk = nn + 1
dt = 0
d = 0
for i in b:
    i1 = str(i)[19:]
    i1 = i1[:-7]
    i2 = i1.translate({ord(','): None})  # год ,  месяц , дата , время

    if nn <= int(i2[7:-3]) < nk:
        if "17" in i2[9:]:
            a17.append(1)
            d = 1
            dt = int(i2[7:-3])
            dk += 1
            # print("----------------------11111",i2[7:-3])
        if d == 0 and dk == int(i2[7:-3]):
            a17.append(0)
            dk += 1
            # print("----------------------00000", i2[7:-3])
        if d != 0 and dt != int(i2[7:-3]):
            d = 0
            # print("------------d = 0", i2[7:-3])
if len(a17) != 8:
    a17.append(0)

b = get_all_clients()
i1 = ""
i2 = ""
dk = nn + 1
dt = 0
d = 0
for i in b:
    i1 = str(i)[19:]
    i1 = i1[:-7]
    i2 = i1.translate({ord(','): None})  # год ,  месяц , дата , время
    if nn <= int(i2[7:-3]) < nk:
        if "18" in i2[9:]:
            a18.append(1)
            d = 1
            dt = int(i2[7:-3])
            dk += 1
        if d == 0 and dk == int(i2[7:-3]):
            a18.append(0)
            dk += 1
        if d != 0 and dt != int(i2[7:-3]):
            d = 0
if len(a18) != 8:
    a18.append(0)
b = get_all_clients()
i1 = ""
i2 = ""
dk = nn + 1
dt = 0
d = 0
for i in b:
    i1 = str(i)[19:]
    i1 = i1[:-7]
    i2 = i1.translate({ord(','): None})  # год ,  месяц , дата , время
    if nn <= int(i2[7:-3]) < nk:
        if "19" in i2[9:]:
            a19.append(1)
            d = 1
            dt = int(i2[7:-3])
            dk += 1
        if d == 0 and dk == int(i2[7:-3]):
            a19.append(0)
            dk += 1
        if d != 0 and dt != int(i2[7:-3]):
            d = 0
if len(a19) != 8:
    a19.append(0)
b = get_all_clients()
i1 = ""
i2 = ""
dk = nn + 1
dt = 0
d = 0
for i in b:
    i1 = str(i)[19:]
    i1 = i1[:-7]
    i2 = i1.translate({ord(','): None})  # год ,  месяц , дата , время
    # print(i2)
    if int(i2[7:-3]) >= nn and int(i2[7:-3]) < nk:
        if "20" in i2[9:]:
            a20.append(1)
            d = 1
            dt = int(i2[7:-3])
            dk += 1
            # print("______-------------",i2[7:-3])
        if d == 0 and dk == int(i2[7:-3]):
            a20.append(0)
            dk += 1
        if d != 0 and dt != int(i2[7:-3]):
            d = 0
if len(a20) != 8:
    a20.append(0)

print(a13)
if len(a13) != 8:
    print("13")
print(a14)
if len(a14) != 8:
    print("14")
print(a15)
if len(a15) != 8:
    print("15")
print(a16)
if len(a16) != 8:
    print("16")
print(a17)
if len(a17) != 8:
    print("17")
print(a18)
if len(a18) != 8:
    print("18")
print(a19)
if len(a19) != 8:
    print("19")
print(a20)
if len(a20) != 8:
    print("20")
a = []
a.append(a13)
a.append(a14)
a.append(a15)
a.append(a16)
a.append(a17)
a.append(a18)
a.append(a19)
a.append(a20)


def add_client(name, telephone, mail, client_city):
    connection_string = 'DRIVER={SQL Server};SERVER=LAPTOP-6J346A01;DATABASE=DOCTOR;'
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()
    cursor.execute(f"exec add_client '{name}', '{telephone}', '{mail}', '{client_city}'")
    print(f"exec add_client '{name}', '{telephone}', '{mail}', '{client_city}'")
    connection.commit()
    connection.close()


