.PHONY: quality build preview


# Convert all notebooks to MDX files

build:
	python convert_notebooks_to_mdx.py


# Preview the docs site locally

preview: build
	doc-builder preview applied-ml-examples docs/source --not_python_module
