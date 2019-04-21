# portfolio-backend
Backend for portfolio related functionality

## Installation

**Clone the project**
``` bash
git clone https://github.com/agapanto/portfolio-backend
```

**Create a virtualenv with python3**
``` bash
mkvirtualenv portfolio-backend  --python=$(which python3)
```

**Install the required packages**
``` bash
pip install -r requirements.txt
```

**Set all required env vars:** You can execute the following `cp` command or set the env vars by yout own(with an `export` command).
``` bash
cp .env.dist .env
```

**Run the app with honcho:** This is a Procfile based project so you can start all the workers with the following command
``` bash
honcho start
```
