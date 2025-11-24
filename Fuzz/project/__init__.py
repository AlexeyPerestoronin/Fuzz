import os
from invoke import Collection, task

import setup
from utils.logger import print_task_documentation

if os.name == "nt":
    from . import core_windows as core
elif os.name == "posix":
    from . import core_linux as core
else:
    raise Exception("unsupported operation system!")


@task(
    pre=[setup.setup_context],
    help={
        "param1": "boolean parameter",
        "param2": "text parameter",
        "param3": "digit parameter",
        "arg": "list argument - can be used multiple times in CLI",
    },
    iterable=["arg"],
)
@print_task_documentation
def full_check(ctx, param1=False, param2="default text", param3=8, arg=None):
    """
    Project full check (template of combined task)!
    """

    core.task(ctx, param1=param1, param2=param2, param3=param3, arg=arg)


collection = Collection("project")
collection.add_task(full_check, name="full-check")
collection.add_collection(Collection.from_module(core, name="core"))
