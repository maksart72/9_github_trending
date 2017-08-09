import datetime
import json
import requests


def get_trending_repositories(top_size):
    delta = datetime.timedelta(days=7)
    date = datetime.date.today() - delta
    url = 'https://api.github.com/search/repositories'
    details = {'q': 'created:>' +
               str(date), 'sort': 'stars', 'order': 'desc', 'per_page': top_size}
    repo_request = requests.get(url, params=details)
    repo_json = json.loads(repo_request.content)
    top_repositories = []
    for repo in repo_json["items"]:
        repo_info = (repo["html_url"], repo["name"], repo["owner"]
                     ["login"], repo["stargazers_count"], repo["open_issues"])
        top_repositories.append(repo_info)
    return top_repositories


def print_trending_repositories_info(repositories):
    for repo in repositories:
        print('* %s, Name: %s Owner: %s Issues: %d URL: %s' %
              (repo[3], repo[1], repo[2], repo[4], repo[0]))


if __name__ == '__main__':
    top_repo = 20
    repositories_list = get_trending_repositories(top_repo)
    print_trending_repositories_info(repositories_list)
