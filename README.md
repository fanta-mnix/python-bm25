# BM25 for document ranking
This project implements BM25 algorithm described in [this paper](https://pdfs.semanticscholar.org/c0a4/8ed7577a7b48288dfb2711cbd86e30636b5f.pdf) for ranking documents according to relevance.

## Installing
Make sure to run the `setup.sh` script. It will install all required dependencies.
 
## Running the sample
Use `python sample.py` to see it in action. It may take some time, but eventually it will print to the console retrieved documents matching the query, sorted by relevance.

## Known issues
This implementation is best fit for small datasets because it lacks the inverted index required for fast querying in big datasets

## Alternatives
https://github.com/nhirakawa/BM25
