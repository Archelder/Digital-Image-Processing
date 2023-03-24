# A Simple Technical Guidance for DIP

<center>This article has been updated, bearing the date of 2023MAY20, by Kilo A. FENG</center>

[toc]

## Language for Coding

### Python

*Python* and *MATLAB* are both of use to finish assignments of this course, however, we recommend *Python* strongly due to its stability. It is quite easy to install, anyone with grade 2 primary education could find multiple approaches via the Internet, which shall not be mentioned in this guidance.

#### Packges Management Tools

Inevitable it is to install various packages for using *python* to handle things with complexity. However, the installation of various packages might be **a little bit annoying**. Packages management tools is likely to make the process of installation simpler. We recommend *Anaconda* and *pip* to manage packages.

##### A. Anaconda/Miniforge (conda)

*Anaconda* is a famous commercial application for virtual environments management as well as packges management, which can provide a GUI. Due to its commercial attribute, we recommend ***miniforge*** as an alternative, which provide quite similar functions and commands but maintained by an open source community rather than a commercial corporation. However, *minidorge* do not offer a GUI, which is not necessary for the strong.

###### Installation

It is as easy as doing mathematics in grade 2  to download the latest release of *miniforge* via NJU’s site.
Click the URL: https://mirror.nju.edu.cn/github-release/conda-forge/miniforge/LatestRelease/

###### Configuration

We strongly recommend any domestic user to switch the default channel of *conda* to a domestic mirror for the purpose of getting a higher access speed. One way to switch to USTC Mirror is shown below, readers may switch to other domestic mirrors such as THU Mirror, NJU Mirror and Ali Mirror, et cetera, whose URL can be found via the Internet easily.

Execute the following commands line by line in your command line interface (shell/terminal/cmd...)

```
conda config --set show_channel_urls yes
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/main/
```

##### B. Pip

*Pip* is a famous packges management tool which enables users to search, install and uninstall various python packages. **Before heading to the installation**, we would like to mention which is often the case is that  *pip* might have been already installed along with the installing process of  *python*. 

Use the commands below to check whether *pip* is intalled or not.

```
pip --version
```

One more possible command:

```
pip3 --version
```

If the prompts suggest that *pip* can not be found, consider checking whether the path of *python* is added to the **environment variables**. Find more details about how to check and edit the environment variables via the Internet, this article will not dig in.

###### Installation 

1. The latest release of *pip* can be found on its official site. Click the URL: https://pypi.org/project/pip/
2. After downloading, unzip the files.
3. Use commands below to enter the directory of the unzipped files. 
   (Replace “directory of files” with its real directory, and do retain the quotation marks.)

```
cd "directory of files"
# an example:
# cd "C:\desktop\pip-22.0.4"
```

4. Execute commands below to start the installation.

   ```
   python setup.py install
   ```

###### Configuration

We strongly recommend any domestic user to switch the default channel of *pip* to a domestic mirror for the same reason as for *conda*. One way to switch to USTC Mirror is shown below.

Execute the following commands line by line.

```
pip install -i https://mirrors.ustc.edu.cn/pypi/web/simple pip -U
pip config set global.index-url https://mirrors.ustc.edu.cn/pypi/web/simple
```

#### Necessary Packages

The following packages is quite necessary for whom using *python* to handle DIP, which we are going to list  and explain the use.

##### A. OpenCV

*OpenCV* is a computer vision and machine learning software library, which may help users with images processing.

###### Installation

1. *OpenCV* can be installed via ***conda*** or ***pip***, using the following commands. (Activate the corresponding environments before running the commands, unless it is going to be installed in the *base* environment.)
   **Conda**

   ```
   conda install opencv
   ```

   **Pip**

   ```
   pip install opencv
   ```

2. Install *OpenCV-Python*, using the following commands. Make sure it is installed in the same environment with *OpenCV*.

   ```
   pip install opencv-python
   ```

###### Using

Import *OpenCV* in *Python* as shown below.

```python
import cv2
```

##### B. NumPy

*NumPy* is a scientific computing library which can be used to store and process large matrixes efficiently.

###### Installation

- *NumPy* can be installed via ***conda*** or ***pip***, using the following commands. (Activate the corresponding environments before running the commands, unless it is going to be installed in the *base* environment.)
  **Conda**

   ```
   conda install numpy
   ```
   **Pip**
  
   ```
   pip install numpy
   ```

###### Using

Import *NumPy* in *Python* as shown below.

```python
import numpy
```

For most of the time, *NumPy* is imported as shown below for handy.

```python
import numpy as np
```

##### C. Matplotlib

*Matplotlib* is a comprehensive library for creating static, animated, andinteractive visualizations in *Python*.

###### Installation 

- *Matplotlib* can be installed via ***conda*** or ***pip***, using the following commands. (Activate the corresponding environments before running the commands, unless it is going to be installed in the *base* environment.)

  **Conda**

   ```
   conda install matplotlib
   ```
   **Pip**

   ```
   pip install matplotlib
   ```

###### Using

Import *Matplotlib* in *Python* as shown below.

```python
import matplotlib
```

For most of the time, *NumPy* is imported as shown below for handy, since it is often the case that only the function *matplotlib.pyplot()* is used.

```python
import matplotlib.pyplot as plot
```

### Markdown

*Markdown* is a kind of simplified *HTML*, whose grammars are as simple as the mathematics in grade 2. As readers can see, this article is written using *markdown*. For finishing the course assignments, only a little bit of grammars will be involved.

Learn more via https://blog.csdn.net/qq_40818172/article/details/126260661

### LaTeX

*LaTeX* is a typesetting system based on ΤΕΧ, which enables users to edit mathematical formula easily. For finishing the course assignments, only a little bit of grammars will be involved. Here some example is given.

**Fractions**

1. Fraction as $\frac{n}{m}$ 

```latex
\frac{n}{m}
```

2. Fraction as $\dfrac{a}{b}$

```latex
\dfrac{a}{b}
```

**Greek Letters**

1. Capital greek letters as $\Alpha,\Beta,\Pi,\Mu,\Sigma$

```
\Alpha,\Beta,\Pi,\Mu,\Sigma
```

2. Lower-case greek letters as $\alpha,\beta,\pi,\mu,\sigma$

```
\alpha,\beta,\pi,\mu,\sigma
```

**Operators**

1. Multiplication sign as $2 \times 3$

```latex
2 \times 3
```

2. Division sing as $4 \div 5$

```latex
4 \div 5
```

More information can be found on the Internet easily.

## Applications for Coding 

### PyCharm

*PyCharm* is an IDE for *Python* programming. Download from its official website (https://www.jetbrains.com/zh-cn/pycharm/). College students could apply for free license to use the professional edition, following instructions on the website.

### JupytrLab

*JupyterLab* enables users to create and edit *Jupyter Notbook*, which is demanded to be used when completing the assignments.

#### Installation

Install *JupyterLab* with *pip*.

```
pip install jupyterlab
```

#### Using 

Launch *JupyterLab* using following commands in command line interface. (Activate the corresponding environments before running the commands.)

```
jupyter-lab
```

