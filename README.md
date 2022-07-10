# Reverse k Nearest Neighbor Graph


## Problem Statement

<img src="http://www.sciweavers.org/tex2img.php?eq=kNN_%7Bk%7D%20%5Cbig%28q%5Cbig%29%20%3D%20%20%5Cbig%5C%7Bo%20%5Cin%20D%20%7C%20d%20%5Cbig%28q%2Co%5Cbig%29%20%20%3C%20d%20%5Cbig%28q%2C%5Chat%7Bo%7D%5Cbig%29%20%5Cforall%20%20%5Chat%7Bo%7D%20%20%5Cin%20D%20%20%5Cbig%5C%7D%20%20&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="kNN_{k} \big(q\big) =  \big\{o \in D | d \big(q,o\big)  < d \big(q,\hat{o}\big) \forall  \hat{o}  \in D  \big\}  " width="347" height="24" />



<img src="http://www.sciweavers.org/tex2img.php?eq=RkNN_%7Bk%7D%20%5Cbig%28q%5Cbig%29%20%3D%20%20%5Cbig%5C%7Bp%20%5Cin%20D%20%7C%20q%20%20%5Cin%20kNN_%7Bk%7D%28p%29%5Cbig%5C%7D%20%20&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="RkNN_{k} \big(q\big) =  \big\{p \in D | q  \in kNN_{k}(p)\big\}  " width="272" height="24" />


Paper Link: [Click Here](https://link.springer.com/article/10.1007/s10586-020-03136-9)

## Content

This repository contains the source code.

  * `ODRA.py`: This python file gives only the source code for ODRA.
  
# Instructions
The program is written in Python 3.8:
* Using conda:
```
conda install -c conda-forge jupyterlab
```
* using pip:
```
pip install jupyterlab
```
* Download Python: [Click Here](https://www.python.org/downloads/)

## Dependencies
The program requires the following Python libraries:
* numpy v1.21.5
* scikit-learn v1.0.1
* pandas v1.3.4
* scipy v1.7.3

# Contributors

* Kushankur Ghosh, [kushanku@ualberta.ca](mailto:kushanku@ualberta.ca)

