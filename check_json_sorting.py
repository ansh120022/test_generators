import json

def is_sorted_by_field(json_list, field, descending):
    for i in range(1, len(json_list)):
        if descending:
            if json_list[i - 1][field] < json_list[i][field]:
                return False
        else:
            if json_list[i - 1][field] > json_list[i][field]:
                return False
    return True

# Sample JSON data
json_data = '''
{
  "category": "dsp_id",
  "currency": "USD",
  "data": [
    {
      "recommendation": 20056200,
      "filtering_rate": 0.8071,
      "imps": 632,
      "reduced_imps": 0.2518,
      "media_cost": 7.18,
      "reduced_media_cost": 0.1975,
      "category_value": "37921"
    },
    {
      "recommendation": 34110000,
      "filtering_rate": 0.8038,
      "imps": 690,
      "reduced_imps": -0.0049,
      "media_cost": 26.37,
      "reduced_media_cost": 0.0583,
      "category_value": "951"
    },
    {
      "recommendation": 84700200,
      "filtering_rate": -0.0064,
      "imps": 73199,
      "reduced_imps": -0.02,
      "media_cost": 978.32,
      "reduced_media_cost": -0.0059,
      "category_value": "892"
    }
  ],
  "total": {
    "recommendation": 1983568500,
    "filtering_rate": 0.5054,
    "imps": 600010,
    "reduced_imps": 0.0163,
    "media_cost": 4695.34,
    "reduced_media_cost": 0.0039
  }
}
'''

# Parse the JSON data
parsed_data = json.loads(json_data)

# Extract the "data" field
data_list = parsed_data["data"]

# Check if the list is sorted by the "filtering_rate" field in descending order
is_sorted = is_sorted_by_field(data_list, "filtering_rate", descending=True)
print("Is the list sorted by 'filtering_rate' field (descending)?", is_sorted)
