FROM python:3.12

RUN apt-get update && apt-get install -y pipx

WORKDIR /app

COPY . .

RUN useradd -m strg \
      && chown -R strg /app

USER strg

ENV PATH="/home/strg/.local/bin:$PATH"

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1

RUN pipx ensurepath && pipx install poetry==1.8.4 && poetry install

ENV PATH="/app/.venv/bin:$PATH"

CMD ["poetry", "run", "streamlit", "run", "template_streamlit/main.py"]
