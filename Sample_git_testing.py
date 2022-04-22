from datetime import *
import time
from bs4 import BeautifulSoup
import requests

username = "limitededition43"
api_token = "ghp_whatever_this is a secret"
basehtmlurl = "https://github.com/search?q="
baseurl = "https://api.github.com/"
header = {'X-Github-Username': username,
          'X-Github-API-Token': api_token
          }
headers = {'Authorization': f'token {api_token}'}

class_id = "commit-author user-mention"


def secret_keyword_search(repo,keyword):
    res = requests.get(basehtmlurl+ "/"  +repo + "/" + "search?q=" + keyword + "&type=code")
    repos = dict()
    soup = BeautifulSoup(res.content,features="html.parser")
    #print(res.text)
    code_block = soup.find_all(class_= class_id)
    code_name = soup.find_all(class_= code_file)
    code = ('\t'.join([line.text.strip() for line in code_block]))
    file_name = ('\t'.join([line.text.strip() for line in code_name]))
    repos.update({"repo":repo,"Code_block":code,"File_name":file_name})
    print("*****",repos)
    if repos['Code_block'] :
        return(repos)
    else:
        return False


def search_issues(keyword):
    res = requests.get(basehtmlurl+keyword+"&type=issues")
    repos = list()
    soup = BeautifulSoup(res.content,features="html.parser")
    divs = soup.find_all(class_= class_id)
    for div in list(divs):
        if div:
            div = div.text.replace("\n","").replace(" ","")
            if div not in repos:
                repos.append(div)
    return(repos)

def search_commits(keyword):
    class_id = "Link--secondary text-bold text-small"
    res = requests.get(basehtmlurl + keyword + "&type=commits")
    time.sleep(5)
    repos = list()
    soup = BeautifulSoup(res.content, features="html.parser")
    divs = soup.find_all("a", {'class': class_id})
    print(res.status_code)
    # print(res.text)
    for div in list(divs):
        if div:
            div = div.text.replace("\n", "").replace(" ", "")
            if div not in repos:
                repos.append(div)
    return (repos)


def search_repo(keyword):
    time.sleep(3)
    res = requests.get(baseurl + "search/repositories?q="+ keyword,headers=headers)
    if res.status_code == 200:
        return res.text
    else:
        return None

def get_user(user):
    time.sleep(3)
    res = requests.get(baseurl + "/")
    if res.status_code == 200:
        return res.text
    else:
        return None


def get_email(user):
    time.sleep(3)
    res = requests.get(baseurl + "users/" + user, headers=headers)
    if res.status_code == 200:
        return res.text
    else:
        return None

