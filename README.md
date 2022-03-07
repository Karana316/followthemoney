## Install
```pip install``` 

## Use
Create a .env file with the api key, or set it as an environment variable
```APIKEY=###yourapikeyhere###```

Import the module, instantiate class
```followthemoneyapi.followthemoney import FollowTheMoney

myquery = FollowTheMoney()
```

### Filtering
Add filters if you wish, a list of all filters can be found in the literals file
```
myquery.add_filters(Election_Year=2021)
```

### Grouping
Get data by a grouping (if filters added, they will be used)
Inputs are in the form Category=['Group1','Group2']
```
myquery.get_data_by_groupings(General=['Election_Year'], Advanced=['Type_of_Transaction'])
```

### Final URL
If you want to see the final url called
```print(myquery._url())```