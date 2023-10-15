# Python Incremental Linting

This repository presents a combined solution of two linters for incremental code formatting.
Format only modified code blocks and check code quality in modified files.

## Installation

Clone the repository to your computer:
```shell
git clone git@github.com:mnv/python-incremental-linting.git
```

Install the requirements:
```shell
pip install -r requirements.txt
```

## Usage

The commands are configured in `Makefile` (`make.bat` also available for Windows):
- `make lint` – static analysis for modified files
- `make fix` – fixing modified files

Linters configuration is stored in the `pyproject.toml` file. Customize it as needed.
Try to change some files in `sandbox` and run the commands.

### Automatic formatting

Code style check:
```shell
darker --revision origin/main --diff --check .
```

Auto format:
```shell
darker --revision origin/main .
```

### Code quality

Check for potential code flaws:
```shell
ruff check $(git diff --name-only --diff-filter=d $(git merge-base HEAD master) | grep -E \.py$)
```

Try to fix found code flaws:
```shell
ruff --fix --silent --exit-zero $(git diff --name-only --diff-filter=d $(git merge-base HEAD master) | grep -E \.py$)
```

### Automation commands

Code quality check:
```shell
make lint
```

Fixing modified files:
```shell
make fix
```

Run these commands from the source directory where `Makefile` is located.

## Related projects

Projects on which the current solution is based:
- [darker](https://github.com/akaihola/darker) – reformat and lint modified Python code
- [ruff](https://github.com/astral-sh/ruff) – an extremely fast Python linter, written in Rust
- [git-diff-lint](https://github.com/codeocelot/git-diff-lint) – lint only the files your branch touches

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
