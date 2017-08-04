import requests
import datetime
import json

def get_trending_repositories(top_size):
    delta = datetime.timedelta(days=7)
    date = datetime.date.today()-delta
    url = 'https://api.github.com/search/repositories'
    details = {'q':'created:>'+str(date),'sort':'stars', 'order':'desc'}
    r = requests.get(url,params=details)
    data = json.loads(r.content)
    for repo in data["items"]:
        print(repo["html_url"],repo["name"],repo["owner"]["login"],repo["stargazers_count"])  
    #print(data)

def get_open_issues_amount(repo_owner, repo_name):
    pass

if __name__ == '__main__':
    top_size = 20
    get_trending_repositories(top_size)
