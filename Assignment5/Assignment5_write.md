<center><font face="微软雅黑" size=5 color=red><b>数字图像处理及应用 第5次作业</b></font></center>

<center><font face=“微软雅黑" size=4 color = blue><b>组号： <u>XX（两位数字）</u>&emsp;小组成员： <u>（列出所有小组成员，成员姓名间用1个空格间隔）</u></b></font></center>



<font face = "微软雅黑" size= 5><b>Part I Exercises</b></font>

***

**Ex.1**  Let A denote the set shown shaded in the following figure, and refer to the structuring elements shown (the black dots denote the origin). Sketch the result of the following operations:
(**a**) $\left( A \ominus B^4 \right) \oplus B^2$.
(**b**) $\left( A \ominus B^1 \right) \oplus B^3$.
(**c**) $\left( A \oplus B^1 \right) \oplus B^3$.

<div align=center><img src="./images/FigP0906.png" alt="FigP0906" style="zoom:40%;"></div>

<div align=center><b>FIGURE 1 Image and structure elements</b></div>

**Answer:**





***

**Ex.2** Prove the validity of the following expressions:
(**a**) $A\circ B$ is a subset (subimage) of $A$.
(**b**) If $C$ is a subset of $D$, the $C\circ B$ is a subset of $D\circ B$.
(**c**) $(A\circ B)\circ B = A\circ B$.

**Answer:**





***

**Ex.3** 

(**a**) Give a morphological algorithm for converting an 8-connected binary boundary to an m-connected boundary. You may assume that the boundary is fully connected and that it is one pixel thick. 
(**b**) Does the operation of your algorithm require more than one iteration with each structuring element? Explain your reasoning.
(**c**) Is the performance of your algorithm independent of the order in which the structuring elements are applied? If your answer is yes, prove it; otherwise give an example that illustrates the dependence of your procedure on the order of application of the structuring elements.

**Answer:**





***

**Ex.4** The rectangle in the binary image in FIGURE 2 is of size $m\times n$ pixels.
(**a**) What would the magnitude of the gradient of this image look like based on using the approximation given in Eq. (1)?
$$
M(x,y)\approx |g_x|+|g_y| \tag{1}
$$
 Assume that $g_x$ and $g_y$ are obtained using the Sobel operators. Show all relevant different pixel values in the gradient image.
(**b**) Sketch the histogram of edge directions computed using Eq. (2). Be precise in labeling the height of each component of the histogram.
$$
\alpha(x,y)=\arctan\left[\frac{g_y}{g_x}\right] \tag{2}
$$
(**c**) What would the Laplacian of this image look like based on using the approximation in Eq. (3)? Show all relevant different pixel values in the Laplacian image.
$$
\nabla^2f(x,y)=f(x+1,y)+f(x-1,y)+f(x,y+1)+f(x,y-1)-4f(x,y) \tag{3}
$$


<div align=center><img src="./images/FigP1012.png" alt="FigP1012" style="zoom:100%;"></div>

<div align=center><b>FIGURE 2 A binary image of size m &times n </b></div>

**Answer:**





***

**Ex.5** Marr and Hildreth noted that it is possible to approximate the LoG filter in Eq.(4) by a difference of Gaussians (DoG) in Eq.(5):
$$
\nabla^2G(x,y)=\left[\frac{x^2+y^2-2\sigma^2}{\sigma^4}\right]e^{-\frac{x^2+y^2}{2\sigma^2}} \tag{4}
$$

$$
\rm DoG(x,y)=\frac{1}{2\pi\sigma_1^2}e^{-\frac{x^2+y^2}{2\sigma_1^2}}-\frac{1}{2\pi\sigma_2^2}e^{-\frac{x^2+y^2}{2\sigma_2^2}} \tag{5}
$$
with $\sigma_1 >\sigma_2$. To make meaningful comparisons between the LoG and DoG, the value of $\sigma$ for the LoG must be selected as in the Eq.(6) so that the LoG and DoG have the same zero crossings,
$$
\sigma^2=\frac{\sigma_1^2 \sigma_2^2}{\sigma_1^2-\sigma_2^2}\ln\left[\frac{\sigma_1^2}{\sigma_2^2}\right] \tag{6}
$$
(**a**) Derive Eq. (6).
(**b**) Let $k ={\sigma_1}/{\sigma_2}$ denote the standard deviation ratio discussed in connection with the DoG function, and express Eq. (6) in terms of $k$ and $\sigma_2$.

**Answer:**





***

**Ex.6** An important area of application for image segmentation techniques is in processing images resulting from so-called *bubble chamber* events. These images arise from experiments in high-energy physics in which a beam of particles of known properties is directed onto a target of known nuclei. A typical event consists of incoming tracks, any one of which, in the event of a collision, branches out into secondary tracks of particles emanating from the point of collision. Propose a segmentation approach for detecting all tracks angled at any of the following six directions off the horizontal: $\pm 25^{\circ}$, $\pm 50^{\circ}$, and $\pm 75^{\circ}$. The allowed estimation error in any of these six directions is $\pm 5^{\circ}$. For a track to be valid it must be at least 100 pixels long and have no more than three gaps, each not exceeding 10 pixels. You may assume that the images have been preprocessed so that they are binary and that all tracks are 1 pixel thick, except at the point of collision from which they emanate. Your procedure should be able to differentiate between tracks that have the same direction but different origins. (**Hint: Base your solution on the Hough transform.**)

**Answer:**





<div STYLE="page-break-after: always;"></div>

<font face = "微软雅黑"  size= 5><b>Part II Programming</b></font>

***

**1.** Refer to the image and the disk structuring element shown in FIGURE 3. Sketch what the sets $C$, $D$, $E$, and $F$ would look like for the following sequence of operations: 

a) $C=A\ominus B$;

b) $D=C\oplus B$;

c) $E=D\oplus B$;

d) $F=E\ominus B$.

Set $A$ consists of all the foreground pixels (white), except the structuring element, $B$, which you may assume is just large enough to encompass any of the random elements in the image. Note that the sequence of operations above is simply the opening of $A$ by $B$ followed by a closing of the result by $B$.

<div align=center><img src="./images/FigP0917.png" alt="FigP0917" style="zoom:40%;"></div>

<div align=center><b>FIGURE 3 Image and the disk structuring element</b></div>

(*followed by  **Matlab live Scripts**  or **Jupyter Scripts** and running results*)



**2.**   Consider the image in FIGURE 4, which shows a region of small circles enclosed by a region of larger circles.
(**a**) Give a morphologic algorithm to partition the image into two parts, in which one contains small circles and another contains larger circles. You can make any assumptions that you need to make for the method to work.
(**b**) Sketch the result in each step of your algorithm.

<div align=center><img src="./images/FigP0934.png" alt="FigP0934" style="zoom:50%;"></div>

<div align=center><b>FIGURE 4</b></div>

(*followed by **Matlab live Scripts** or **Jupyter Scripts** and running results*)



**3.**   The objects and background in FIGURE 5 have a mean intensity of 170 and 60, respectively, on a [0, 255] scale. The image is corrupted by Gaussian noise with 0 mean and a standard deviation of 10 intensity levels. 

(**a**) Segment the image based on thresholding (Refer to Example 10.15 in textbook, and pay attention to the choice of initial threshold $T$).

(**b**) Repeat segmentation based on region growing. (**Optional**)

<center class="half"><img src="./images/FigP1036.png" alt="FigP1036" style="zoom:60%"></center>

<div align=center><b>FIGURE 5</b></div>

(*followed by **Matlab live Scripts** or **Jupyter Scripts** and running results*)
