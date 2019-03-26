import json
from statistics import median, mean, mode
from numpy import histogram

responses = [
    [
        ["1", 44],
        ["2", "max"]
    ],
    [
        ["1", 77],
        ["2", "biscuit"]
    ],
    [
        ["1", 98],
        ["2", "cheddar"]
    ],
    [
        ["1", 3],
        ["2", "marie"]
    ],
    [
        ["1", 15],
        ["2", "lisa"]
    ],
    [
        ["1", 77],
        ["2", "sam"]
    ],
    [
        ["1", 82],
        ["2", "billy"]
    ]
]


def calculated_data(survey_responses):
    data_set = []

    for response in survey_responses:
        data_point = response[0][1]
        data_set.append(data_point)

    hist = []
    bin_val = 0
    for d in histogram(data_set)[0]:
        arr = [bin_val, bin_val+10, int(d)]
        bin_val += 10
        hist.append(arr)

    data = {
        'count': len(data_set),
        'min': min(data_set),
        'max': max(data_set),
        'sum': sum(data_set),
        'mean': mean(data_set),
        'median': median(data_set),
        'mode': mode(data_set),
        'histogram': hist
    }
    json_res = json.dumps(data)
    return json_res


print(calculated_data(responses))
