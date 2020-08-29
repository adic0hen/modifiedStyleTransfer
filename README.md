This is the readme file for modifiedstyletransfer project, welcome.  
First, make sure you have both django and tensorflow on your environment (you may have to degrade your version of tensorflow to 1.4).  
You can use the requirements file appended to the git.
To work with this project, you will need to download weights to work with the several networks:
* For adain- 1. download VGG19 weights from [here](https://s3-us-west-2.amazonaws.com/wengaoye/vgg19_normalised.npz) and save it in your main directory.   
 Also download the checkpoint weights from [here](https://s3-us-west-2.amazonaws.com/wengaoye/arbitrary_style_model_style-weight-2e0.zip).
 Add the downloaded checkpoint to a ./models directory (create that directory yourself).
 
* You will need to download another set of pretrained vgg 19 weights from [here](https://www.vlfeat.org/matconvnet/models/imagenet-vgg-verydeep-19.mat) ans save it in your main directory.

* Don't change the files names, if you do, you will need to specify the new names in the appropriate locations in the code.

That's it, you are good to go!

Now, to run the website:
* Open terminal in "django_project" directory and run "python manage.py runserver", access the website in the ip address that django will supply.



