setup: python-setup mysql-setup

python-setup:
	pip install -r requirements.txt
run:
	python manage.py runserver

mysql-setup:
	docker pull mysql:5.7

mysql-run:
	docker run --name gestao_usuario \
		-e MYSQL_ROOT_PASSWORD=myrootpassword \
		-e MYSQL_USER=gestaousuario \
		-e MYSQL_PASSWORD=mypassword \
		-e MYSQL_DATABASE=gestaousuario_mysql \
		--publish 3306:3306 \
		-d mysql:5.7
