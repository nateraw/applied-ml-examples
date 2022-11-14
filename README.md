# applied-ml-examples
Temporary repo to put some applied ML examples


## Setup

```
pip install git+https://github.com/huggingface/doc-builder.git@main#egg=hf-doc-builder
pip install watchdog black
```

## Usage

1. Edit notebook files in `notebooks/`.
2. Run `make preview` to view the site locally

When happy with the changes, commit the notebook/any changes to `docs/source/_toctree.yml`, push to new branch on GitHub, and open a PR.
