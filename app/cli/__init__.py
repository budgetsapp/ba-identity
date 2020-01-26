
import click
from flask.cli import with_appcontext
from app.extensions import db
from app.services import user as user_service


def init_cli_commands(app):
    app.cli.add_command(init_db_command)
    app.cli.add_command(load_db_data_command)
    app.cli.add_command(get_user_command)


def init_db():
    # import is important
    import app.models.role
    import app.models.user
    import app.models.user_roles
    # then create
    db.create_all()


@click.command("init-db")
@with_appcontext
def init_db_command():
    init_db()
    click.echo('Initialized the database')


# Load init data

def get_item_by_value(items, key, value):
    match = None
    for item in items:
        if item[key] == value:
            match = item
            break
    return match


def load_db_data():
    from app.models.role import Role
    from app.models.user import User
    import json
    import os

    root = os.path.realpath(os.path.dirname(__file__))

    # roles_seed_data = json.load(open(os.path.join(root, "roles.json")))
    # for role in roles_seed_data:
    #     r = Role(id=role["id"], display_name=role["display_name"])
    #     db.session.add(r)

    # users_seed_data = json.load(open(os.path.join(root, "roles.json")))
    # for user in users_seed_data:
    #     u = User(id=user["id"], login=user["login"], display_name=user["display_name"],
    #              password=user["password"])
    #     db.session.add(u)

    # ba_user_1 = get_item_by_value(users_seed_data, "login", "ba-user-1")
    # ba_user_2 = get_item_by_value(users_seed_data, "login", "ba-user-2")

    # role_admin = get_item_by_value(roles_seed_data, "display_name", "admin")
    # role_user = get_item_by_value(roles_seed_data, "display_name", "user")

    # roles data
    roles_seed_data = json.load(open(os.path.join(root, "roles.json")))

    role_admin_raw = get_item_by_value(
        roles_seed_data, "display_name", "admin")
    role_admin = Role(id=role_admin_raw["id"],
                      display_name=role_admin_raw["display_name"])

    role_user_raw = get_item_by_value(roles_seed_data, "display_name", "user")
    role_user = Role(id=role_user_raw["id"],
                     display_name=role_user_raw["display_name"])

    # users data
    users_seed_data = json.load(open(os.path.join(root, "users.json")))

    ba_user_1_raw = get_item_by_value(users_seed_data, "login", "ba-user-1")
    ba_user_1 = User(id=ba_user_1_raw["id"],
                     login=ba_user_1_raw["login"],
                     display_name=ba_user_1_raw["display_name"],
                     password=ba_user_1_raw["password"])
    ba_user_1.roles.append(role_admin)
    db.session.add(ba_user_1)

    ba_user_2_raw = get_item_by_value(users_seed_data, "login", "ba-user-2")
    ba_user_2 = User(id=ba_user_2_raw["id"],
                     login=ba_user_2_raw["login"],
                     display_name=ba_user_2_raw["display_name"],
                     password=ba_user_2_raw["password"])
    ba_user_2.roles.append(role_user)
    db.session.add(ba_user_2)

    db.session.commit()


@click.command("load-db-data")
@with_appcontext
def load_db_data_command():
    load_db_data()
    click.echo('Loaded data')


@click.command("get-user")
@with_appcontext
def get_user_command():
    user = user_service.get_user_by_login("ba-user-1")
    click.echo(user)
