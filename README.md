# crowdflower-weather
This repo contains 2 things related to the 'weather sentiment' task from Crowdflower's 'data-for-everyone' initiative:

1) Annotated predicates produced by crowdflower during a separate follow-on annotation task, and some processing code. These annotations contributed to the paper "Learning from Measurements in Crowdsourcing Models:Inferring Ground Truth from Diverse Annotation Types" in COLING 2018.

2) Raw annotations from crowdflower
This is also available via the full data link here: https://www.figure-eight.com/data-for-everyone/ although when I checked it last that link was broken so I don't mind including the data here, too, for completeness in documenting the resources used by the paper.

The project contains a dataset/ folder with the raw .csv converted into json annotation streams suitable for use with the dataset-utils code base (from https://github.com/BYU-NLP-Lab/Utilities/tree/master/DatasetUtils/python_datautils). Each contains a README explaining the particulars of how they were compiled.



# Annotation Stream Format
Annotation datasets are encoded as a list of json objects with 
the following structure:

[
    {   batch: 123
        source: "http://document/id",
        data: "The text of the first document",
        label: "TrueLabel",
        trustedlabel: "TrueLabel",
        annotator: "george",
        annotation: "SomeLabel"
        "startTime":1319123,
        "endTime":1319198}
    },
    etc...
]

If 'batch' is set, this annotation was received as part
of a batch of annotations sharing this number.
Annotations in the same batch are reported consecutively.

'label' conveys the value of the true label, if available

'trustedlabel', if present, indicates that the label was
available for use in the experiment.

'datapath' may be substituted for 'data' when dealing with
documents containing text that would be problematic to
embed in json.

startTimeSecs and endTimeSecs are utc timestamps (number
of secs since 1 Jan 1970))







# Background on Crowdflower's "Data for Everyone"
A note on Crowdflower's "data for everyone" initiative here http://www.crowdflower.com/data-for-everyone

Crowdflower didn't originally make their raw annotations available--just the pre-aggregated ones. But, at my request they 
posted some of that data and expressed willingness to do it again in the future. 
