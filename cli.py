#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import module
import click

# define a dictionary to hold context; the dictionary sets a list onto help_option_names...
CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.group(context_settings=CONTEXT_SETTINGS)
def main():
    return

@main.command()
@click.pass_context
def help(ctx):
    print(ctx.parent.get_help())

#@main.argument(hidden=True)
#@click.pass_context
#def help(ctx): #, topic, **kw):
#    print(ctx.parent.get_help())


if __name__ == '__main__':
    main()

# program condition requirements
# 1 the .ssh/ directory must have 700 permission
# 2 authorized_key_known_hosts_congif, and any public(ending in .pub) needs to have 644 permissions
# 3 all private keys must have 600 permission bits
