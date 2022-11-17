# Why make it?

Python is a very popular tool when it comes to working with Data analytics, data sciences, AI and machine learning projects, etc. These fields often benfit from visualization tools for both analytical and presentation purposes.

`Matplotlib` is a common example of this. However tools like matplotlib do not often have a great visual appeal, hence this community lacks a tool for presentation purposes which has given rise to libraries like `pyvis` that gave better visualization tools by using web based front-end, clearly showing there is potential for a front end web dev framework in python to be useful to this community.

## Some approaches to give your python project a web based frontend include

- Using Python as a wrapper

A python code generates an HTML and Javascript static webpage and displays the webpage, example `pyvis`. problem with this is that the website being static is not reactive and can not directly communicate with the python code to send in inputs or update its state

- Using a python interpretter made in JS / convert python code to JS

There have been brilliant attempts like `Skulpt` that have written python interpretters in javascript allowing developers to write entire front end websites in python. However since the website ends up running in javascript, there is very limited access to the vast ecosystem of python libraries which makes using python a rich experience

- Using a Flask/Django API to host the python data to a Javascript webpage

While this approach gives you access to all the python resources and well as web development tools you may need, the approach is complex to impliment, can be an overkill when the purpose of the UI is to be presented on a local machine and requires the developer to have good knowledge of both javascript and python
