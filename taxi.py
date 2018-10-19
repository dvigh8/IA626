import csv
# # find min / max
# with open('trip_data_11.csv',"r") as f:
#     reader = csv.reader(f)
#     mindt = 20171212000000
#     maxdt = 0
#     for i, row in enumerate(reader):
#         if i == 0:
#
#             continue
#         else:
#
#             # print (row)
#             tim = row[5].split(' ')
#             # print(tim)
#             dt = tim[0].split('-')
#             dd = tim[1].split(':')
#             if len(dt) == 3:
#                 y = dt[0]
#                 m = dt[1].zfill(2)
#                 d = dt[2].zfill(2)
#                 a = dd[0]
#                 b = dd[1]
#                 c = dd[2]
#                 #print y + m + d
#                 dti = int(y + m + d + a + b + c)
#                 if dti > maxdt:
#                     maxdt = dti
#                 if dti < mindt:
#                     mindt = dti
#
#             if i % 500000 == 0:
#                 print (i)
# print (mindt)
# print (maxdt)
# # find min / max
dic = {}
for i in range(24):
    if i < 10:
        dic['0' + str(i)] = []
    else:
        dic[str(i)] = []



with open('trip_data_11_1000.csv',"r") as f:
    reader = csv.reader(f)
    mindt = 20171212000000
    maxdt = 0
    for i, row in enumerate(reader):
        if i == 0:
            continue
        else:
            # print (row)
            tim = row[5].split(' ')
            # print(tim)
            dt = tim[0].split('-')
            dd = tim[1].split(':')
            if len(dt) == 3:
                a = dd[0]
                dic[str(a)].append(int(row[7]))

            if i % 500000 == 0:
                print (i)
    for i in range(24):
        if i < 10:
            print(str(i) + ' ' + str(sum(dic['0' + str(i)])/ float(len(dic['0' + str(i)]))))
        else:
            print(str(i) + ' ' + str(sum(dic[str(i)])/ float(len(dic[str(i)]))))

# def find_max_min(index):
#     with open('trip_data_11.csv',"r") as f:
#         errors = 0
#         reader = csv.reader(f)
#         maxim = -100000000000000000.000
#         mini = 1000000000000000000.000
#         for i, row in enumerate(reader):
#             if i == 0:
#                 label = row[index]
#                 continue
#             else:
#                 try:
#                     if float(row[8]) != 0.0 and float(row[7]) != 0.0 and float(row[2] != 0.0):
#                         num = float(row[index])
#                         if num > -180.0 and num < 180.0 and num != 0.0:
#                             if num > maxim:
#                                 maxim = num
#                             if num < mini:
#                                 mini = num
#                         if i % 1000000 == 0:
#                             print (i)
#                 except:
#                     errors += 1
#                     print(row[index])
#     print(label + ' ' + str(index) + ' errors ' + str(errors))
#     print ("minimum = " + str(mini))
#     print ("max = " + str(maxim))
#
# numerics = [10,11,12,13]
# for l in numerics:
#     find_max_min(l)


#
# with open('trip_data_11.csv',"r") as f:
#     c = open('trip_data_11_1000.csv',"w")
#     reader = csv.reader(f)
#     writer = csv.writer(c)
#     for i, row in enumerate(reader):
#         if i % 1000== 0:
#             writer.writerow(row)


# def find_distinct(index):
#     with open('trip_data_11.csv',"r") as f:
#         errors = 0
#         reader = csv.reader(f)
#         vals = []
#         for i, row in enumerate(reader):
#             if i == 0:
#                 label = row[index]
#                 continue
#             else:
#                 vals.append(row[index])
#         print(label + ' ' + str(index))
#         print (set(vals))
#
#
# numerics = [9]
# for l in numerics:
#     find_distinct(l)
