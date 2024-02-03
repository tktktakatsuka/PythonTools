from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("--user-data-dir=C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome\\User Data")
options.add_argument("--profile-directory=Profile 1")
driver = webdriver.Chrome(ChromeDriverManager().install() , options=options)

driver.get("http://redmine.atue.jp/projects/atue-company-overtime/issues/new")
time.sleep(1)

def sendKeyById(idName , sendString):
    title = driver.find_element('id' , idName)
    time.sleep(1)
    title.clear()
    title.send_keys(sendString)

def selectVlueById(idName , selectValue):
    WebElement = driver.find_element('id' , idName)
    select = Select(WebElement)
    time.sleep(1)
    select.select_by_visible_text(selectValue)
    
def checkBoxClickById(idName ):
    title = driver.find_element('id' , idName)
    time.sleep(1)
    title.click()
    
def checkBoxClickByXpath(idName ):
    title = driver.find_element(By.XPATH , idName)
    time.sleep(1)
    title.click()


    
# # 作業場所に値をセット
sendKeyById('issue_custom_field_values_6' , '池袋') 
# # 就業時刻に値をセット
sendKeyById('issue_custom_field_values_8' , '18:30~19:30') 
# # 開始日に値をセット

sendKeyById('issue_start_date' , '2023-05-28') 
# # 期日に値をセット
sendKeyById('issue_due_date' , '2023-05-29') 
# # 予定工数
sendKeyById('issue_estimated_hours' , '1.0') 
#工数実績
sendKeyById('issue_custom_field_values_12' , '1.1') 
# タイトルに値をセット
sendKeyById('issue_subject' , '5/25 残業申請(社内)') 
# 説明文に値をセット
sendKeyById('issue_description' , '勤務時間 9:30～18:30(休憩1H)\n残業時間 18:30～19:30(1H)\nオッズパーク案件 投票内容入力画面単体試験実施の為') 

# # 許可者
selectVlueById('issue_custom_field_values_13' , '弘道 相原')
# # 作業区分
selectVlueById('issue_custom_field_values_14' , 'その他')
# セレクトボックスの指定
selectVlueById('issue_assigned_to_id' , '高塚 祥太')

#checkBoxのクリック
checkBoxClickById('issue_watcher_user_ids_69')
checkBoxClickById('issue_watcher_user_ids_101')
checkBoxClickById('issue_watcher_user_ids_85')
checkBoxClickById('issue_watcher_user_ids_6')
checkBoxClickById('issue_watcher_user_ids_100')
checkBoxClickById('issue_watcher_user_ids_99')
checkBoxClickById('issue_watcher_user_ids_102')
checkBoxClickById('issue_watcher_user_ids_98')

#status
selectVlueById('issue_status_id' , '申請中')

checkBoxClickByXpath('//*[@id="issue-form"]/input[1]')

driver.close()