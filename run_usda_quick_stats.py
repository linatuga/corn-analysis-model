from c_usda_quick_stats import c_usda_quick_stats
import urllib.parse

# Create an instance of the c_usda_quick_stats class. Call it with search parameters
# and the output file to write the returned CSV data into.

parameters =    'source_desc=SURVEY' +  \
                '&' + urllib.parse.quote('sector_desc=FARMS & LANDS & ASSETS') + \
                '&' + urllib.parse.quote('commodity_desc=FARM OPERATIONS') + \
                '&' + urllib.parse.quote('statisticcat_desc=AREA OPERATED') + \
                '&unit_desc=ACRES' + \
                '&freq_desc=ANNUAL' + \
                '&reference_period_desc=YEAR' + \
                '&year__GE=1997' + \
                '&agg_level_desc=NATIONAL' + \
                '&' + urllib.parse.quote('state_name=US TOTAL') + \
                '&format=CSV'

stats = c_usda_quick_stats()

s_json = stats.get_data(parameters, 'national_farm_survey_acres_ge_1997')