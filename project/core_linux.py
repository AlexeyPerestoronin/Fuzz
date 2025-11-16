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
    },
)
@print_task_documentation
def task(ctx, param1=False, param2="default text", param3=8):
    """
    Task template (on linux)!
    """

    command = [
        "echo",
        f"param1={param1}",
        f"param2={param2}",
        f"param3={param3}",
    ]

    CommandExecutor(ctx).execute(command, log="project-task.log")
