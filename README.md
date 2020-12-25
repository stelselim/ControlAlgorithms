# Welcome To Control Algorithms

<p/>

### This is a Control Engineering Algorithms Repo <a href="https://github.com/stelselim/ControlAlgorithms#-this-is-a-control-engineering-algorithms-repo"> For Documentation.</a>
<p> In the project, the control algorithms in Python is working on Google Cloud App Engine. The objective of the project is that making a really simple API in order to analyze a system in transfer function form (Hopefully, will be implemented StateSpace model). </p>
<p>It's so simplified to see control functions, such as step response, stepinfo, bodeplot and much more. All API's are designed to take URL Parameters as an input. Accordingly, you to use GET requests without needing anything else. </p>  

<br>



### Contact
Maintainer: Selim Üstel<br/>
<ul>
  <li> <a href="https://stelselim.github.io"> Website</a> </li>
  <li> <a href="https://www.linkedin.com/in/selimustel/"> Linkedin</a> </li>
  <li> <a href="https://github.com/stelselim"> Github</a> </li>
</ul>




### Currently, available features:
* <a href="https://github.com/stelselim/ControlAlgorithms#stepresponse"> stepresponse </a>
* <a href="https://github.com/stelselim/ControlAlgorithms#stepinfo"> stepinfo </a>
* <a href="https://github.com/stelselim/ControlAlgorithms#rampresponse"> rampresponse </a>
* <a href="https://github.com/stelselim/ControlAlgorithms#impulseresponse"> impulseresponse </a>
* <a href="https://github.com/stelselim/ControlAlgorithms#bodeplot"> bodeplot </a>
* <a href="https://github.com/stelselim/ControlAlgorithms#nyquistplot"> nyquistplot </a>
* <a href="https://github.com/stelselim/ControlAlgorithms#rlocusplot"> rlocusplot </a>
* <a href="https://github.com/stelselim/ControlAlgorithms#closedloopunitfeedback"> closedloop/unitfeedback </a>


<br/>

### How To Use

### stepresponse
<p> Required URL Parameters </p>
<p>
num: as a numerator of transfer function
</p>
<p>
den: as a denominator of transfer function
</p>


### Example - 1

transfer function 
<img src="https://github.com/stelselim/ControlAlgorithms/blob/master/tf1.png"/>

#### num=1   for 1

#### den=1,2   for s + 2

#### URL = https://controlalgo.ey.r.appspot.com/stepresponse?num=1&den=1,2


<br/>

### Example - 2

transfer function 
<img src="https://github.com/stelselim/ControlAlgorithms/blob/master/tf2.png"/>

#### num=1,2   for s + 2

#### den=1,5,2   for s^2 + 5*s + 2  

#### URL = https://controlalgo.ey.r.appspot.com/stepresponse?num=1,2&den=1,5,2

<br>

### Example - 3

transfer function 
<img src="https://github.com/stelselim/ControlAlgorithms/blob/master/tf3.png"/>

#### num=1,0,2   for s^2 + 2

#### den=2,0,5,2   for 2*s^3 + 5*s + 2  

#### URL = https://controlalgo.ey.r.appspot.com/stepresponse?num=1,0,2&den=2,0,5,2


<br/>


### stepinfo
<p> Required URL Parameters </p>
<p>
num: as a numerator of transfer function
</p>
<p>
den: as a denominator of transfer function
</p>


### Example - 1

transfer function 
<img src="https://github.com/stelselim/ControlAlgorithms/blob/master/tf1.png"/>

#### num=1   for 1

#### den=1,2   for s + 2

#### URL = https://controlalgo.ey.r.appspot.com/stepinfo?num=1&den=1,2


<br>

### Example - 2

transfer function 
<img src="https://github.com/stelselim/ControlAlgorithms/blob/master/tf2.png"/>

#### num=1,2   for s + 2

#### den=1,5,2   for s^2 + 5*s + 2  

#### URL = https://controlalgo.ey.r.appspot.com/stepinfo?num=1,2&den=1,5,2

<br>

### Example - 3

transfer function 
<img src="https://github.com/stelselim/ControlAlgorithms/blob/master/tf3.png"/>

#### num=1,0,2   for s^2 + 2

#### den=2,0,5,2   for 2*s^3 + 5*s + 2  

#### URL = https://controlalgo.ey.r.appspot.com/stepinfo?num=1,0,2&den=2,0,5,2



<br/>


### rampresponse
<p> Required URL Parameters </p>
<p>
num: as a numerator of transfer function
</p>
<p>
den: as a denominator of transfer function
</p>


### Example - 1

transfer function 
<img src="https://github.com/stelselim/ControlAlgorithms/blob/master/tf1.png"/>

#### num=1   for 1

#### den=1,2   for s + 2

#### URL = https://controlalgo.ey.r.appspot.com/rampresponse?num=1&den=1,2


<br>


### Example - 2

transfer function 
<img src="https://github.com/stelselim/ControlAlgorithms/blob/master/tf2.png"/>

#### num=1,2   for s + 2

#### den=1,5,2   for s^2 + 5*s + 2  

#### URL = https://controlalgo.ey.r.appspot.com/rampresponse?num=1,2&den=1,5,2

<br>

### Example - 3

transfer function 
<img src="https://github.com/stelselim/ControlAlgorithms/blob/master/tf3.png"/>

#### num=1,0,2   for s^2 + 2

#### den=2,0,5,2   for 2*s^3 + 5*s + 2  

#### URL = https://controlalgo.ey.r.appspot.com/rampresponse?num=1,0,2&den=2,0,5,2




### impulseresponse
<p> Required URL Parameters </p>
<p>
num: as a numerator of transfer function
</p>
<p>
den: as a denominator of transfer function
</p>


### Example - 1

transfer function 
<img src="https://github.com/stelselim/ControlAlgorithms/blob/master/tf1.png"/>

#### num=1   for 1

#### den=1,2   for s + 2

#### URL = https://controlalgo.ey.r.appspot.com/impulseresponse?num=1&den=1,2


<br>


### Example - 2

transfer function 
<img src="https://github.com/stelselim/ControlAlgorithms/blob/master/tf2.png"/>

#### num=1,2   for s + 2

#### den=1,5,2   for s^2 + 5*s + 2  

#### URL = https://controlalgo.ey.r.appspot.com/impulseresponse?num=1,2&den=1,5,2

<br>

### Example - 3

transfer function 
<img src="https://github.com/stelselim/ControlAlgorithms/blob/master/tf3.png"/>

#### num=1,0,2   for s^2 + 2

#### den=2,0,5,2   for 2*s^3 + 5*s + 2  

#### URL = https://controlalgo.ey.r.appspot.com/impulseresponse?num=1,0,2&den=2,0,5,2


<br>

### bodeplot
<p> Required URL Parameters </p>
<p>
num: as a numerator of transfer function
</p>
<p>
den: as a denominator of transfer function
</p>


### Example - 1

transfer function 
<img src="https://github.com/stelselim/ControlAlgorithms/blob/master/tf1.png"/>

#### num=1   for 1

#### den=1,2   for s + 2

#### URL = https://controlalgo.ey.r.appspot.com/bodeplot?num=1&den=1,2


<br>


### Example - 2

transfer function 
<img src="https://github.com/stelselim/ControlAlgorithms/blob/master/tf2.png"/>

#### num=1,2   for s + 2

#### den=1,5,2   for s^2 + 5*s + 2  

#### URL = https://controlalgo.ey.r.appspot.com/bodeplot?num=1,2&den=1,5,2

<br>

### Example - 3

transfer function 
<img src="https://github.com/stelselim/ControlAlgorithms/blob/master/tf3.png"/>

#### num=1,0,2   for s^2 + 2

#### den=2,0,5,2   for 2*s^3 + 5*s + 2  

#### URL = https://controlalgo.ey.r.appspot.com/bodeplot?num=1,0,2&den=2,0,5,2


<br>


### nyquistplot
<p> Required URL Parameters </p>
<p>
num: as a numerator of transfer function
</p>
<p>
den: as a denominator of transfer function
</p>


### Example - 1

transfer function 
<img src="https://github.com/stelselim/ControlAlgorithms/blob/master/tf1.png"/>

#### num=1   for 1

#### den=1,2   for s + 2

#### URL = https://controlalgo.ey.r.appspot.com/nyquistplot?num=1&den=1,2


<br>


### Example - 2

transfer function 
<img src="https://github.com/stelselim/ControlAlgorithms/blob/master/tf2.png"/>

#### num=1,2   for s + 2

#### den=1,5,2   for s^2 + 5*s + 2  

#### URL = https://controlalgo.ey.r.appspot.com/nyquistplot?num=1,2&den=1,5,2

<br>

### Example - 3

transfer function 
<img src="https://github.com/stelselim/ControlAlgorithms/blob/master/tf3.png"/>

#### num=1,0,2   for s^2 + 2

#### den=2,0,5,2   for 2*s^3 + 5*s + 2  

#### URL = https://controlalgo.ey.r.appspot.com/nyquistplot?num=1,0,2&den=2,0,5,2

<br>


### rlocusplot
<p> Required URL Parameters </p>
<p>
num: as a numerator of transfer function
</p>
<p>
den: as a denominator of transfer function
</p>


### Example - 1

transfer function 
<img src="https://github.com/stelselim/ControlAlgorithms/blob/master/tf1.png"/>

#### num=1   for 1

#### den=1,2   for s + 2

#### URL = https://controlalgo.ey.r.appspot.com/rlocusplot?num=1&den=1,2


<br>


### Example - 2

transfer function 
<img src="https://github.com/stelselim/ControlAlgorithms/blob/master/tf2.png"/>

#### num=1,2   for s + 2

#### den=1,5,2   for s^2 + 5*s + 2  

#### URL = https://controlalgo.ey.r.appspot.com/rlocusplot?num=1,2&den=1,5,2

<br>

### Example - 3

transfer function 
<img src="https://github.com/stelselim/ControlAlgorithms/blob/master/tf3.png"/>

#### num=1,0,2   for s^2 + 2

#### den=2,0,5,2   for 2*s^3 + 5*s + 2  

#### URL = https://controlalgo.ey.r.appspot.com/rlocusplot?num=1,0,2&den=2,0,5,2


<br>

### closedloop/unitfeedback
<p> Required URL Parameters </p>
<p>
num: as a numerator of transfer function
</p>
<p>
den: as a denominator of transfer function
</p>


### Example - 1

transfer function 
<img src="https://github.com/stelselim/ControlAlgorithms/blob/master/tf1.png"/>

#### num=1   for 1

#### den=1,2   for s + 2

#### URL = https://controlalgo.ey.r.appspot.com/closedloop/unitfeedback?num=1&den=1,2


<br>


### Example - 2

transfer function 
<img src="https://github.com/stelselim/ControlAlgorithms/blob/master/tf2.png"/>

#### num=1,2   for s + 2

#### den=1,5,2   for s^2 + 5*s + 2  

#### URL = https://controlalgo.ey.r.appspot.com/makeclosedloop?num=1,2&den=1,5,2

<br>

### Example - 3

transfer function 
<img src="https://github.com/stelselim/ControlAlgorithms/blob/master/tf3.png"/>

#### num=1,0,2   for s^2 + 2

#### den=2,0,5,2   for 2*s^3 + 5*s + 2  

#### URL = https://controlalgo.ey.r.appspot.com/closedloop/unitfeedback?num=1,0,2&den=2,0,5,2



