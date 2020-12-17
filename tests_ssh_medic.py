#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import stat
import click

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help', 'help'])

@click.group(context_settings=CONTEXT_SETTINGS)
def main():
    """
    Ensure SSH directories and files have correct permissions:

    \b
    $HOME/.ssh      -> 700
    authorized_keys -> 644
    known_hosts     -> 644
    config          -> 644
    *.pub keys      -> 644
    All private key -> 600
    """
    return

# introduce seperate sub command that checks the permissions and displays them in terminal
@main.command()
def check():
    click.echo('This sub-command innspects files in ~/.ssh and reports back')

if __name__ == '__main__':
    main()
# -*- coding: utf-8 -*-

