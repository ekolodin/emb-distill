# Giga-Embeddings paper

Read the current EACL revision: **[PDF](paper_eacl_revised.pdf)** · [LaTeX source](paper_eacl_revised.tex) · [response draft](rebuttal_eacl.md).

- `paper_arxiv.tex` / `paper_arxiv.pdf`: public preprint with authors, affiliations, and model links.
- `paper_eacl.tex` / `paper_eacl.pdf`: anonymous EACL Industry Track review version.
- `paper_eacl_revised.tex` / `paper_eacl_revised.pdf` / `references_revised.bib`: separate working revision addressing the reviews; remaining evidence limitations are stated in the manuscript.
- `rebuttal_eacl.md`: response draft within the 5000-character limit shown in the OpenReview Official Comment form; contains only the comment body. PDF replacement during rebuttal has not been confirmed.
- `paper_arxiv_source.zip`: self-contained source archive for arXiv submission.
- `paper.tex` / `paper.pdf`: original ICML-style manuscript.

Build a version with `latexmk -pdf <file>.tex`. Remove generated LaTeX intermediates afterward with `latexmk -c <file>.tex`.

Build the working revision with `latexmk -pdf -outdir=revisions/build paper_eacl_revised.tex`; its PDF is written to `revisions/build/paper_eacl_revised.pdf`. Copy it to `paper_eacl_revised.pdf` to update the reader-facing copy.

Internal working notes, server requests, raw evidence bundles, verification artifacts, downloaded metadata and build intermediates stay local and are ignored by Git.
