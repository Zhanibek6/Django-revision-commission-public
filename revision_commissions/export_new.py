import xlsxwriter
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

titles_extra = [
    "Коррупционные и уголовные действия при освоении бюджетных средств",
    "Дисциплинарные взыскания, дискредитирующие государственную службу",
    "Количество материалов рассмотренных советом по этике",
    "Количество сотрудников, привлеченных к дисциплинарной ответственности советом по этике",
    "Административные меры в результате выявленных нарушений по государственным закупкам",
    "Дисциплинарные меры в результате выявленных нарушений по государственным закупкам",
    "Увольнение в результате выявленных нарушений по государственным закупкам"
]


def calculate(x, y, calc_type):
    if x == 0 or y == 0:
        return 0
    result = 0

    if calc_type == 1:
        return round(x/y*100, 2)

    elif calc_type == 2:
        return round(y/x*100, 2)
    
    elif calc_type == 3:
        return round(x/y*100-100, 2)

    elif calc_type == 4:
        return round(y/x*100-100, 2)

    elif calc_type == 5:
        return y.year-x.year
    
    return round(result, 2)

# 1
def year_finance(value):
    title = "Годовой объем финансирования учреждения"
    score = 3 if value >= 1000000 else 2 if value >= 400000 else 1 if value >= 200000 else 1
    value = str(value)+" тенге."
    return [title, value, score]

# 2
def finance_increase(last_year, cur_year):
    title = "Рост/снижение объемов финансирования по сравнению с прошлым периодом"
    value = calculate(last_year, cur_year, 4)
    score = 3 if value >= 30 else 2 if value >= 20 else 1 if value >= 15 or value <= 15 else 1

    value = str(value)+" %"
    return [title, value, score]

# 3
def budget_utilization(finance_amount, cash_expense):
    title = "Освоение бюджетных средств на конец года"
    value = calculate(finance_amount, cash_expense, 2)
    score = 3 if value < 93 else 2 if value < 97 else 1 if value < 100 else 1

    value = str( value ) + " %"
    return [title, value, score]

# 4
def last_audit(last_check, factual_date):
    title = "Срок с момента проведения последнего государственного аудита"
    value = calculate(last_check, factual_date, 5)
    score = 3 if value >= 3 else 2 if value >= 2 else 1 if value >= 1 or value <= 1 else 1

    value = str(value) + " год"
    return [title, value, score]

# 5
def recovered_funds(fin_violations, recovered_funds):
    title = "Доля востановленных/возмещенных средств от объема выявленных финансовых нарушений"
    value = calculate(fin_violations, recovered_funds, 2)
    score = 3 if value <= 80 else 2 if value <= 90 else 1 if value <= 100 else 1

    value = str(value) + " %"
    return [title, value, score]

# 6
def fin_violations(fin_violations, cash_expense):
    title = "Доля финансовых нарушений от общего объема расходов текущего периода"
    value = calculate(fin_violations, cash_expense, 1)
    score = 3 if value >= 10 else 2 if value >= 5 else 1 if value >= 0 else 1

    value = str( value ) + " %"
    return [title, value, score]

# 7
def debt_change(debt_current, debt_previous):
    title = "Рост/снижение объема дебиторской задолженности по сравнению с прошлым периодом"
    value = calculate(debt_current, debt_previous, 3)
    score = 3 if value >= 20 else 2 if value >= 10 else 1 if value >= 0 else 1

    value = str( value ) + " %"
    return [title, value, score]

# 8 
def credit_change(credit_current, credit_previous):
    title = "Рост/снижение объема кредиторской  задолженности по сравнению с прошлым периодом"
    value = calculate(credit_current, credit_previous, 3)
    score = 3 if value >= 30 else 2 if value >= 20 else 1 if value >= 0 else 1

    value = str( value ) + " %"
    return [title, value, score]

# 9+
def extra(value, i):
    title = titles_extra[i]
    score = 1 if value <= 1 else 2 if value <= 2 else 3 if value <= 3 else 1
    value = str(value)+" ед"
    return [title, value, score]


# table 2
# 5
def capital_change(capital_current, capital_previous):
    title = "Рост/снижение объема уставного капитала по сравнению с прошлым периодом"
    value = calculate(capital_current, capital_previous, 3)
    score = 3 if value >= 30 else 2 if value >= 20 else 1 if value >= 0 else 1

    value = str(value) + " %"
    return [title, value, score]

#6
def net_profit_change(profit_current, profit_previous):
    title = "Рост/снижение чистой прибыли по сравнению с прошлым периодом"
    value = calculate(profit_current, profit_previous, 3)
    score = 3 if value <= 2 else 2 if value >= 3 else 1 if value > 4 else 1

    value = str(value) + " %"
    return [title, value, score]

#7
def dividents(dividents_current, profit_current):
    title = "Доля выплаченных дивидендов (доли части чистого дохода) от чистой прибыли"
    value = calculate(dividents_current, profit_current, 1)
    score = 3 if value >= 10 else 2 if value >= 2 else 1 if value >= 0 else 1

    value = str(value) + " %"
    return [title, value, score]

#8
def administrative_spendings(spendings_current, cash_expense):
    title = "Доля административных расходов от общего объема расходов текущего периода"
    value = calculate(spendings_current, cash_expense, 1)
    score = 3 if value >= 30 else 2 if value >= 20 else 1 if value >= 10 else 1

    value = str(value) + " %"
    return [title, value, score]


def risk_group(points):
    title = "Группа риска"
    score = 3 if points >= 23 else 2 if points >= 19 else 1 if points >= 15 else 1

    return [title, points, score]

'''
ГУ
0 Годовой объем финансирования учреждения
1 Объем финансирования прошлого периода
2 Объем финансирования текущего периода
3 Объем финансирования на конец финансового года
4 Кассовый расход(исполнение плаченных обязательств по бюджетным программам (подпрограммам)
5 Дата проведения последней проверки
6 Фактическая дата на конец отчетного периода
7 Объем выявленных финансовых нарушений
8 Объем востановленных/возмещенных средств
9 Объем дебиторской задолженности текущего периода
10 Объем дебиторской задолженности прошлого периода
11 Объем кредиторской  задолженности текущего периода
12 Объем кредиторской  задолженности прошлого периода
13 Коррупционные и уголовные действия при освоении бюджетных средств
14 Дисциплинарные взыскания, дискредитирующие государственную службу
15 Количество материалов рассмотренных советом по этике
16 Количество сотрудников, привлеченных к дисциплинарной ответственности советом по этике
17 Административные меры в результате выявленных нарушений по государственным закупкам
18 Дисциплинарные меры в результате выявленных нарушений по государственным закупкам
19 Увольнение в результате выявленных нарушений по государственным закупкам
'''


'''
КВАЗИ
0 Годовой объем финансирования учреждения
1 Объем финансирования на конец финансового года
2 Кассовый расход(исполнение плаченных обязательств по бюджетным программам (подпрограммам)
3 Дата проведения последней проверки
4 Фактическая дата на конец отчетного периода
5 Объем выявленных финансовых нарушений
6 Объем востановленных/возмещенных средств
7 Объем дебиторской задолженности текущего периода
8 Объем дебиторской задолженности прошлого периода
9 Объем кредиторской  задолженности текущего периода
10 Объем кредиторской  задолженности прошлого периода
11 Коррупционные и уголовные действия при освоении бюджетных средств
12 Дисциплинарные взыскания, дискредитирующие государственную службу
13 Количество сотрудников, привлеченных к дисциплинарной ответственности советом по этике
14 Административные меры в результате выявленных нарушений по государственным закупкам
15 Дисциплинарные меры в результате выявленных нарушений по государственным закупкам
16 Увольнение в результате выявленных нарушений по государственным закупкам
17 Объем уставного капитала текущего периода
18 Объем уставного капитала прошлого периода
19 Объем чистой прибыли текущего периода
20 Объем чистой прибыли прошлого периода
21 Объем дивидендов текущего периода
22 Объем административных расходов текущего периода
'''

#sample_arr2 = [50000, 25000, 27000, 40000, 10000, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
#sample_arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]

def generate_organization_data(arr, type):
    if type == "ГУ":
        table = [
            year_finance(arr[0]),
            finance_increase(arr[1], arr[2]),
            budget_utilization(arr[3], arr[4]),
            last_audit(arr[5], arr[6]),
            recovered_funds(arr[7], arr[8]),
            fin_violations(arr[7], arr[4]),
            debt_change(arr[9], arr[10]),
            credit_change(arr[11], arr[12]),
        ]

        for i in range(7):
            table.append(extra(arr[13+i], i))

    elif type == "КВАЗИ":
        table = [
            year_finance(arr[0]),
            budget_utilization(arr[1], arr[2]),
            last_audit(arr[3], arr[4]),
            recovered_funds(arr[5], arr[6]),
            capital_change(arr[17], arr[18]),
            net_profit_change(arr[19], arr[20]),
            dividents(arr[21], arr[19]),
            administrative_spendings(arr[22], arr[2]),
            debt_change(arr[7], arr[8]),
            credit_change(arr[9], arr[10]),
            extra(arr[11], 0),
            extra(arr[14], 4),
            extra(arr[15], 5),
            extra(arr[16], 6)
        ]

    scores = sum([x[2] for x in table])
    risk = risk_group(scores)
    table.append(["Сумма баллов", "", scores])
    table.append(risk)

    return table


def export_to_excel(arr, filename):
    workbook = xlsxwriter.Workbook(f'{BASE_DIR}/revision_commissions/exports/{filename}.xlsx', options={'remove_timezone': True})
    worksheet = workbook.add_worksheet()

    # Ширину для тайтла
    worksheet.set_column(0, 0, 81)
    
    for row in range(len(arr)):
        for column in range(len(arr[row])):
            worksheet.write(row, column, arr[row][column])
    
    workbook.close()


def parse_data(clean_data, type):
    values = list(clean_data.values())[1:]
    [int(x) for x in values if isinstance(x, int)]
    org_data = generate_organization_data(values, type)
    score = org_data[-1][1]
    risk = org_data[-1][2]
    return [score, risk]