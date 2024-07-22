# MLOps-Bootcamp-team10

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

Hotel booking demand analysis



# Step-by-Step Guide to Setup

## 1. Install Conda
If you haven't already installed Conda, you can download and install Miniconda (a minimal Conda installer) or Anaconda (which includes more packages by default):

- **Miniconda (Recommended for most users):**
  
  Download Miniconda from the official website: [Miniconda Installation](https://docs.conda.io/en/latest/miniconda.html).

  Follow the installation instructions for your operating system.

- **Anaconda:**
  
  Download Anaconda from the official website: [Anaconda Installation](https://www.anaconda.com/products/individual).

  Follow the installation instructions for your operating system.

Now you have Conda installed and ready to use. You can create environments, install packages, and manage your Python projects efficiently.



## 2. Create a New Conda Environment
Once Conda is installed, you can create a Conda environment specifically for this project. This helps isolate project dependencies from other projects on your system:

- **Create the Environment:**

   This will create the environment using `environment.yml` file:
   ```bash
   make create_environment     
   ```


- **Activate the Environment:**

   Activate the newly created environment:
   ```bash
   conda activate mlops-bootcamp-team10
   ```

Now, your terminal prompt should indicate that you are working within the `mmlops-bootcamp-team10` environment.


## 3. Install Packages
Now that your environment is active, you can start installing packages required for your project.  All you need to do is update the contents of your `environment.yml` file accordingly and then run the following command:

```bash
make requirements
```



## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for mlops_bootcamp_team10
│                         and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── mlops_bootcamp_team10                <- Source code for use in this project.
    │
    ├── __init__.py    <- Makes mlops_bootcamp_team10 a Python module
    │
    ├── data           <- Scripts to download or generate data
    │   └── make_dataset.py
    │
    ├── features       <- Scripts to turn raw data into features for modeling
    │   └── build_features.py
    │
    ├── models         <- Scripts to train models and then use trained models to make
    │   │                 predictions
    │   ├── predict_model.py
    │   └── train_model.py
    │
    └── visualization  <- Scripts to create exploratory and results oriented visualizations
        └── visualize.py
```

--------