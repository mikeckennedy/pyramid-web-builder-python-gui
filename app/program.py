import cookiecutter.main
import sys
from gooey import Gooey, GooeyParser

from utils import to_project_style


def main():
    print("sys.argv: {}".format(sys.argv))
    if '--ignore-gooey' not in sys.argv:
        info = get_user_values()
    elif '/var/folders/' in sys.argv:
        return
    else:
        info = windows_callback_args_workaround()
    proj_dir = build_app(info)

    print("Project created: {}".format(proj_dir))


@Gooey(
    program_name='Pyramid app builder',
    program_description='Create a Pyramid web app')
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

    args = parser.parse_args()
    return args


def windows_callback_args_workaround():
    if len(sys.argv) != 6:
        return Args()

    # second callback args:
    # exe  --ignore-gooey "Starter" "test3" "chameleon" "C:\Users\mkennedy\Desktop"
    args = Args()
    args.template = sys.argv[2]
    args.project_name = sys.argv[3]
    args.template_language = sys.argv[4]
    args.working_dir = sys.argv[5]

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


class Args:
    pass


if __name__ == '__main__':
    main()
