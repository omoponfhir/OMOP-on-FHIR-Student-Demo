# OMOP-on-FHIR DEMO

For help with this demo, please reach out to Elizabeth.Shivers@gtri.gatech.edu.

*! Warning: The `/resources` folder contains in progress work to streamline loading Synthea transaction bundles. It is not currently functional and should be disregarded. !*

## Quick Start
### Step 1 - Download Athena Vocab
Go to https://athena.ohdsi.org/search-terms/start. Go to Download.

Select the following Vocabularies to Download:
* LOINC
* SNOMED
* RxNorm
* Gender (OMOP Gender)
* Race (Race and Ethnicity Code Set (USBC))

### Step 2 - Add Vocab to Build Path
Extract the .CSV files from the zip provided by Athena. Place the CSVs in the /vocab directory (which should be available when you clone with a place holder file inside it).

### Step 3 - Run Docker
With Docker Desktop/Engine running, execute the following command:
`docker compose up`

## Troubleshooting
If you run into an error, cancel your running container with CTRL+C in the terminal. Then be sure to remove the partially configured container with `docker compose down` before running the `up` command again.

## Health Check Script
The OMOP CDM database image used includes a health check script which allows the OMOP on FHIR container to wait until the `f_person` tables are available prior to starting. This shows up as an expected "error" in the logs, as follows:

```
2023-06-30 16:58:46.481 UTC [91] ERROR:  relation "f_person" does not exist at character 15
2023-06-30 16:58:46.481 UTC [91] STATEMENT:  SELECT * FROM f_person;
```
This message can be disregarded.

Please note this script may not work consistently in all environments, and has been observed to not always function as expected in Non-WSL Windows deployments, starting the OMOP on FHIR container prior to the required dependencies being setup. In such a case, you may have to stop the containers *after the database has been loaded fully* and rerun them per the troubleshooting section of this file. (It should pick up with the database fully loaded and should not impact the operation of the containers.)