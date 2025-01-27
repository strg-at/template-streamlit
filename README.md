<!-- markdownlint-disable MD041 -->
<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD028 -->

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![pre-commit][pre-commit-shield]][pre-commit-url]
[![taskfile][taskfile-shield]][taskfile-url]

# Streamlit Template

This repo is a template to quick start a streamlit application for proof of concept projects

<details>
  <summary style="font-size:1.2em;">Table of Contents</summary>
<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Code-Style](#code-style)
- [Getting Started](#getting-started)
  - [Using Poetry](#using-poetry)
  - [Streamlit](#streamlit)
  - [Prerequisties](#prerequisties)
  - [Initialize repository](#initialize-repository)
  - [Pre-commit](#pre-commit)
  - [Preparation](#preparation)
- [Known Issues](#known-issues)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->
</details>

## Code-Style

<!-- TBD -->

## Getting Started

This Python project is managed via [Poetry](https://python-poetry.org/), and leverages the [pyproject.toml](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)
configuration file, rather than the older `setup.py`.
The `pyproject.toml` configuration file can be and is also used to store 3rd party tools configurations, such as black, ruff, mypy etc.

### Using Poetry

In order to use poetry, you should [install it first](https://python-poetry.org/docs/#installing-with-pipx). If your OS package manager has
a `python-poetry` package, you might also choose to install Poetry that way. **Notice** that if you do this, you should make sure that your OS
also ships all the necessary plugins you might want to use (most importantly, `poetry-plugin-export`). As of the time of writing, Archlinux does.

#### Setup

Install the project, by using:

```bash
poetry install
```

This will install the necessary dependencies **plus the dev dependencies**, any binary shipped with the project, as well as create a dedicated virtual environment.  
The virtual environment can be activated with:

```bash
source $(poetry env info -p)/bin/activate
```

Alternatively, you can also source the script `activate.sh` in this repo:

```bash
source ./activate.sh
```

This has the advantage, over standard venvs management, that you don't need to remember the name of the environment for any project.
If you **don't want** the dev dependencies, simply install the project with `poetry install`.

You can also install the project with `pip`, since Poetry is [PEP-517 compliant](https://python-poetry.org/docs/pyproject/#poetry-and-pep-517):

```bash
pip install .
# OR, using git+ssh
pip install git+ssh://git@github.com:strg-at/template-streamlit.git
```

#### Dependency management

To add a dependency, simply run:

```bash
poetry add 3rd-party-package
```

To remove a dependency, run:

```bash
poetry remove 3rd-party-package
```

To add a dev dependency, run:

```bash
poetry add dev-dep-package --group dev
```

In this template, we also create one (or more) additional dependency group(s) to deal with IDE specific dependencies.
For instance, if you want to use the [python-lsp-server](https://github.com/python-lsp/python-lsp-server), as well as installing
its plugins for `mypy` etc., then you can use the `lsp-dev` group.

```bash
poetry install --with dev --with lsp-dev
```

##### Generating a requirements.txt

You can also generate a `requirements.txt` with poetry. **NOTICE** that this is **not** mandatory at all, and should be done only for backward compatibility, IF necessary.
First, install the `poetry-plugin-export`.
This can be done in [several ways](https://python-poetry.org/docs/plugins/#using-plugins), depending on how you installed poetry.
If you installed poetry via your package manager, then you should install the plugin via your package manager. For instance, on Archlinux:

```bash
sudo pacman -S python-poetry-plugin-export
```

To generate the requirements, you can then run:

```bash
poetry export --without-hashes --format=requirements.txt > requirements.txt
```

#### Version management

Poetry has some nice shortcuts to manage the project version. You can see them by running

```bash
poetry version --help
```

For instance, bumping to the next minor version can be done with:

```bash
poetry version minor
```

This would be a project from, e.g., `1.2` to `1.3`. A major bump can be done with:

```bash
poetry version major
```

Poetry can do more than this, consult the [documentation for more information](https://python-poetry.org/docs/).

### Streamlit

see [streamlit docs](https://docs.streamlit.io) for details

#### Commands

There is a **task** for running the streamlit app:

```bash
task app:run
```

Otherwise the app can also be started with the manual command:

```bash
streamlit run template_streamlit/main.py
```

Look [here](https://docs.streamlit.io/develop/quick-reference/cheat-sheet) for a cheat-sheet of commands and often used widgets

#### Configuration

To customize the theme or adjust rendering logic of e.g. the sidebar, create / update the `.streamlit/config.toml` file in your root folder.
For example, as an app grows, one might want to hide the sidebar with `showSidebarNavigation = true` and implement their own menu.

You can also configure server, client and browser options; for all options see the [docs](https://docs.streamlit.io/develop/api-reference/configuration/config.toml).

#### Plugins and Components

Available streamlit plugins can be found [here](https://streamlit.io/components).
For example for

- more [ui tools/components](https://arnaudmiribel.github.io/streamlit-extras/),
- [additional charting](https://echarts.streamlit.app/),
- a simple kind of [authentication](https://github.com/mkhorasani/Streamlit-Authenticator) or
- [chatbot functionality](https://github.com/ai-yash/st-chat)

### Prerequisties

Install pre-commit.

- [pre-commit][pre-commit]
- [yamllint][yamllint]
- [taskfile][taskfile-url]

### Initialize repository

Pre-commit framework need to get initialized.

```console
task pre-commit:init
```

### Pre-commit

Run the following to fix linting issues using pre-commit.

```bash
task pre-commit:run
```

Based on pre-commit gitleaks dependencies Go language needs to be installed.

### Preparation

All changes require a PR and review. Create a new branch and reference a Jira ticket, f.e.

```console
git switch -c feature/INPRO-1-configure-resource
```

## Known Issues

<!-- TBD -->

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

<!-- Links -->

[pre-commit]: https://pre-commit.com/
[yamllint]: https://github.com/adrienverge/yamllint

<!-- Badges -->

[pre-commit-shield]: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit
[pre-commit-url]: https://github.com/pre-commit/pre-commit
[taskfile-url]: https://taskfile.dev/
[taskfile-shield]: https://img.shields.io/badge/Taskfile-Enabled-brightgreen?logo=task
