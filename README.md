# assessment-yello-cabs-ny

# Repo structure
``` shell
.
├── src                         
│   ├── __init__.py
│   ├── bigquery_handler.py      //file that inits the client and execute the query.
│   ├── entrypoint.py            //file with the necessary functions to work with excel files
│   ├── logger_handler.py        //file that creates the logger especifying the name file.
│   ├── main.py                  //file with the main function that extracts, processes and prepares the response.
│   ├── response_hanlder.py      //file that prepares the body response
│   └── exception.py             //file with all the exceptions necessary for the whol process
├── tests (TO DO)          // unit tests files
│   ├── __init__.py
|   └── unit
│       ├── __init__.py
│       ├── test_main.py
│       ├── test_bigquery.py
│       ├── test_logger_handler.py
│       └── test_response.py
├── requirements.txt
├── test_requirements.txt
└── README.md
```

# Test using command terminal
- **Command:** gcloud functions call assessment_ny_cabs
