import gzip
import json
import argparse
from pathlib import Path
from tqdm import tqdm

if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Create bilingual pretraining file for tevatron.')
    parser.add_argument('--input', dest='input', required=True)
    parser.add_argument('--output', dest='output', required=True)

    args = parser.parse_args()
    
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    with open(args.input) as f, open(args.output, "w") as g:
        for line in tqdm(f):
            query, text = line.strip().split("\t")
            query = query.strip().lower()
            pos_text = text.strip().lower()
            
            temp = {}
            temp["query"] = query
            temp["positives"] = [pos_text]
            temp["negatives"] = []
            
            g.write(json.dumps(temp)+"\n") 
