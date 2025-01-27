FROM python:3.11-alpine

RUN apk add pipx

WORKDIR template-streamlit

COPY . .

RUN adduser -S strg \
      && chown -R strg /template-streamlit

USER strg

ENV PATH="/home/strg/.local/bin:$PATH"
RUN pipx ensurepath && pipx install poetry==1.8.3 && poetry install

RUN poetry run python -m unittest discover -s "test" -p "*test*.py"

RUN poetry run streamlit run template_streamlit/main.py
