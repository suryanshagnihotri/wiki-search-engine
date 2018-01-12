mkdir Output_files
echo "Running Indexer"
time python indexer2.py ./wiki-search-small.xml
echo "Merging"
time python merge.py
for FILENAME in ./Output_files/*; do mv $FILENAME ./Output_files/index.txt; done
mkdir Index
mkdir Index/Split
mkdir Title
mkdir Title/Split
cp ./Output_files/index.txt ./Index/index.txt
echo "Spitting"
time python create_index.py
echo "Query Time"
time python query.py