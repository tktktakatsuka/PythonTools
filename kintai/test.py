from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("--user-data-dir=C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome\\User Data")
options.add_argument("--profile-directory=Profile 1")
driver = webdriver.Chrome(ChromeDriverManager().install() , options=options)

driver.get("http://redmine.atue.jp/projects/atue-company-overtime/issues/new")
time.sleep(1)

# タイトルに値をセット
title = driver.find_element('id' , 'issue_subject')
time.sleep(1)
title.send_keys('5/25 残業申請(社内)')

# タイトルに値をセット
description = driver.find_element('id' , 'issue_description')
time.sleep(1)
description.send_keys('勤務時間 9:30～18:30(休憩1H)\n残業時間 18:30～19:30(1H)\nオッズパーク案件 投票内容入力画面単体試験実施の為')

# statusに値をセット
status = driver.find_element('id' , 'issue_status_id')
time.sleep(1)
status.send_keys('申請中')

# # 担当者に値をセット
# tantousya = driver.find_element('id' , 'issue_assigned_to_id')
# time.sleep(1)
# tantousya.send_keys('高塚祥太')

# # 作業場所に値をセット
# basyo = driver.find_element('id' , 'issue_custom_field_values_6')
# time.sleep(1)
# basyo.send_keys('池袋')

# # 就業時刻に値をセット
# workTime = driver.find_element('id' , 'issue_custom_field_values_6')
# time.sleep(1)
# workTime.send_keys('18:30~19:30')

# # 開始日に値をセット
# startDate = driver.find_element('id' , 'issue_start_date')
# time.sleep(1)
# startDate.send_keys('2023-05-28')

# 期日に値をセット
dueDate = driver.find_element('id' , 'issue_due_date')
time.sleep(1)
dueDate.send_keys('2023-05-29')

# 予定工数
dueDate = driver.find_element('id' , 'issue_estimated_hours')
time.sleep(1)
dueDate.send_keys('1.0')

# 実績校数
zisseki = driver.find_element('id' , 'issue_estimated_hours')
time.sleep(1)
zisseki.send_keys('1.1')


# 許可者
kyoka = driver.find_element('id' , 'issue_custom_field_values_13')
time.sleep(1)
kyoka.send_keys('弘道 相原')


# 作業区分
kubun = driver.find_element('id' , 'issue_custom_field_values_14')
time.sleep(1)
kubun.send_keys('その他')

time.sleep(100000)

driver.close()