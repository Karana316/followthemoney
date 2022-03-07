from followthemoney.followthemoney import FollowTheMoney

myquery = FollowTheMoney()
myquery.add_filters(Election_Year=2021)
print(myquery._url())
df = myquery.get_data_by_groupings(General=['Filing_State'])

# in noteboook
# df.head()
print(df.head())

# get a specific entity, this will just be a total because I added no groupings
# could build out more specific calls like this rather than having to do filters + groupings each time
myquery2 = FollowTheMoney()
df = myquery2.get_entity(330788)
print(df.head())