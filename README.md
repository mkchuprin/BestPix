# BestPix

View your iPhone's best photos by leveraging Apple's machine learning models.
Inspired by Simon Willison's [Pelican post](https://simonwillison.net/2020/May/21/dogsheep-photos/)!


## Description 

All of your iPhones photos are put through Apple's machine learning models to produce a table of "beautifulness" scores. This table is saved on your iPhone and copied to your MacBook when you import your Photos from your iPhone to your Macbook. This package will read that table to find the 10 most beautiful photos and display them for you in your browser. 


## Supported Platforms

  * Mac 

## Privacy

No data leaves your computer.

## Prerequisites

* The latest available version of [Python3](https://www.python.org/downloads/)
* [Docker Desktop](https://www.docker.com/products/docker-desktop)


## Install 

1. Open your terminal and run the command `pip3 install bestpix`

## Use

1. Start Docker Desktop by opening your terminal and running `open -a Docker`
2. Import your iPhone's photos to your Mac. Official instructions [here](https://support.apple.com/en-us/HT201302#importmac)
3. Start the package by opening your terminal and running `reveal`
4. View the results by opening your web browser and going to the url `localhost:8442`

## Uninstall 

1. Open your terminal and run the command `cleanup`, then the command `pip3 uninstall bestpix`
2. Shutdown and uninstall Docker Desktop as you would any Application. Official instructions [here](https://support.apple.com/en-us/HT202235)