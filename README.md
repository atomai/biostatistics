# LocusZoom Association Viewer
## Summary
The LocusZoom Association Viewer allows the user to easily view the results of their own genome wide association tests, including PLINK, RAREMETALWORKER, and EPACTS.  Upon runnning this program, the user browses to localhost (127.0.0.1) on their browser, at the port they specified. Three different types of graphs are available:  
* Manhattan Plot
* LocusZoom Plot
* QQ Plot
  * Currently, only available for EPACTS files

#### Manhattan Plot
The manhattan plot is a scatterplot of all points.  Points have tooltips and are clickable if they are deemed statistically significant ( > 1e-4). However, if the point is deemed as statistically insignificant, it is binned, and therefore will not include tooltips and will not be clickable.  Upon click, the user is taken to a LocusZoom Plot with a region that is centered around the point clicked.

#### QQ Plot
The QQ plot generates multiple scatter plots on the same chart based on differing MAF ranges if the input file is EPACTS; Otherwise, a normal QQ plot is generated. 

#### LocusZoom Plot
The LocusZoom Plot is a scatterplot of a specific region of a chromosome.  Points have tooltips that show additional information.

## Command Line Options
The only required command line argument is the filename, which should be directly after the program name.
The program is ran with multiple options inlucding:
* `--help`		list off all of the command line options
* `--port`		you can specify a port at which to view the results
* `--range`		specify a specific range of format [CHROMOSOME]:[START POSITION]-[END POSITION] to view.
  * if range is specified, the default homepage is the LocusZoom Plot with specified range.
  * if range is not specified, the default homepage is the Manhattan Plot
* `--EPACTS | --PLINK | --RAREMETAL`		Although this program does have a filetype-autodetect feature, you can explicitly denote filetype to be certain results are correct.

## Installation 
There are two methods for running this package

####Install this package via pip* 
Run the pip command in your terminal or chosen shell
```
pip install lz_assoc_viewer
```
Then, run the program using the following syntax:
```
lz_assoc_viewer --port [PORT] --range [RANGE] [FILENAME]
```

#### Download this package from the github repository
Put your results file and associated tabix file in the program's directory, and then run the program by putting running `__main__.py`:
```
python __main__.py --port [PORT] --range [RANGE] [FILENAME]
```
	
###### Sample use of command line options:
lz_assoc_viewer my_results.gz --range 11:113580000-114150000 --port 5541 
(notice, order of arguments is not important)

*not live on pypi yet(7/13/2016)