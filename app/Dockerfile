FROM python:3.10.2-slim

RUN apt update && apt install -y --no-install-recommends default-jre

# default non-root user (security)
RUN useradd -ms /bin/bash python

WORKDIR /home/python/app

COPY --chown=python:python pyproject.toml .
COPY --chown=python:python pdm.lock .
COPY --chown=python:python .pdm.toml .

RUN pip install pdm

RUN echo 'eval "$(pdm --pep582)"' >> /home/python/.bashrc

RUN python -m pdm install

USER python

ENV MY_PYTHON_PACKAGES="/home/python/app/.venv"
ENV PYTHONPATH="${PYTHONPATH}:/home/python/app/blog:$MY_PYTHON_PACKAGES/lib/python3.10/site-packages"
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV PATH $PATH:${MY_PYTHON_PACKAGES}/bin

WORKDIR /home/python/app/blog

CMD [ "tail", "-f", "/dev/null" ]
