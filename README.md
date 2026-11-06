# Abdominal Aortic Aneurysm Dataset

Tabular abdominal aortic aneurysm (AAA) dataset with **400 records**, **11 features**, and a binary `Target` column.

## Repository structure

```text
aaa_data/
├── data_full.xls        # Dataset: Sheet1, 400 rows × 12 columns
├── load_data.py         # Load and summarize the dataset
├── requirements.txt    # Reading dependencies
├── citation.bib        # Repository citation
├── LICENSE             # Apache License 2.0
└── README.md
```

## Quick start

```bash
git clone https://github.com/iliaohai/aaa_data.git
cd aaa_data
python -m pip install -r requirements.txt
python load_data.py
```

Expected summary:

```text
Records: 400
Features: 11
Blank cells: 0
Target counts: {0: 200, 1: 200}
X shape: (400, 11)
y shape: (400,)
```

To load the data in your own code:

```python
import pandas as pd

df = pd.read_excel("data_full.xls", sheet_name="Sheet1", engine="xlrd")
X = df.drop(columns="Target")
y = df["Target"]
```

## Columns

| Column | Description |
|---|---|
| `Age` | Age |
| `Sex` | Sex code (0/1) |
| `Drinking` | Drinking code (0/1) |
| `Smoking` | Smoking code (0/1) |
| `BP` | Blood pressure |
| `TG` | Triglycerides |
| `LDL-C` | Low-density lipoprotein cholesterol |
| `Glu` | Glucose |
| `BMI` | Body mass index |
| `Hcy` | Homocysteine |
| `UA` | Uric acid |
| `Target` | Binary label: 200 records per class |

Units, categorical code meanings, and the clinical definition of `Target` are not documented in the source workbook. Confirm these before interpreting results. This repository provides data; it does not include a trained model or a paper-reproduction pipeline.

## Citation

```bibtex
@misc{iliaohai_aaa_data,
  author       = {{iliaohai}},
  title        = {Abdominal Aortic Aneurysm Dataset},
  howpublished = {GitHub repository},
  url          = {https://github.com/iliaohai/aaa_data},
  note         = {Accessed: 2026-11-06}
}
```

## License

See [LICENSE](LICENSE) (Apache License 2.0).
