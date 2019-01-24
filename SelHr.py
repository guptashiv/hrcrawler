from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import argparse
from getpass import getpass
import json
import requests


parser = argparse.ArgumentParser(description = "Loging in")
parser.add_argument("username")
args = parser.parse_args()
args.password = getpass("password: " )

#conts
giturl = 'http://github.com/login'
hrurl = 'https://www.hackerrank.com/auth/login'
ccurl = 'https://www.codechef.com/login'
ccprivate = 'https://www.codechef.com/users/shivgupta/edit'
hrprivate = 'https://www.hackerrank.com/contests/cs345a18pa1/judge/submissions/challenge/match-me-if-you-can'

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
print(prefJson['total'])


driver.get(stackSubUrl)
stackJson = json.loads(driver.find_element_by_id("json").text)
print(stackJson['total'])


for i in range(prefJson['total']):
	print(prefJson['models'][i])
	k = input()
	if(k=='q'):
		break
		
# print(prefResp.content)
# print(type(prefResp))
# solution = driver.get()

# print(driver.page_source)

k = input()

# driver.get(hrprivate)
driver.quit()
