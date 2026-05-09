reports = {
    'report_1': [7, 6, 4, 2, 1],
    'report_2': [1, 2, 7, 8, 9],
    'report_3': [9, 7, 6, 2, 1],
    'report_4': [1, 3, 2, 4, 5],
    'report_5': [8, 6, 4, 4, 1],
    'report_6': [1, 3, 6, 7, 9],
}

def main():
    displayOption()
    

# displayOption - Choose displaying logs
def displayOption():

    classifications_logs = None
    process_logs = None

    while classifications_logs not in ['Y', 'N'] or process_logs not in ['Y', 'N']:

        if classifications_logs not in ['Y', 'N']:
            entry = input("Do you want to display all classifications logs? (Y/N) ").upper()
            if entry in ['Y', 'N']:
                classifications_logs = entry
            else:
                print("Please enter 'Y' or 'N' only.")

        if classifications_logs in ['Y', 'N'] and process_logs not in ['Y', 'N']:
            entry = input("Do you want to display all process logs? (Y/N) ").upper()
            if entry in ['Y', 'N']:
                process_logs = entry
            else:
                print("Please enter 'Y' or 'N' only.")

    # Start classifying            
    classify(classifications_logs, process_logs)
    

# Classify - Increasing or Decreasing
def classify(classifications_logs, process_logs):

    indexer = 0
    role_value = 0
    final_role_value = 0
    classifying_number = 1
    status = ''
    display_filtered = 'no'
    classified_reports = {}

    # Start classifying
    print('\n ---------------( -> Start classifying <- )--------------- \n')

    for i in reports:
        if classifications_logs == 'Y':
           print(f'### {classifying_number}) Starting with -> {i}: {reports[i]} \n')
        while indexer < len(reports[i]) - 1:
            if reports[i][indexer] >= reports[i][indexer + 1]:
                if classifications_logs == 'Y':
                    print(f"[{reports[i][indexer]} >= {reports[i][indexer + 1]}]: Decreasing")
                role_value -= 1
            elif reports[i][indexer] <= reports[i][indexer + 1]:
                if classifications_logs == 'Y':
                    print(f"[{reports[i][indexer]} <= {reports[i][indexer + 1]}]: Increasing")
                role_value += 1
            indexer += 1
            continue
        if(role_value == -4):
            final_role_value = role_value
            status = 'Decreasing'
        elif(role_value == 4):   
            final_role_value = role_value
            status = 'Increasing'
        else:
            final_role_value = role_value
            status = 'Unsafe'
        indexer = 0
        role_value = 0
        classifying_number += 1 
        if status == 'Unsafe':
            if classifications_logs == 'Y':
                print(f"\nX [Not safe order] {i}: {reports[i]} >> status: {status} <<-->> role_value: {final_role_value} << \n")
            classified_reports[f'{i}_{status}_order'] = reports[i] 
        else: 
            if classifications_logs == 'Y':
                print(f"\n{i}: {reports[i]} >> status: {status} <<-->> role_value: {final_role_value} << \n")
            classified_reports[f'{i}_{status}_order'] = reports[i]
    if classifications_logs == 'Y':
        print('\n ------------------------------------------------------------ \n')
    display_filtered = 'yes'    

    if display_filtered == 'yes':

        print('### Classifications Reports Filtered Successfully >> \n')

        for i in classified_reports:
            print(i, ':', classified_reports[i]) 

        # Start process_logsing
        process(classified_reports, process_logs)       



def process(reports, process_logs):

    # Start processing
    print('\n ---------------( -> Start processing <- )--------------- \n')

    final_report_result = {}
    report_result = 0
    display_result = 'no'
    process_number = 1

    for i in reports:
        if process_logs == 'Y':
           print(f'### {process_number}) Starting with -> {i}: {reports[i]} \n')
        for j in range(len(reports[i]) - 1):
            if(abs(reports[i][j] - reports[i][j + 1]) <= 3 and abs(reports[i][j] - reports[i][j + 1]) >= 1):
                if process_logs == 'Y':
                   print(f'safe [{reports[i][j]} - {reports[i][j + 1]}] = {abs(reports[i][j] - reports[i][j + 1])}')
                report_result += 1 
            else:
                if process_logs == 'Y':
                   print(f'-> not safe [{reports[i][j]} - {reports[i][j + 1]}] = {abs(reports[i][j] - reports[i][j + 1])} --> out of 1 - 3 level range')
                report_result -= 1
        if report_result == len(reports[i]) - 1:
           if process_logs == 'Y':
              print('\n report_result: ', report_result, '\n')
              print('------------------------------------------------------------ \n')
           if i.endswith('Unsafe_order'):
              final_report_result[f'{i}_is_not_safe'] = reports[i]
           else:
               final_report_result[f'{i}_is_safe'] = reports[i]
        else:
            if process_logs == 'Y':
               print('\n report_result: ', report_result, '\n')
               print('------------------------------------------------------------ \n')
            final_report_result[f'{i}_is_not_safe'] = reports[i]
        report_result = 0
        process_number += 1

    display_result = 'yes'
    if display_result == 'yes':

        print('### Processing Reports Completed Successfully >> \n')

        for i in final_report_result:
            print(i, ':', final_report_result[i]) 

        # Start process_logsing   
        print('\n ---------------( -> Report filtered successfully <- )--------------- \n')
        displayFinalReportsOutput(final_report_result)


def displayFinalReportsOutput(reports):

    print('### Final Reports Displayed Successfully >> \n')

    number_of_safe= 0
    number_of_unsafe = 0

    for i in reports:
        for j in reports[i]:
            print(j, end=' ')

        if i.endswith("is_not_safe"):
            status = "Unsafe"
            number_of_unsafe += 1
        else:
            status = "safe"
            number_of_safe += 1
        
        print(f": {status}")
    
    print(f"\nSafe Reports -> {number_of_safe} \nUsafe Reports -> {number_of_unsafe}")
    print('\n ---------------( -> Final Reports Results <- )--------------- \n')


                        
if __name__ == "__main__":
    main()