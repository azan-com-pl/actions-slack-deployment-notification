import sys
import json
from os import environ
from jinja2 import Environment, FileSystemLoader


def load_env_from_file():
    """
    Load environment variables from a JSON file.
    This method is required for easier testing.
    We test via bash_unit not pytest, as GitHub Actions trigger python script.

    ENV_JSON=file.json python render_template.py template.j2
    """
    if environ.get('ENV_JSON', 'false') != 'false':
        try:
            with open(environ.get('ENV_JSON')) as f:
                data = json.load(f)
                for key, value in data.items():
                    environ[key] = value
        except FileNotFoundError as e:
            raise Exception(f"File {environ.get('ENV_JSON')} not found")


def format_service(service):
    if service == 'pwa':
        return 'PWA'

    return service.capitalize()


def main(template_path):
    env = Environment(loader=FileSystemLoader('./'))
    template = env.get_template(template_path)

    service = environ.get('service')

    variables = {
        "action": environ.get('action'),
        "environment_name": environ.get('environment_name'),
        "environment_url": environ.get('environment_url'),
        "github_actor": environ.get('github_actor'),
        "service": service,
        "service_formatted": format_service(service),
        "release_tag": environ.get('release_tag'),
        "github_release_url": environ.get('github_release_url'),
        "github_run_url": environ.get('github_run_url'),
        "ecs_url": environ.get('ecs_url'),
        "datadog_url": environ.get('datadog_url'),
    }

    print(template.render(variables))


if __name__ == "__main__":
    load_env_from_file()
    main(sys.argv[1])
