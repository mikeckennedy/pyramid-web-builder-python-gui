import cookiecutter.main
import sys
from gooey import Gooey, GooeyParser

from utils import to_project_style


@Gooey(
    program_name='Pyramid app builder',
    program_description='Create a Pyramid web app',
    show_success_modal=False)
def main():
    print(sys.argv)
    info = get_user_values()
    proj_dir = build_app(info)

    print("Project created: {}".format(proj_dir))


def get_user_values():
    parser = GooeyParser()
    parser.add_argument(dest='template',
                        metavar='Project type',
                        help="Type of Pyramid project",
                        choices=['Starter', "Talk Python Entrepreneur's", 'SQLAlchemy', 'SubstanceD', 'ZODB'])
    parser.add_argument('project_name',
                        metavar='Project name',
                        help="The user-visible name of your project")
    parser.add_argument(
        dest='template_language',
        metavar='Template language',
        widget='Dropdown',
        choices=["jinja2", "chameleon", "mako"]
    )
    parser.add_argument(
        dest="working_dir",
        metavar='Output directory',
        help='Directory for project',
        widget="DirChooser")

    sysargs = sys.argv[1:]
    args = parser.parse_args(sysargs)
    return args


def template_to_url(template_name: str) -> str:
    if template_name == 'Starter':
        return 'https://github.com/Pylons/pyramid-cookiecutter-starter'
    elif template_name == 'SQLAlchemy':
        return 'https://github.com/Pylons/pyramid-cookiecutter-alchemy'
    elif template_name == 'SubstanceD':
        return 'https://github.com/Pylons/substanced-cookiecutter'
    elif template_name == "Talk Python Entrepreneur's":
        return 'https://github.com/mikeckennedy/cookiecutter-pyramid-talk-python-starter'
    else:
        raise Exception("Unknown template type")


def build_app(info):
    template = template_to_url(info.template)
    proj_dir = cookiecutter.main.cookiecutter(
        template,
        no_input=True,
        output_dir=info.working_dir,
        extra_context={
            'project_name': info.project_name,
            'repo_name': to_project_style(info.project_name),
            'template_language': info.template_language,
            "project_slug": to_project_style(info.project_name),
            "contact_name": "Company Name",
            "domain_name": "yourcompany.com",
            "contact_email": "contact@company.com",
            "description": "",
            "integrations": "",
            "mailchimp_api": "",
            "mailchimp_list_id": "",
            "outbound_smtp_username": "",
            "outbound_smtp_password": "",
            "outbound_smtp_server": "",
            "outbound_smtp_port": "587",
            "rollbar_access_token": ""
        }
    )

    return proj_dir


if __name__ == '__main__':
    sys.exit(main())
