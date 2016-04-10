all: env pip-tools pip
dev: env pip-tools dev-pip

.PHONY: env
env:
	pyvenv-3.5 env
	env/bin/pip install -U pip

.PHONY: pip-tools
pip-tools:
	env/bin/pip install pip-tools

.PHONY: pip
pip:
	env/bin/pip-sync requirements.txt

.PHONY: dev-pip
dev-pip:
	env/bin/pip-sync requirements.txt dev-requirements.txt

.PHONY: pip-compile
pip-compile:
	env/bin/pip-compile requirements.in
	env/bin/pip-compile dev-requirements.in

.PHONY: run
run:
	env/bin/python manage.py runserver 0.0.0.0:8080

.PHONY: migrate
migrate:
	env/bin/python manage.py migrate

.PHONY: clean_cache
clean_cache:
	find **/__pycache__ -delete

.PHONY: tags
tags:
	ctags -R

.PHONY: clean
clean: clean_cache
	rm -rf env tags

.PHONY: static
static:
	env/bin/python manage.py collectstatic --noinput

.PHONY: shell
shell:
	env/bin/python manage.py shell
