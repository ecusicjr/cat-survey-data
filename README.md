# cat-survey-data
A simple aggregation of data from a sample cat survey (coding exercise).
#
To install and run:

(Recommended) Create a virtualenv (install this pip package if needed)
```
virtualenv venv
```
Activate the venv (Windows):
```
source venv/Scripts/activate
```
Activate the venv (Mac/Unix):
```
source venv/bin/activate
```
#

Install:
```
pip install -r requirements.txt
```
#
Run:
```
python cat_survey_data.py
```
#
Sample input used in this exercise: 

```python
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
```
#
Expected output (dict):

```python
{
  'count': 7,
  'min': 3,
  'max': 98,
  'sum': 396,
  'mean': 56.57142857142857,
  'median': 77,
  'mode': 77,
  'histogram': [
    [0, 10, 1],
    [10, 20, 1],
    [20, 30, 0],
    [30, 40, 0],
    [40, 50, 1],
    [50, 60, 0],
    [60, 70, 0],
    [70, 80, 2],
    [80, 90, 1],
    [90, 100, 1]
  ]
}
```