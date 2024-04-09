# 1.086 Wake modeling demonstration using FLORIS

[FLORIS](https://www.nrel.gov/wind/floris.html) is a tool developed by NREL to compute wake losses. 
Here, we work through several examples in a Jupyter notebook on how to get started using FLORIS. 
You can find the notebook [here](https://github.com/kirbyh/1.086_wake_demo/blob/main/src/example.ipynb). 

## Installation instructions: 
### Using Poetry
```
git clone git@github.com:jaimeliew1/unified-momentum-reviewer-response.git
cd unified-momentum-reviewer-response
poetry install
```

## Run instructions
### Using GitHub codespaces
Poetry should auto-install all of the required packages. 
To run a script, type 
`poetry run python <script.py>`

To run a notebook, change the kernel to the python installation thru poetry (something like `1-086-wake-demo-...`)
