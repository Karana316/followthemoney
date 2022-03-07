GROUPS = {
    'General': {
         'Election_State': 's',
         'Election_Year': 'y',
         'Filing_State': 'f-s',
         'Filer': 'f-eid',
         'Candidate': 'c-t-id',
         'Ballot_Measure_Committee': 'm-t-eid"',
         'Party_Committee': 'pt-eid',
         'Spender': 'is-f-eid'
     },
    'Advanced': {
        'Filing_Year': 'f-y',
        'Office_Sought': 'c-r-osid',
        'Office': 'c-r-oc',
        'Incumbency_Data': 'c-t-i',
        'Incumbency_Advantage': 'c-t-icod',
        'Original_Name': 'd-nme',
        'Amount': 'd-amt',
        'Date': 'd-dte',
        'Last_Updated': 'd-ludte',
        'Type_of_Transaction': 'd-typ',
        'Street': 'd-ad-str',
        'Latitude': 'd-ad-lat',
        'Longitude': 'd-ad-long',
        'DND': 'd-search',
        'DND': 'empl-search',
        'DND': 'd-file',
        'Lobbying Entity': 'd-llink'
    },
    'Candidates': {
        'Candidate': 'c-t-id',
        'General_Party': 'c-t-p',
        'Status_of_Candidate': 'c-t-sts',
        'Specific_Party': 'c-t-pt',
        'Career_Summary': 'c-t-eid',
        'Specific_Office': 'c-r-id',
        'Election_Type': 'c-r-t',
        'General_Office': 'c-r-ot',
        'Status_of_Candidate': 'c-t-sts',
        'Incumbency_Status': 'c-t-ico'

    },
    'Party Committees': {
        'Party': 'pt-p',
        'Committee Type': 'pt-typ'
    },
    'Contributors': {
        'Record': 'd-id',
        'Contributor': 'd-eid',
        'Type_of_Contributor': 'd-et',
        'Specific_Business': 'd-ccb',
        'General_Industry': 'd-cci',
        'Broad_Sector': 'd-ccg',
        'Parent_Org_or_Employer': 'd-par',
        'City': 'd-ad-cty',
        'State': 'd-ad-st',
        'Zip': 'd-ad-zip',
        'In-State': 'd-ins',
        'Employer': 'd-empl',
        'Occupation': 'd-occupation'
    },
    'Spender': {
        'Spender_Sector': 'cis-f-ccg',
        'Spender_Industry': 'cis-f-cci',
        'Spender_Business Classification': 'cis-f-ccb',
        'Type_of_Spender': 'cis-et'
    },
    'Lawmakers': {
        'Law_Officeholder': 'law-eid',
        'Law_Office_Held': 'law-did',
        'Law_Type_of_Office': 'law-oc',
        'Law_General_Office': 'law-ot',
        'Law_Specific_Party': 'law-pt',
        'Law_General_Party': 'law-p',
        'Law_Officeholder_Jurisdiction': 'law-s',
        'Law_Officeholder_Year': 'law-y'
    }
}

TOKENS = {}
for token_dict in list(map(lambda x: GROUPS[x], GROUPS.keys())):
    TOKENS = {**TOKENS, **token_dict}

GROUPING_CONFLICTS = {
    's': ['f-s'],
    'y': ['f-y'],
    'f-s': ['s'],
    'f-y': ['y'],
    'c-r-oc': ['c-r-ot'],
    'c-t-id': ['s', 'y', 'c-r-osid', 'c-t-pt', 'c-t-eid', 'c-r-id', 'c-t-ico'],
    'c-t-p': ['c-t-pt'],
    'c-t-pt': ['c-t-p'],
    'c-r-id': ['s', 'y', 'c-r-osid'],
    'd-eid': ['d-et'],
    'd-et': ['d-eid'],
    'd-ccb': ['d-cci', 'd-ccg'],
    'd-cci': ['d-ccg']
}

FILTER_CONFLICTS = {
    's': ['f-s'],
    'y': ['f-y'],
    'f-s': ['s'],
    'f-y': ['y'],
    'c-r-oc': ['c-r-ot'],
    'c-t-id': ['s', 'y', 'c-r-osid', 'c-t-pt', 'c-t-eid', 'c-r-id', 'c-t-ico'],
    'c-t-p': ['c-t-pt'],
    'c-t-pt': ['c-t-p'],
    'c-r-id': ['s', 'y', 'c-r-osid'],
    'd-eid': ['d-et'],
    'd-et': ['d-eid']
}
