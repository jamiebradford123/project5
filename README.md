# Mildew Detection in Cherry Leaves Project


## Dataset Content
* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). We then created a fictitious user story where predictive analytics can be applied in a real project in the workplace.
* The dataset contains +4 thousand images taken from the client's crop fields. The images show healthy cherry leaves and cherry leaves that have powdery mildew, a fungal disease that affects many plant species. The cherry plantation crop is one of the finest products in their portfolio, and the company is concerned about supplying the market with a compromised quality product.



## Business Requirements
The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute.  The company has thousands of cherry trees, located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.


* 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
* 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.


## Hypothesis and how to validate?

* We believe that cherry leaves which have powdery mildew have clear signs/ marks which will allow Farky & Foods to differentiate between healthy and unhealthy cherry trees
  * An average image study can help to investigate it


## The rationale to map the business requirements to the Data Visualisations and ML tasks

* **Business Requirement 1**: Visually differentiate a healthy cherry leaf from one with powdery mildew (Data Visualisation).
	* We will display the "mean" and "standard deviation" images for healthy and unhealthy cherry trees.
 	* We will display the difference between an average healthy leaf and an average powdery mildew leaf.
	* We will display an image montage for either a healthy leaf or a powdery mildew leaf.

* **Business Requirement 2**:  Predicting if a cherry leaf is healthy or contains powdery mildew (Classification).
	* We want to predict if a cherry leaf is healthy or contains powdery mildew. 
	* We want to build a binary classifier and generate reports.

## ML Business Case

* What are the business requirements?
	* The client is interested in conducting a study to visually differentiate a cherry leaf that is healthy from one that contains powdery mildew.
	* The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

* Is there any business requirement that can be answered with conventional data analysis?
	* Yes, we can use conventional data analysis to conduct a study to visually differentiate a cherry leaf that is healthy from one that contains powdery mildew.

* Does the client need a dashboard or an API endpoint?
	* The client needs a dashboard.

* What does the client consider as a successful project outcome?
	* A study showing how to visually differentiate a cherry leaf that is healthy from one that contains powdery mildew.
	* Also, the capability to predict if a cherry leaf is healthy or contains powdery mildew.

* Can you break down the project into Epics and User Stories?
	* Information gathering and data collection.
	* Data visualization, cleaning, and preparation.
	* Model training, optimization and validation.
	* Dashboard planning, designing, and development.
	* Dashboard deployment and release.

* Ethical or Privacy concerns?
	* The client provided the data under an NDA (non-disclosure agreement), therefore the data should only be shared with professionals that are officially involved in the project.

* Does the data suggest a particular model?
	* The data suggests a binary classifier, indicating whether a particular cherry leaf is healthy or contains powdery mildew.

* What are the model's inputs and intended outputs?
	* The input is an unlabelled cherry leaf image and the output is a labelled image with a prediction of whether the cherry leaf is healthy or contains powdery mildew.

* What are the criteria for the performance goal of the predictions?
 * We agreed with the client a degree of 97% accuracy.

* How will the client benefit?
	* The client will not supply the market with a product of compromised quality.

### Powdery Mildew Classifier
* Aim - Create an ML model to predict if a leaf is healthy or contains powdery mildew, based on historical image data. It is a supervised model, a 2-class, single-label, classification model.
* Ideal outcome - provide Farmy & Foods a faster and more reliable diagnostic for powdery mildew detection.
* The model success metrics are
	* Accuracy of 97% or above on the test set.
* The model output is defined as a flag, indicating if the leaf contains powdery mildew or not and the associated probability of being healthy or not. An employee will take a picture of a leaf and upload the picture to the App. The prediction is made on the fly (not in batches).
* Heuristics: Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute. This is not scalable as the farm has thousands of trees and having enough experienced staff will require a lot of money and training. 
* The training data to fit the model come from the [Kaggle](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves). This dataset contains about +4 thousand images.
	* Train data - target: contains powdery mildew or not; features: all images

## Dashboard Design (Streamlit App User Interface)

### Page 1: Quick Project Summary
* Quick project summary
	* General Information
		* Powdery mildew is a fungal disease that affects many plant species. 
		* An employee takes a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute.
	* Project Dataset.
		* The dataset contains +4 thousand images taken from the client's crop fields. The images show healthy cherry leaves and cherry leaves that have powdery mildew.
	* Business requirements
		* The company is concerned about supplying the market with a compromised quality product.
		*  The company needs a faster more scalable option to check its thousands of trees. A ML system to detect an infected leaf would speed up the process

### Page 2: Leaf Visualizer
* It will answer business requirement 1
	* Checkbox 1 - Difference between average and variability image
	* Checkbox 2 - Differences between average healthy and average infected leaf
	* Checkbox 3 - Image Montage

### Page 3: Powdery Mildew detector
* Business requirement 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.
* Link to download a set of infected and uninfected leaf images for live prediction.
* User Interface with a file uploader widget. The user should upload multiple leaf images. It will display the image and a prediction statement, indicating if the leaf is infected or not with powdery mildew and the probability associated with this statement. 
* Table with the image name and prediction results.
* Download button to download table.

### Page 4: Project Hypothesis and Validation
* Block for each project hypothesis, describe the conclusion and how you validated it.

### Page 5: ML Performance Metrics
* Label Frequencies for Train, Validation and Test Sets
* Model History - Accuracy and Losses
* Model evaluation result


## Unfixed Bugs
* You will need to mention unfixed bugs and why they were unfixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable for consideration, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.

## Deployment
### Heroku

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/ 
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file. 


## Main Data Analysis and Machine Learning Libraries
* Here you should list the libraries used in the project and provide an example(s) of how you used these libraries.


## Credits 

* In this section, you need to reference where you got your content, media and from where you got extra help. It is common practice to use code from other repositories and tutorials. However, it is necessary to be very specific about these sources to avoid plagiarism. 
* You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content 

- The text for the Home page was taken from Wikipedia Article A.
- Instructions on how to implement form validation on the Sign-Up page were taken from [Specific YouTube Tutorial](https://www.youtube.com/).
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/).

### Media

- The photos used on the home and sign-up page are from This Open-Source site.
- The images used for the gallery page were taken from this other open-source site.



## Acknowledgements (optional)
* Thank the people that provided support throughout this project.

Business Case Assessment
You have already conducted a business case assessment, so you can also use that information to build your project README file.

What are the business requirements?
The client is interested in conducting a study to visually differentiate a cherry leaf that is healthy from one that contains powdery mildew.
The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.
Is there any business requirement that can be answered with conventional data analysis?
Yes, we can use conventional data analysis to conduct a study to visually differentiate a cherry leaf that is healthy from one that contains powdery mildew.
Does the client need a dashboard or an API endpoint?
The client needs a dashboard.
What does the client consider as a successful project outcome?
A study showing how to visually differentiate a cherry leaf that is healthy from one that contains powdery mildew.
Also, the capability to predict if a cherry leaf is healthy or contains powdery mildew.
Can you break down the project into Epics and User Stories?
Information gathering and data collection.
Data visualization, cleaning, and preparation.
Model training, optimization and validation.
Dashboard planning, designing, and development.
Dashboard deployment and release.
Ethical or Privacy concerns?
The client provided the data under an NDA (non-disclosure agreement), therefore the data should only be shared with professionals that are officially involved in the project.
Does the data suggest a particular model?
The data suggests a binary classifier, indicating whether a particular cherry leaf is healthy or contains powdery mildew.
What are the model's inputs and intended outputs?
The input is a cherry leaf image and the output is a prediction of whether the cherry leaf is healthy or contains powdery mildew.
What are the criteria for the performance goal of the predictions?
We agreed with the client a degree of 97% accuracy.
How will the client benefit?
The client will not supply the market with a product of compromised quality.
Project Considerations
Business Requirement 1
Your study should include at least analysis on:
average images and variability images for each class (healthy or powdery mildew),
the differences between average healthy and average powdery mildew cherry leaves,
an image montage for each class.
Business Requirement 2
You may deliver an ML system that is capable of predicting whether a cherry leaf is healthy or contains powdery mildew. In this case, we suggest to use Neural Networks to map the relationships between the features and the labels.
You will notice when exploring the dataset that the images are 256 pixels × 256 pixels. When defining your image shape to load the images to memory for training the model, you may choose 256 × 256 as your image shape. However, that will lead to a trained model that will likely be larger than 100Mb. This is fine as long as the model meets the project requirement, the caveat is that you may need to use Git LFS (Large File Storage) to push files larger than 100Mb to GitHub. As a result, we suggest you consider using an image shape that is smaller, like 100 × 100 or 50 × 50, with the expectation that the model would still meet the performance requirement and will be smaller than 100Mb for a smoother push to GitHub.
Dashboard Expectations
Your dashboard should contain:

A project summary page, showing the project dataset summary and the client's requirements.
A page listing your findings related to a study to visually differentiate a cherry leaf that is healthy from one that contains powdery mildew
A page containing:
A link to download a set of cherry leaf images for live prediction (you may use the Kaggle repository that was provided to you).
A User Interface with a file uploader widget. The user should have the capacity to upload multiple images. For each image, it will display the image and a prediction statement, indicating if a cherry leaf is healthy or contains powdery mildew and the probability associated with this statement.
A table with the image name and prediction results, and a download button to download the table.
A page indicating your project hypothesis and how you validated it across the project.
A technical page displaying your model performance.