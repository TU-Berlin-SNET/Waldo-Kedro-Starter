FROM python:3.8

WORKDIR /home/{{ cookiecutter.project_name }}

COPY ./ .

RUN pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple -r src/requirements.txt

VOLUME /home/{{ cookiecutter.project_name }}/data/00_input
VOLUME /home/{{ cookiecutter.project_name }}/data/99_output

ENTRYPOINT ["kedro", "run"]