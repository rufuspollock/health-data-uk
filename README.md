UK Health Data. Research on what's available and what you can do with it.

# What's out there

## Sources

### Health and Social Care Information Center

http://www.hscic.gov.uk/

Appear to be primary data provider of health-related open data in UK (other
than national statistics)

All of their open data is, in theory, on data.gov.uk at
http://data.gov.uk/publisher/nhs-information-centre-for-health-and-social-care
(they still have their own [search
index](http://www.hscic.gov.uk/searchcatalogue) but data.gov.uk is quite a bit
better and easier to use).

Confusingly much of the data listed in their catalog is actually to be found on
the "indicator portal": https://indicators.ic.nhs.uk/webview/

For example, the SHMI (see below) entries in the catalog at
http://www.hscic.gov.uk/searchcatalogue?productid=14111 actually have no data
(just PDFs) and link you to the indicator portal (though not to the actual
relevant dataset!)


### Care Quality Commission

http://www.cqc.org.uk/cqcdata

Only data AFAICT is CQC care directory which is just a list of care providers.

http://www.cqc.org.uk/sites/default/files/media/documents/05_mar_2014_cqc_directory.csv_.csv

## Key Indicators

### SHMI - summary hospital mortality index

SHMI == Observerd Deaths / Expected Deaths


Its a real odyssey to find the data - see below. Here's a the latest CSV data:

https://indicators.ic.nhs.uk/download/SHMI/January_2014/Data/SHMI.csv

Here's a previous quarter release to get a sense of how data gets named.

https://indicators.ic.nhs.uk/download/SHMI/October_2013/Data/SHMI.csv

Here's the data definition file

https://indicators.ic.nhs.uk/download/SHMI/January_2014/Data/SHMI_FILE_DEFINITION.xls

#### Data Complaints

Really quite difficult to track down the data.

* Here on data.gov.uk http://data.gov.uk/dataset/summary_hospital-level_mortality_indicator_shmi

  Unfortunately no actual *data* - all files are links to pages like this: http://www.hscic.gov.uk/catalogue/PUB11278 (which has a bunch of PDFs)
 
* Then tracked it to http://www.hscic.gov.uk/SHMI However, no data on this page (just PDFs describing methodology). If you open [SHMI FAQs PDF](http://www.hscic.gov.uk/media/9926/SHMI-FAQs/pdf/SHMI_FAQ.pdf) on RHS menu and go to page 9 you get told

  > The SHMI publication can be accessed from both the HSCIC publications page and the HSCIC Indicator Portal: 
  > 
  > * Link to HSCIC SHMI publications page [here there is a link that is broken]
  > * Link to HSCIC Indicator Portal https://indicators.ic.nhs.uk/webview/ 

  Next step is to go to indicator site which is a fancy JS site (no shareable URLs) which loads completely b0rked like this:

  <img src="img/indicator-webview-borked.png" />

  But which a reload fixes. After some digging here you find the data we need:

  <img src="img/indicator-webview-shmi.png" />

  And thankfully the data itself has a nice URL: https://indicators.ic.nhs.uk/download/SHMI/January_2014/Data/SHMI.csv

### HES 

HES is the linked data warehouse of what happens to people in hospitals including:

* clinical information about diagnoses and operations
* information about the patient, such as age group, gender and ethnicity
* administrative information, such as time waited, and dates and methods of admission and discharge
* geographical information such as where patients are treated and the area where they live.

A subset of this information is released as open data - mostly monthly summaries. 

http://www.hscic.gov.uk/article/2677/Linked-HES-ONS-mortality-data

Using the linked HES-ONS mortality data, deaths both in and outside hospital following hospital admission or primary procedure have been calculated. Detailed data on aggregated counts of deaths within 30, 60 and 90 days by primary procedure and primary diagnosis is available for HES data years 2007-08, 2008-09 and 2009-10:

xls icon 3 Character Procedure & Diagnosis tables XLS [2Mb]

http://www.hscic.gov.uk/media/11669/3characterprocedurediagnosistables/xls/3_character_procedure_diagnosis_tables_V3_050613.xls

