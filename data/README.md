# Dataset

## [FootballDB](FootballDB)
The [FootballDB](FootballDB) folder has 3 subfolders [v1](FootballDB/v1/), [v2](FootballDB/v2/), [v3](FootballDb/v3/). 

Each of these folders contains the data for each version of the database schema used in our experiments. Each folder is structrured as follows: 
 
* 100 --> the 100 training split & test data
* 200 --> the 200 training split & test data
* 300 --> the 300 training split & test data
* db --> the database dump

## [results](results)

The [results](results) file contains all of the evaluation results for each NL-to-SQL system used in our evaluations: 

* [GPT-3.5_s](results/GPT-3.5_s/) --> zero shot and few shot results
* [GPT-3.5_sc](results/GPT-3.5_sc/) --> zero shot and few shot results
* [T5-Picard](results/T5-Picard/) --> zero shot and results for each training split
* [T5](results/T5/) --> zero shot and results for each training split
* [ValueNet](results/ValueNet/) --> zero shot and results for each training split
