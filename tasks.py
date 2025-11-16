from invoke import task, Collection

import setup
import project
from utils.logger import INFO


@task(pre=[setup.setup_context])
def get_info(ctx):
    """
    Print to console information about active configuration of invoke-tasks
    """
    env_context = setup.get_env_context()

    # Define custom formatters for string columns
    formatters = {}
    for col in env_context.select_dtypes(include='object').columns:
        max_len = env_context[col].astype(str).str.len().max()
        formatters[col] = lambda x, length=max_len: f"  {x:<{length}s}"

    INFO.log_line("Active environment configuration:") \
        .log_line(f"{env_context.to_string(formatters=formatters, index=False)}")


namespace = Collection()
namespace.add_task(get_info, name="get-info")
namespace.add_collection(project.collection)
