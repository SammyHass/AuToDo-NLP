
# Task Classification

tasks will be categorised by an NLP model to allows the user to concerntrate on their work.


## Installation

1. Please ensure that you have [Git CLI](https://git-scm.com) installed. You can do this by opening a terminal/powershell window and typing ```git --version```. If you are shown a version number, you have installed git correctly. If you recieve an error, you must download it, ensuring that there is no traces of a past git installation on your machine.

2. Once you are certain you have git installed, please use the cd (change dir) and mkdir (make dir) commands in order to get yourself into the location you would like the code we will downlaod to be in.

For Example I went into the Documents folder and made a new folder called project_files where I can store my code:

```bash
	cd ~/Documents
	mkdir project_files
	cd project_files/
```  

3. We will now download the code onto our machine. We will do this with *git clone* which allows us to copy a repository over to our computer from a server. 

```bash
git clone https://gitlab.com/Task_Management_CompSci/task_classifier.git
```

This creates a folder within the project_files directory. This new folder is populated with the code we want to execute and is called 'task_classifier'.

Now, change into the this folder.

```bash
cd task_classifier/
```

4. Please ensure that you have Python 3.4 or higher installed as well as the Pip package manager. You can check these are installed correctly by running:

```bash
python --version
pip --version
```

5. Install the dependencies needed to make the project work.

```bash
pip install -r requirements.txt
```

## Running 

* **add_to_csv.py**
```bash
python add_to_csv.py
```

* **classifier.ipynb**
```bash
jupyter notebook
```
This will run the application on localhost:8888. Type this into your browser and the notebook will open. To run each cell in this notebook, you can press ```SHIFT + ENTER```.






