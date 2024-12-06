# Airbnb ETL Project

### project Setup:

1.  Create a new project directory

```
   mkdir airbnb_etl
```

2.  Navigate to the folder

```
   cd airbnb_etl
```

3.  Create a New Virtual Environment

```
  python -m venv abvenv
```

4.  Activate the virtual environment

- Mac

```
  source/abvenv/activate
```

- Windows

```
  cd abvenv/Scripts/activate
```

5. Create a following files into src <br>
   | FILES | Descriptions |
   |-------|--------------|
   | AIRBNB_ETL / src | Root directory which contains the code base |
   | AIRBNB_ETL / .gitignore | Contains files to get ignore / sensitive to share |
   | AIRBNB_ETL / README.md | Project Documentation file |
   | AIRBNB_ETL / LICENSE | Contains permissions, Limitations and Conditions of the project |
   | src / abvenv | Contains all the dependencies of the virtual environment |
   | src / .env | Contains all the credentials that are used in the code base |
   | src / data_extract.py | Contains code for data extraction |
   | src / etl_pipeline.py | Contains code for ETL pipeline |
   | src / test_extract.py | Contains code to test data extraction scripts |
   | src / transformations.py | Contains code for data transformations |

6. Run the project code

```python

   python <file_name.py>
```
