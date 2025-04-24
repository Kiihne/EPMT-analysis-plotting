# EPMT_analysis

For demonstrating the analysis capabilities of EPMT through jupyter notebooks.

A quick description of each notebook-


`Analysis-Example`
this notebook demonstrates the most basic functionality of
the `epmt_query` and `ui` modules. Great place to start!
Keeps it simple and straightforward. If you find this too
simple, consider delving into one of the other notebooks.

contains a number of basic plots focused on smaller amounts of data.

`Query-API`
this notebook demonstrates the more advanced functionalities of
epmt's querying code base. This notebook dives head first into
querying for lower-level data directly, including processes,
threads, and roots. If Analysis-Example barely whetted your
appetite, here's where to look next!

this notebook currently undergoing some maintenance, but is in
a fairly usable state.

`Outliers`
this notebook demonstrates the outlier detection capabilities of
epmt, which rely on `PyOD` and `sklearn` python packages. As yet
another more advanced example, it's best tackled after first
understanding the Analysis-Example notebook. Conducts a simple
principle component analysis (PCA) for both single and multi
variable approaches. Further goes on to lay out a basic root
cause analysis (RCA).

this notebook currently undergoing some maintenance, but is in
a fairly usable state.

`OCEAN_field_analysis`
This notebook separates 'ocean' jobs from other tags, and conducts
a variety of analysis examples on them, including bar plots and 
2D histograms. heavy emphasis on rssmax.

`ocean_outliers`
A series of two notebooks that are near idenitical. They separate 
'ocean' jobs and train a model based on those jobs. Then a 
separate set of data is called and applied to the model. we 
create a plot based on the results as a proof-of-concept.
The difference between the notebooks is that one of them normalizes
the data used to make the model.

`procs_analysis`
Notebook that uses basics of [get_procs] to start to look at how 
procs can be used for more detailed analysis. Splits jobs down 
into individual operations and makes basic comparision plots.
Currently a work in progress.


