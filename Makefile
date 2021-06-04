install:
	poetry install

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

brain-calc:
	poetry run brain-calc

brain-gcd:
	poetry run brain-gcd

brain-progression:
	poetry run brain-progression

brain-prime:
	poetry run brain-prime

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	python3 -m pip install --user --force-reinstall dist/*.whl

lint:
	poetry run flake8 brain_games
	poetry run flake8 brain_even
	poetry run flake8 brain_calc
	poetry run flake8 brain_gcd
	poetry run flake8 brain_progression
	poetry run flake8 brain_prime

install-all:
	poetry install
	poetry build
	poetry publish --dry-run
	python3 -m pip install --user dist/hexlet_code-0.7.9-py3-none-any.whl
	poetry run flake8 brain_games
	poetry run flake8 even_even
	poetry run flake8 brain_calc
	poetry run flake8 brain_gcd
	poetry run flake8 brain_progression
	poetry run flake8 brain_prime
