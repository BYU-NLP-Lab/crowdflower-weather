#!/usr/bin/python3
import argparse
from python_datautils import pipes
from subprocess import call
from uuid import uuid4
import json

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--non-agg-path",default="../raw/weather-non-agg-DFE.csv",help="Path to input .details file (for data)")
    parser.add_argument("--agg-path",default="../raw/weather-evaluated-agg-DFE.csv",help="Path to input .crd file (for annotations)")
    args = parser.parse_args()

    # translate crowdflower fieldnames into our fieldnames
    pipe = pipes.input_csv(args.non_agg_path)
    pipe = pipes.pipe_rename_attr(pipe,"_worker_id",rename_to="annotator")
    pipe = pipes.pipe_rename_attr(pipe,"_started_at",rename_to="starttime")
    pipe = pipes.pipe_rename_attr(pipe,"_created_at",rename_to="endtime")
    pipe = pipes.pipe_rename_attr(pipe,"what_emotion_does_the_author_express_specifically_about_the_weather",rename_to="annotation")
    pipe = pipes.pipe_rename_attr(pipe,"tweet_id",rename_to="source")
    pipe = pipes.pipe_rename_attr(pipe,"tweet_text",rename_to="data")

    # convert times -> timestamps
    pipe = pipes.pipe_txt2int_parse_timestamp(pipe,"starttime")
    pipe = pipes.pipe_txt2int_parse_timestamp(pipe,"endtime")

    # parse gold-standard label data
    labelpipe = pipes.input_csv(args.agg_path)
    labelpipe = pipes.pipe_rename_attr(labelpipe,"sentiment",rename_to="label")
    labelpipe = pipes.pipe_rename_attr(labelpipe,"tweet_id",rename_to="source")
    labelpipe = pipes.pipe_rename_attr(labelpipe,"tweet_text",rename_to="data")
    # only keep those judged correct with greater than 0.9 confidence
    labelpipe = pipes.pipe_drop_by_regex(labelpipe,"is_the_category_correct_for_this_tweet",pattern="No")
    labelpipe = pipes.pipe_append_thresholded_value(labelpipe,"is_the_category_correct_for_this_tweet:confidence",dest_attr="confidence",levels=[0.9],names=["low","high"])
    labelpipe = pipes.pipe_drop_by_regex(labelpipe,"confidence",pattern="low")

    # combine annotations and labels
    pipe = pipes.pipe_concat(pipe,labelpipe)
    
    # eliminate unneeded fields
    pipe = pipes.pipe_retain_attrs(pipe,["annotation","annotator","label","source","starttime","endtime","data"])

    # pretty print
    print(json.dumps(list(pipe), separators=(',',': '), sort_keys=True, indent=4))
