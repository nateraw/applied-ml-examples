from argparse import Namespace
from pathlib import Path

from doc_builder.commands.notebook_to_mdx import notebook_to_mdx_command


def main(notebooks_root: str = "./notebooks", docs_root: str = "./docs/source"):
    notebooks_root = Path(notebooks_root)
    docs_root = Path(docs_root)

    for src_path in Path("notebooks").glob("**/*.ipynb"):
        # Relative path to notebooks
        relative_path = src_path.relative_to(notebooks_root)
        dest_path = docs_root / relative_path.with_suffix(".mdx")
        notebook_to_mdx_command(
            Namespace(
                notebook_file=str(src_path),
                max_len=119,
                dest_file=str(dest_path),
            )
        )


if __name__ == "__main__":
    main()
