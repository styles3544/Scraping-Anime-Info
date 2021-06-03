# How to Setup This Web Automation Project

> Getting real time anime info and updates sent directly to your smartphone

Contents:
------------------
   - [Getting Started](##Getting-Started)
    
   - [Prerequisites](#Prerequisites)
    
   - [Setting Up Pushbullet Channel](#Setting-Up-Pushbullet-Channel)
       +  Generating Access Token
       +  Running The Code 
        
   - [More Possibilities](#More-Possibilities)
       + [Custom Search Feature](#Custom-Search-Feature)
        
   - [References](#References)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

1. Get the code by cloning the repository 

2. Open the folder Script and It'll look something like below

![](assets/torun1.gif)

3. Right click on script1.py file and select --> open with IDLE as shown below ( You will get this option if python is already installed in your pc )

![](assets/torun2.gif)

4. Now select 'Run Module' from 'Run' option as shown in next step ( Make sure that you're connected to the internet before running the script )

5. After clicking that one few windows might open like browser, and terminal window as shown below:
   ( After few seconds the browser will automatically close and you can see your results )

![](assets/torun3.gif)

You can use pyCharm to run the script as:

![](assets/results1.gif)


### Prerequisites

What things you need to run the program:
  
    - selenium package

use pip to install the selenium package. Python 3.6 has pip available in the standard library. Using pip, you can install selenium by opening your powershell and typing the following:    

```
pip install selenium

```

## Setting Up Pushbullet Channel

If you want custom notifications in your smartphone then can use any medium but as I've used pushbullet so I'm gonna show u how I did it

1. Make a pushbullet account

![](assets/pb.gif)

2. Make a channel on your pushbullet account

![](assets/pushbullet_make_channel.gif)

3. generate your pushbullet ACCESS TOKEN as follows

![](assets/creatingaccesstoken.gif)

4. Copy the ACCESS TOKEN you generated and replace it with "YOUR_ACCESS_TOKEN" in the code in line 

```
api_key = 'YOUR_ACCESS_TOKEN'

```

5. Uncomment the lines marked in the following image ( remove '#' symbol from start )

![](assets/removinghashes.png)

6. Run the module again as shown in step 5 of [Getting Started](#Getting-Started) section 




## More Possibilities

You can add as many features you want to the program. For example I added a custom search feature to it the [Custom Search Feature](#Custom-Search-Feature) section.


You can also add feature like:
   + Season Info
   + When is the next episode of any particular anime is coming?
   + Next episode synopsis
   + Airing or Completed/Finished
   + What are the Genres of any anime?
   + And many more.....


> You can also host your python code online on [wayScript](https://wayscript.com/) and schedule it there so that it'll run automatically and keep yourself updated 

![wayscript](assets/Annotation.png)



### Custom Search Feature

As you can see below that I added a custom search option by modifying the script so that I can look for the anime I want. You can also contribute to the code and add more features to it.

![](assets/results2.gif)

![](assets/gleipnir_results.gif)

I've provided the code for above in Script2 ( with custom search option ) folder, so that the process of getting notification using pushbullet API is also clear to you.


## References

1. [pushbullet Docs](https://pypi.org/project/pushbullet.py/0.9.1/)

2. [selenium Docs](https://selenium-python.readthedocs.io/getting-started.html)

3. [How to use selenium](https://www.edureka.co/blog/selenium-using-python/)


## Authors

* **Piyush Kumar ( styles )** 




