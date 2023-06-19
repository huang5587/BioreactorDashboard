# Ark Biotech SWE Intern 2023 Take Home Project by Jun Han Huang, May 2023
# Technical Overview
For this project I decided to use the streamlit library to create and manipulate the necessary Bioreactor graphs. The library is a popular and user friendly choice for creating minimalist data science related web-apps, favoured for its readability and minimalist theme. In addition, Streamlit is has integration for industry favoured data science libraries (eg. pandas, numpy, matplotlib.)

# General Features 
To my understanding, I have successfully accomplished all the necessary MVP criteria. 

# Bonus Features
I was able to create the download button that lets the user download .csv files for each data metric.

Unfortunately, as I am currently studying for finals I couldn't find the time to finish the other two bonus features, but I wanted to share how I would approach them.

1) Can you allow the user to select the time window?
    -Let user input time choice via dropdown menu
    -dropdown menu is populated with min and max values of time calculated from dataframe
    -use a dropdown menu to avoid having to do deal with invalid input from the user
    -use the min/max time values filter criteria to disregard data outside of the range
    -plot new graphs accordingly and adjust the x-axis limits accordingly

2) Can you add a button to refresh the data without refreshing the page, or auto-refresh the page for the user?
    -add a state to the app associated with data staleness
    -create a button to toggle that state
    -when that state is invalid, trigger data refresh.