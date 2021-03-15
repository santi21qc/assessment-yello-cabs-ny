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
- **Data**: 500k records

![command-example](https://github.com/santi21qc/assessment-yello-cabs-ny/blob/develop/images/terminal-example.gif)
- **output:** 
```
[
   {
      "passengerCount":1,
      "totalTimeMinutes":19662,
      "numberOfTrips":1114,
      "numberOfCabsRequired":2
   },
   {
      "passengerCount":2,
      "totalTimeMinutes":3476,
      "numberOfTrips":223,
      "numberOfCabsRequired":2
   },
   {
      "passengerCount":3,
      "totalTimeMinutes":1292,
      "numberOfTrips":61,
      "numberOfCabsRequired":2
   },
   {
      "passengerCount":4,
      "totalTimeMinutes":568,
      "numberOfTrips":33,
      "numberOfCabsRequired":2
   },
   {
      "passengerCount":5,
      "totalTimeMinutes":1210,
      "numberOfTrips":74,
      "numberOfCabsRequired":1
   },
   {
      "passengerCount":6,
      "totalTimeMinutes":810,
      "numberOfTrips":47,
      "numberOfCabsRequired":1
   }
]

```

# Test in Google Cloud Function
- **Function name:** assessment_ny_cabs
- **Data**: 500k records

![command-example](https://github.com/santi21qc/assessment-yello-cabs-ny/blob/develop/images/function_test-example.gif)

- **output:**
```
[
   {
      "passengerCount":1,
      "totalTimeMinutes":19662,
      "numberOfTrips":1114,
      "numberOfCabsRequired":2
   },
   {
      "passengerCount":2,
      "totalTimeMinutes":3476,
      "numberOfTrips":223,
      "numberOfCabsRequired":2
   },
   {
      "passengerCount":3,
      "totalTimeMinutes":1292,
      "numberOfTrips":61,
      "numberOfCabsRequired":2
   },
   {
      "passengerCount":4,
      "totalTimeMinutes":568,
      "numberOfTrips":33,
      "numberOfCabsRequired":2
   },
   {
      "passengerCount":5,
      "totalTimeMinutes":1210,
      "numberOfTrips":74,
      "numberOfCabsRequired":1
   },
   {
      "passengerCount":6,
      "totalTimeMinutes":810,
      "numberOfTrips":47,
      "numberOfCabsRequired":1
   }
]

```
