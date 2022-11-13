import urllib.parse
import urllib.request
from requests.utils import requote_uri
import ssl

# Create an instance of the c_usda_quick_stats class. Call it with search parameters
# and the output file to write the returned CSV data into.


class c_usda_quick_stats:

    def __init__(self):

        # Set the USDA QuickStats API key, API base URL, and output file path where CSV files will be written. 

        self.api_key = '04B486D3-02D1-39C8-9FB5-BF3CD314CE87'

        self.base_url_api_get = 'http://quickstats.nass.usda.gov/api/api_GET/?key=' + self.api_key + '&'

        self.output_file_path = r'usda_quick_stats_files'

    def get_data(self, parameters, file_name):

        # Call the api_GET api with the specified parameters. 
        # Write the CSV data to the specified output file.

        # Create the full URL and retrieve the data from the Quick Stats server.
        
        full_url = self.base_url_api_get + parameters
        s_result = urllib.request.urlopen(full_url)
        s_text = s_result.read().decode('utf-8')

        # Create the output file and write the CSV data records to the file.

        s_file_name = self.output_file_path + file_name + ".csv"
        o_file = open(s_file_name, "w", encoding="utf8")
        o_file.write(s_text)
        o_file.close()


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
