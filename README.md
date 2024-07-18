# MLOps-Bootcamp-team10

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

Hotel booking demand analysis

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

## Setup

To install Conda, you can choose between two primary distributions: Anaconda and Miniconda. Here are the steps for installing each:

### 1. **Installing Anaconda**

Anaconda is a comprehensive distribution that includes Conda, Python, and many pre-installed packages for data science and machine learning.

#### **Windows, macOS, and Linux**

1. **Download Anaconda:**
   - Go to the [Anaconda Distribution](https://www.anaconda.com/products/distribution#download-section) download page.
   - Select your operating system (Windows, macOS, or Linux).
   - Download the installer for Python 3.x.

2. **Run the Installer:**
   - **Windows:** Double-click the downloaded `.exe` file and follow the installation instructions.
   - **macOS:** Open the downloaded `.pkg` file and follow the installation instructions.
   - **Linux:** Open a terminal, navigate to the directory containing the downloaded `.sh` file, and run:
     ```bash
     bash Anaconda3-2023.03-Linux-x86_64.sh
     ```
   - Follow the on-screen instructions to complete the installation.

3. **Verify Installation:**
   - Open a new terminal (or Anaconda Prompt on Windows) and run:
     ```bash
     conda --version
     ```
   - This should display the Conda version, confirming the installation was successful.

### Post-Installation Steps

1. **Initialize Conda (if needed):**
   - On some systems, you may need to initialize Conda to set up the necessary shell configuration. Run:
     ```bash
     conda init
     ```
   - Restart your terminal or run `source ~/.bashrc` (or equivalent for your shell) to apply the changes.

2. **Update Conda:**
   - It’s a good practice to update Conda to the latest version:
     ```bash
     conda update conda
     ```

Now you have Conda installed and ready to use. You can create environments, install packages, and manage your Python projects efficiently.

## Install dependencies

To install dependencies using Conda with the `environment.yml` file, follow these steps:

### 1. **Create the Conda Environment**

Use the `conda env create` command to create the environment from the `environment.yml` file. Open your terminal or command prompt, navigate to the directory containing the `environment.yml` file, and run:

```bash
conda env create -f environment.yml
```

### 2. **Activate the Conda Environment**

After creating the environment, activate it with the `conda activate` command:

```bash
conda activate mlops-bootcamp-team10
```

### 3. **Verify the Environment**

To ensure that the environment was created correctly with all specified dependencies, you can list the installed packages:

```bash
conda list
```

### Updating an Existing Environment

If you need to update an existing environment with new dependencies specified in an updated `environment.yml` file, use:

```bash
conda env update -f environment.yml
```

By following these steps, you can efficiently manage your Conda environments and ensure all necessary dependencies are installed as specified.