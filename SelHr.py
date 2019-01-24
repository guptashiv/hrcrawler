from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import argparse
from getpass import getpass
import json
import requests

solURL = 'https://www.hackerrank.com/rest/contests/eso207pa1/submissions/'

#will contain latest submission ids for each user
StackIDs = {} 
PrefIDs = {}

def getSubIDs(jdata, idDictionary):	
	total = jdata['total']
	for i in range(total):
		curr = jdata['models'][i]
		uname = curr['hacker_username']
		subID = curr['id']
		if not (uname in idDictionary.keys()):
			idDictionary[uname] = subID


def getCode(subID, uname):
	# print('subID is', subID )
	sub = solURL + str(subID)
	driver.get(sub)
	jdata = json.loads(driver.find_element_by_id("json").text)
	curr = jdata['model']	
	slug = curr['slug']
	print(['code'], file=open(slug+'/'+uname+'.cpp', "w"))
	# exctract JSON HERE. jdata['code'] will have the actual code





parser = argparse.ArgumentParser(description = "Loging in")
parser.add_argument("username")
args = parser.parse_args()
args.password = getpass("password: " )

#conts
giturl = 'http://github.com/login'
hrurl = 'https://www.hackerrank.com/auth/login'
ccurl = 'https://www.codechef.com/login'
ccprivate = 'https://www.codechef.com/users/shivgupta/edit'


prefSubmUrl = "https://www.hackerrank.com/rest/contests/eso207pa1/judge_submissions/?offset=0&limit=1000&challenge_id=i-am-prefixed"
stackSubUrl = "https://www.hackerrank.com/rest/contests/eso207pa1/judge_submissions/?offset=0&limit=1000&challenge_id=stack-em-up"


driver = webdriver.Firefox()

driver.get(hrurl)
f = driver.find_element_by_tag_name('form')
username = f.find_element_by_name('username')
password = f.find_element_by_name('password')
login = f.find_element_by_tag_name('button')
# creds = {'username': args.username, 'password':args.password}
# driver.post(hrurl, creds)

username.send_keys(args.username)
password.send_keys(args.password)
login.click()


driver.get(prefSubmUrl)
prefJson = json.loads(driver.find_element_by_id("json").text)
# print(prefJson['total'])


driver.get(stackSubUrl)
stackJson = json.loads(driver.find_element_by_id("json").text)
# print(stackJson['total'])


getSubIDs(stackJson, StackIDs)
getSubIDs(prefJson, PrefIDs)


for k in StackIDs.keys():
	getCode(StackIDs[k], k)

for k in PrefIDs.keys():
	getCode(PrefIDs[k], k)

# print(StackIDs)

# for i in range(prefJson['total']):
# 	curr = prefJson['models'][i]
# 	uname = curr['hacker_username']
# 	subID = curr['id']
# 	if not (uname in PrefIDs.keys()):
# 		PrefIDs[uname] = subID
# 	k = input()
# 	if(k=='q'):
# 		break



# print(prefResp.content)
# print(type(prefResp))
# solution = driver.get()

# print(driver.page_source)

k = input()

# driver.get(hrprivate)
driver.quit()
