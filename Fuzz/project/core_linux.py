from invoke import task

import setup
from utils.command_executor import CommandExecutor
from utils.logger import print_task_documentation


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
def task(ctx, param1=False, param2="default text", param3=8, arg=None):
    """
    Task template (on linux)!
    """

    command = [
        "echo",
        f"param1={param1}",
        f"param2={param2}",
        f"param3={param3}",
    ]

    if arg:
        for a in arg:
            command.append(f"arg={a}")

    CommandExecutor(ctx)\
        .add_command(command).execute("project-task.log")
