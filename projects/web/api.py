'''
From the command line, run:
  flask --app main.py --debug run
This will start the Flask web but watch it for changes and automatically reload the site.
'''
import glob
import os
import sys
import yaml
import random
from flask import Flask, Blueprint, render_template, request, send_file, redirect, send_from_directory, jsonify


get_name = Blueprint('get_name', __name__)

@get_name.route('/api/name', methods=['GET'])
def getName():
  return jsonify({ 'results': { 'name': 'rob'}})


@get_name.route('/api/random', methods=['GET'])
def getRandom():
  n = int(request.args['n'] or 10)
  r = random.Random()
  return jsonify([r.randint(0,1000000000) for x in range(n)])