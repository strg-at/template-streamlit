FROM python:3.12-slim

RUN apt-get update && \
    apt-get install -y pipx --no-install-recommends && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . .

RUN useradd -m strg && \
    chown -R strg /app

USER strg

ENV PATH="/home/strg/.local/bin:/app/.venv/bin:$PATH" \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1

RUN pipx ensurepath && \
    pipx install poetry && \
    poetry install

EXPOSE 8501

CMD ["poetry", "run", "streamlit", "run", "template_streamlit/main.py"]
