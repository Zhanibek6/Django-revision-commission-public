import xlsxwriter
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def get_formula(x, y, i):
    if x == 0 or y == 0:
        return 0
    result = 0
    if i == 4 or i == 5 or i == 8 or i == 9:
        #result += X/Y*100-100
        return round(x/y*100-100, 2)
    elif i == 1 or i == 3:
        #result += y/x*100
        return round(y/x*100, 2)
    elif i == 6 or i == 7:
        # X / Y * 100
        return round(x/y*100, 2)
    elif i == 2:
        #result += (y-x)/365
        return y.year-x.year
    
    return round(result, 2)


def get_score(num, i):
    if i == 0:
        return 3 if num >= 1000000 else 2 if num >= 400000 else 1 if num >= 200000 else 0
    if i == 1:
        return 3 if num <= 94 else 2 if num <= 96 else 1 if num <= 100 else 0
    if i == 2:
        return 3 if num >= 3 else 2 if num >=2 else 1 if num >= 1 else 0
    if i == 3:
        return 3 if num <= 80 else 2 if num <= 90 else 1 if num <= 100 else 0
    if i == 4 or i==9:
        return 3 if num >= 30 else 2 if num >= 20 else 1 if num >= 0 else 0
    if i == 5:
        return 3 if num <= 2 else 2 if num >= 3 else 1 if num > 4 else 0
    if i == 6:
        return 3 if num >= 10 else 2 if num >= 2 else 1 if num >= 0 else 0
    if i == 7:
        return 3 if num >= 30 else 2 if num >= 20 else 1 if num >= 10 else 0
    if i == 8:
        return 3 if num >= 20 else 2 if num >= 10 else 1 if num >= 0 else 0
    if i > 9:
        return 1 if num <= 1 else 2 if num <= 2 else 3 if num <= 3 else 0
    
#            0            1    2         3      4     5   6     7      8
metrics = [" тыс. тенге", "%", " год", " %", "%", "%", "%", "%", " ед.", "%"]
titles = ["Годовой объем финансирования учреждения",
        "Освоение бюджетных средств на конец года", 
        "Срок с момента проведения последнего государственного аудита",
        "Доля востановленных/возмещенных средств от объема выявленных финансовых нарушений",
        "Рост/снижение объема уставного капитала по сравнению с прошлым периодом",
        "Рост/снижение чистой прибыли по сравнению с прошлым периодом",
        "Доля выплаченных дивидендов (доли части чистого дохода) от чистой прибыли ",
        "Доля административных расходов от общего объема расходов текущего периода",
        "Рост/снижение объема дебиторской задолженности по сравнению с прошлым периодом",
        "Рост/снижение объема кредиторской  задолженности по сравнению с прошлым периодом",
        "Коррупционные и уголовные действия при освоении бюджетных средств",
        "Количество сотрудников, привлеченных к дисциплинарной ответственности советом по этике",
        "Административные меры в результате выявленных нарушений по государственным закупкам",
        "Дисциплинарные меры в результате выявленных нарушений по государственным закупкам",
        "Увольнение в результате выявленных нарушений по государственным закупкам"]
# 15
# = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
# = [0, 1,    2,    3,    4,    5,     6,      7,      8,      9,      10, 11, 12, 13, 14]
data_indexes = {
    0: 0,
    1: 1,
    2: 3,
    3: 5,
    4: 7,
    5: 9,
    6: 11,
    7: 13,
    8: 15,
    9: 17,
    10: 19,
    11: 20,
    12: 21,
    13: 22,
    14: 23
}

def generate_organization_data_2(arr):
    result = []
    data_ind = 0
    for i in range(15):
        row = []
        # Название
        row.append(titles[i])

        # У первой строки нет формулы

        if i==0 or i>9:
            number = arr[data_indexes[i]]
        else:
            # Число
            number = get_formula(arr[ data_indexes[data_ind] ], arr[ data_indexes[data_ind] +1], i)

        # Все поля выше 8 считаются в ед
        if i>=9:
            metric = " ед."
        else:
            metric = metrics[i]

        row.append(str(number)+metric)

        # Баллы
        row.append(get_score(number, i))

        # increment data ind to get to next point
        data_ind += 1

        result.append(row)
    
    return result


def export_to_excel(arr, filename):
    workbook = xlsxwriter.Workbook(f'{BASE_DIR}/revision_commissions/exports/export.xlsx')
    worksheet = workbook.add_worksheet()

    # Ширину для тайтла
    worksheet.set_column(0, 0, 81)
    
    for row in range(len(arr)):
        for column in range(len(arr[row])):
            worksheet.write(row, column, arr[row][column])
    
    workbook.close()


if __name__=="__main__":
    #             0       1      2      3      4     5     6      8      9      10     11    12    13     14    15
    fake_data = [50000, 30000, 40000, 45000, 60000, 2013, 2020, 30000, 45000, 13000, 15000, 6000, 7000, 10000, 5000, ]
    #export_organization(fake_data, "sample")
    org = generate_organization_data_2(fake_data)
    print(org)
    #export_to_excel(org, "testing")

        

