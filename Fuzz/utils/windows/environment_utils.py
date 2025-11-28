def extend_path(paths: list):
    context = {}

    def setup_context(env_name, env_value):
        context[env_name] = env_value

    path_extensions = [
        *paths,
        # add here env-variables should be shared on each invoke-task on windows
    ]
    path_string = ";".join(path_extensions) + ";%PATH%"
    setup_context("PATH", path_string)

    return context

def activate_VS2019_environment():
    return [
        "call",
        "\"C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/Common7/Tools/vsdevcmd\"",
        "-arch=x64",
    ]
