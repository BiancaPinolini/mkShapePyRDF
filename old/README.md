# mkShapePyRDF
Example of analysis with PyRDF and ROOT RDataFrame for the Latinos framework

## log

Open `LatinosSparkTest.ipynb` on https://swan.cern.ch.

* set the bleeding-edge pytohn
* connect to spark cluster

produce `sample.json`

example:
```
python unfold_sample.py -i "./Full2017v6/samples.py" -o Full2017v6/samples.json -s Wjets DY VBS ttbar singleTop
```