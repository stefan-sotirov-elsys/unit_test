import requests

class Temperature:

    temp_list = []

    def __init__(self, url):
        
        data = requests.post(url).json()["data"]

        sorted_data = sorted(data, key = lambda d: d["temperature"])

        data_len = len(data)

        for i in range(0, data_len):

            self.temp_list.append(sorted_data[i].get("temperature"))

    def min_temp_read(self):

        return self.temp_list[0]

    def max_temp_read(self):

        return self.temp_list[len(self.temp_list) - 1]

    def avg_temp_read(self):

        return sum(self.temp_list) / len(self.temp_list)