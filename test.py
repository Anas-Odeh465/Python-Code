

# for i in reports:
#     print(f'\n # Starting with -> {i}: {reports[i]} \n')
#     for j in reports[i]:
#         print('-', end=' ')

# final_report_result = {}
# report_result = 0
# display_result = 'no'

# for i in reports:
#     print(i, reports[i])
#     for j in range(len(reports[i]) - 1):
#         if(abs(reports[i][j] - reports[i][j + 1]) <= 3 and abs(reports[i][j] - reports[i][j + 1]) >= 1):
#           print(f'safe [{reports[i][j]} - {reports[i][j + 1]}] = {abs(reports[i][j] - reports[i][j + 1])}')
#           report_result += 1 
#         else:
#            print(f'-> not safe [{reports[i][j]} - {reports[i][j + 1]}] = {abs(reports[i][j] - reports[i][j + 1])} --> out of 1 - 3 level range')
#            report_result -= 1
#     if report_result == len(reports[i]) - 1:
#        print('\n report_result: ', report_result)
#        if i.endswith('Unsafe_order'):
#            final_report_result[f'{i}_is_not_safe'] = reports[i]
#        final_report_result[f'{i}_is_safe'] = reports[i]
#     else:
#        print('\n report_result: ', report_result)
#        final_report_result[f'{i}_is_not_safe'] = reports[i]
#     report_result = 0

# display_result = 'yes'
# if display_result == 'yes':

#     print('Classifications reports Filtered Successfully >> \n')

#     for i in final_report_result:
#         print(i, ':', final_report_result[i]) 

#     # Start process_logsing   
#     print('\n ---------------( -> Report filtered successfully <- )--------------- \n') 

# reports = {
#     'report_1': [7, 6, 4, 2, 1],
#     'report_2': [1, 2, 7, 8, 9],
#     'report_3': [9, 7, 6, 2, 1],
#     'report_4': [1, 3, 2, 4, 5],
#     'report_5': [8, 6, 4, 4, 1],
#     'report_6': [1, 3, 6, 7, 9],
# }

# for i in reports:
#     for j in reports[i]:
#         print(j, end=' ')

#     status = "Safe"
    
#     print(f": {status}")



        



