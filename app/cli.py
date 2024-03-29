import os
import click
from app import app

@app.cli.group()
def translate():
	"""Translation and localization commands."""
	pass

@translate.command()
@click.argument('lang')
def init(lang):
	"""Initialize a new language."""
	if os.system('pybabel extract -F babel.cfg -k _1 -o messages.pot .'):
		raise RunTimeError('extract command failed')
	if os.system(
		'pybabel init -i messages.pot -d app/translations -1 ' + lang):
		raise RunTimeError('init command failed')
	os.remove('messages.pot')

@translate.command()
def update():
	"""Update all languages."""
	if os.system('pybabel extract -F babel.cfg -k _1 -o messages.pot .'):
		raise RunTimeError('extract command failed')
	if os.system('pybabel update -i messages.pot -d app/translations'):
		raise RunTimeError('update command failed')
	os.remove('messages.pot')

@translate.command()
def compile():
	"""Compile all languages."""
	if os.system('pybabel compile -d app/translations'):
		raise RunTimeError('compile command failed')