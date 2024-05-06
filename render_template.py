import sys
import json
from os import environ
from jinja2 import Environment, FileSystemLoader

def main(template_path):
    env = Environment(loader=FileSystemLoader('./'))
    template = env.get_template(template_path)

    variables = {
      "action": environ.get('action'),
      "environment_name": environ.get('environment_name'),
      "environment_url": environ.get('environment_url'),
      "github_actor": environ.get('github_actor'),
      "service": environ.get('service'),
      "release_tag": environ.get('release_tag'),
      "github_release_url": environ.get('github_release_url'),
      "github_run_url": environ.get('github_run_url'),
      "ecs_url": environ.get('ecs_url'),
      "datadog_url": environ.get('datadog_url'),
    }

    print(template.render(variables))

if __name__ == "__main__":
    main(sys.argv[1])
