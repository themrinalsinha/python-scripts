from click import argument, get_current_context, group, option, UsageError

@group(context_settings=dict(help_option_names=['-h', '--help']))
def cli():
    pass

@cli.group(help='for internal use only (automaion commands)')
def automate():
    pass
