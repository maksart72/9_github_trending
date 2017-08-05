import datetime
import json
import requests



def get_trending_repositories(top_size):
    delta = datetime.timedelta(days=7)
    date = datetime.date.today() - delta
    url = 'https://api.github.com/search/repositories'
    details = {'q': 'created:>' + str(date), 'sort': 'stars', 'order': 'desc'}
    repo_request = requests.get(url, params=details)
    repo_json = json.loads(repo_request.content)
    top_repositories = []
    for repo in repo_json["items"]:
        info = [repo["html_url"], repo["name"], repo["owner"]
                ["login"], repo["stargazers_count"], repo["open_issues"]]
        top_repositories.append(info)
    top_repositories = top_repositories[0:top_size]
    return top_repositories


def print_trending_repositories_info(repositories):
    for repo in repositories:
        print('* ' + str(repo[3]) + ', Name:' + str(repo[1]) + ', Owner:' +
              str(repo[2]) + ', Issues:' + str(repo[4]) + ', URL:' + repo[0] + '')

if __name__ == '__main__':
    top_repo = 20
    repositories_list = get_trending_repositories(top_repo)
    print_trending_repositories_info(repositories_list)
