import click
import json
import logging
from task import run_task


@click.command()
@click.option('--name', help='Service name.')
@click.option('--description', help='Service description.')
@click.option('--parameters', help="Task parameters in JSON format e.g.: \"{'param1':'value1','param2':'value2'}\".")
@click.option('--service-metadata', help="Service Metadata in JSON format e.g.: \"{'param1':'value1','param2':'value2'}\".")
def run(name, description, parameters, service_metadata):
    """Run task."""
    logging.basicConfig(level=logging.INFO, format='%(levelname)s %(asctime)s %(message)s')
    run_task(name, description, eval(parameters), eval(service_metadata))

if __name__ == '__main__':
    run()
