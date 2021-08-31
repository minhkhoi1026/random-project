from bs4 import BeautifulSoup
from decouple import config

# load HTML to parser
GPA_path = config('HTML_PATH')
with open(GPA_path, "r", encoding = 'utf-8') as f:
    data = f.read()
    soup = BeautifulSoup(data, "lxml")

# find table contain GPA
table = soup.find('table', id = "tbDiemThiGK")
# Loop through the table to get all GPAs
table_body = table.find('tbody')
GPAs =[]
rows = table_body.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    GPAs.append(cols)

# function to calculate cummulative GPA from GPA list
def summary(GPAs, subignore = []):
    sum_credit = 0
    sum_GPA = 0
    expected_credit = 0
    for GPA in GPAs:
        sub_name, sub_credit, sub_GPA = GPA[1], GPA[2], GPA[5]
        if all(item not in sub_name for item in subignore) and  sub_credit != '':
            expected_credit += int(sub_credit)
        if any(item in sub_name for item in subignore) or sub_credit == '' or sub_GPA == '':
            continue
        sub_credit = int(sub_credit)
        sub_GPA = float(sub_GPA)
        sum_credit += sub_credit
        sum_GPA += sub_GPA * sub_credit

    print('Cummulative GPA:', sum_GPA / sum_credit)
    print('Cummulative credit:', sum_credit)
    print('Expected credit:', expected_credit)

# ignore subject that not join in GPA
subignore = ['BAA00011', 'BAA00012', 'BAA00013', 'BAA00014',
             'BAA00030', 'ADD00002', 'BAA00021', 'BAA00022']
summary(GPAs, subignore)
