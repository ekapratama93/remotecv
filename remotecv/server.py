#!/usr/bin/python
# -*- coding: utf-8 -*-

# remote cv service
# https://github.com/globocom/thumbor/wiki

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2011 globo.com timehome@corp.globo.com

import sys
import argparse
import logging

from tornado_server import run_server
#from zmq_server import run_server

def main(params=None):
    if params is None:
        params = sys.argv[1:]
    parser = argparse.ArgumentParser(description='Runs RemoteCV.')

    conn_group = parser.add_argument_group('Connection arguments')
    conn_group.add_argument('-b', '--bind', default='*', help='IP address to bind')
    conn_group.add_argument('-p', '--port', default=13337, type=int, help='Port to listen')

    other_group = parser.add_argument_group('Other arguments')
    other_group.add_argument('-l', '--level', default='debug', help='Logging level')

    arguments = parser.parse_args(params)

    logging.basicConfig(level=getattr(logging, arguments.level.upper()))

    run_server(arguments.bind, arguments.port)


if __name__ == "__main__":
    main()
