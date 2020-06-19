# BestPix

Use your Mac to see the photos your iPhone thinks are best. Inspired by Simon Willison's [Pelican post](https://simonwillison.net/2020/May/21/dogsheep-photos/)!

## Description 

Each time you take a photo with your iPhone, a "beautifulness" score is given to that photo. This package shows you the 10 highest scoring photos.

## Supported Platforms

  * Mac 

## Privacy

No data leaves your computer.


## Install 

1. Install and start [Docker Desktop](https://docs.docker.com/docker-for-mac/install/)
2. Open your terminal and run the command `pip install bestpix`

## Use

1. Import your iPhone's photos to your Mac. Official instructions [here](https://support.apple.com/en-us/HT201302#importmac)
2. Open your terminal and run the command `reveal`
3. Using your web browser, go to `localhost:8442`

## Uninstall 

1. Open your terminal and run the command `cleanup`, then the command `pip3 uninstall bestpix`
2. Shutdown and uninstall Docker Desktop