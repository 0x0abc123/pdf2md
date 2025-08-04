import sys
import pymupdf
import pymupdf4llm

doc = pymupdf.open(sys.argv[1])

md_text = pymupdf4llm.to_markdown(doc)
print(md_text)
