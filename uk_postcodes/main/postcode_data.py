import pandas as pd

class PostcodeData:
    def __init__(self, file_path):
        self.data = pd.read_csv(file_path)
        self.postcode_info = self.data.set_index('postcode').to_dict('index')

    def get_postcode_info(self, postcode):
        return self.postcode_info.get(postcode)

# Example usage:
# postcode_data = PostcodeData('path_to_your_csv_file.csv')
# info = postcode_data.get_postcode_info('AB1 0AA')
