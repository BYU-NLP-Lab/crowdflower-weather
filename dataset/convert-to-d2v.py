#!/usr/bin/python3
import argparse
from python_datautils import pipes
from python_datautils import gensim_pipes
from subprocess import call
from uuid import uuid4
import json

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--inpath",default="weather.json",help="Path to annotation stream with lexical data.")
    parser.add_argument("--modelpath",default="/local/plf1/enwiki_word2vec/enwiki-word2vec.model",help="Path to pre-trained word2vec model.")
    parser.add_argument("--dictpath",default="../raw/bohan_norm_lexicon_emnlp2012.txt",help="Path to pre-trained word2vec model.")
    parser.add_argument("--dictdelim",default="=",help="")
    args = parser.parse_args()
    
    lookup = [v.strip().split("=") for v in open(args.dictpath).readlines()]
    lookup = {k.lower():v for k,v in lookup}

    # parse annotations
    pipe = pipes.input_json(args.inpath)
    # transform all punctuation into spaces
    pipe = pipes.pipe_txt2txt_sub(pipe,"data",pattern="[^\w]",sub=" ")
    pipe = pipes.pipe_txt2txt_dictionary_lookup(pipe,"data",lookup,word_delim=" ")
    pipe = gensim_pipes.pipe_txt2list_doc2vec(pipe,id_attr="source",data_attr="data",model=args.modelpath,word_delim=" ")
    pipe = pipes.pipe_val2txt_stringcast(pipe,"data")

    # pretty print
    print(json.dumps(list(pipe), separators=(',',': '), sort_keys=True, indent=4))
