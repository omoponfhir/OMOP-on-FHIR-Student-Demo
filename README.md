# Lab-6-OMOPonFHIR

Please see the Lab page on Canvas for more information. The following is only provided as a quick reference.

## Step 1 - Download Athena Vocab
Go to https://athena.ohdsi.org/search-terms/start. Go to Download.

Select the following Vocabularies to Download:
* LOINC
* SNOMED
* RxNorm
* Gender (OMOP Gender)
* Race (Race and Ethnicity Code Set (USBC))

## Step 2 - Add Vocab to Build Path
Extract the .CSV files from the zip provided by Athena. Place the CSVs in the /vocab directory (which should be available when you clone with a place holder file inside it).

## Step 3 - Run Docker
With Docker Desktop/Engine running, execute the following command:
`docker compose up`

## Troubleshooting
If you run into an error, cancel your running container with CTRL+C in the terminal. Then be sure to remove the partially configured container with `docker compose down` before running the `up` command again.
