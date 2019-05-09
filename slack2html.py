#!/usr/bin/env python

import webbrowser
import os

import flask
import click
from slackviewer.app import app
from slackviewer.main import configure_app
from flask_frozen import Freezer


class CustomFreezer(Freezer):

    cf_output_dir = None

    @property
    def root(self):
        return u"{}".format(self.cf_output_dir)


@click.command()
@click.option("-z", "--archive", type=click.Path(), required=True,
              help="Path to your Slack export archive (.zip file)")
@click.option("-o", "--output-dir", type=click.Path(), required=True,
              help="Output directory for HTML files")
@click.option('--no-browser', is_flag=True,
              help="If you do not want a browser to open "
                   "automatically, set this.")
@click.option('--debug', is_flag=True)
def main(archive, output_dir, no_browser, debug):
    configure_app(app=app, archive=archive, channels=None, no_sidebar=False, no_external_references=False, debug=debug)
    # We need relative URLs, otherwise channel refs do not work
    app.config["FREEZER_RELATIVE_URLS"] = True
    # Use a custom subclass of Freezer which allows to overwrite
    #  the output directory
    freezer = CustomFreezer(app)
    freezer.cf_output_dir = output_dir

    # This tells freezer about the channel URLs
    @freezer.register_generator
    def channel_name():
        for channel in flask._app_ctx_stack.channels:
            yield {"name": channel}

    freezer.freeze()

    if not no_browser:
        webbrowser.open("file:///{}/index.html"
                        .format(os.path.abspath(output_dir)))


if __name__ == '__main__':
    main()
