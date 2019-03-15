import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


# Make an API call and store the response.

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)

# Store API response in a variable.
response_dict = r.json()
print(response_dict.keys())
print('total repositories: ', response_dict['total_count'])
print('repositories returned: ', len(response_dict['items']))
print("\nSelected information about each repository:")
repo_dicts = response_dict['items']
names, plot_dicts = [], []
i=0
for repo_dict in repo_dicts:
    print(i, repo_dict['stargazers_count'], repo_dict['description'], repo_dict)
    i += 1
    names.append(repo_dict['name'])
    if not repo_dict['description']:
        repo_dict['description'] = ''
    plot_dicts.append({'value': repo_dict['stargazers_count'], 'label': repo_dict['description']})


# Make visualization.
my_style = LS('#333366', base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.show_y_guides = False
my_config.width = 1000
my_config.value_formatter = lambda x: '{:,}'.format(x)
chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names
chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')

