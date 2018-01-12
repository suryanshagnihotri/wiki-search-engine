# wiki-search-engine
Search engine built on 75 gb wiki dump
This project generates a sorted indexer for the dump specified. It is optimized by compression
techniques. Given a dump, it will create the inverted index file in Index/ folder, create a tree
of indexers in `Split/` folder for the inverted index and tree in `Title/` for title-docID mappings file.
Inverted index and title mapping file can be found in `Index/` folder<br>

run `start.sh` <br>
indexer : make index <br>
`time python indexer.py ./wiki-search-small.xml` (get xml file which is our dump)

run Kwaymerge.py : merge small files<br>
`time python Kwaymerge.py`<br>

copy file from output_files to index folder and make split folder inside index folder.<br>
run create_index.py  : create multilevel index<br>
`python create_index.py`<br>

finally run query.py : answer query<br>
`python query.py`<br>
