README file for Machine learning Porject on Online Fraud Detection

In ML_Project_Train

1. Make sure all the libraries used are installed on your system
   or environment in which the code is being run on.
   (The libraries are installed using the pip install "library" command)

2. If the files are running through google colab, mount the collaboratory
  with the command prompted by colab

3. On line 32, change the location accordingly where the train.csv file
 is present

4. Line 244 downloads the processed .csv file so run the code and save the
processed file so that we dont have to run the code again and again
(Note: This code is only for google colab; if done via any other platform,
comment lines 244-246 and download the csv file accordingly)

In ML_Project_Test

1. As Done above, install the the required libraries, mount the collaboratory
and change the location of the files on lines 35 and 37

2. In order to test each of the models, decomment the block of code under
 each text block which has a model name (By default, the light GBM model has been 
decommented as it gave the best result according to the current preprocessing)

3. After step 2, run the code which will in turn will download the prediction file
(Note: The downloading in the code is from line 238 which works fine on google colab;
if used on any other platform, change the code accordingly)


