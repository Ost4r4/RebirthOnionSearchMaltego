# Description
Maltego plugin for finding .onion links on Tor. It uses three search engines: Ahmia, Gdark, Tormax.


## Example of use

![](https://user-images.githubusercontent.com/128547363/232911743-2cb50de9-9405-4371-965d-1ea5fab1977e.gif)
_Load times have been greatly sped up as part of this gif._

## Installation

Install the necessary libraries
```
pip3 install maltego-trx
pip3 install re
pip3 install urllib3
pip3 install BeautifulSoup
```
Start a new project with Maltego-TRX. This will create a new_project directory in your home
```
maltego-trx start new_project
```
Download ROSM (RebirthOnionSearchMaltego)
```
git clone https://github.com/Ost4r4/RebirthOnionSearchMaltego.git
```
Move the script to the directory specific to Maltego-TRX
```
mv RebirthOnionSearchMaltego/RebirthOnionSearchMaltego.py new_project/transforms/RebirthOnionSearchMaltego.p
```
Start Maltego
```
maltego
```
Click on "New Local Transform"

![](https://user-images.githubusercontent.com/128547363/232909799-732589dc-d03d-40b9-a784-f568c75f7efa.png)

Fill parameters

![](https://user-images.githubusercontent.com/128547363/234114045-5bb9ccf1-ee16-4d9f-986b-8b6da7cb39e2.png)

Again

![](https://user-images.githubusercontent.com/128547363/234114460-d5e272ae-54d0-47a1-8b12-53e32f4258f2.png)

Deploy a phrase entity of your choice

![](https://user-images.githubusercontent.com/128547363/232910513-dbb034df-e254-461c-a9c8-d57e9888d9f9.png)

Right-click, choose Local transform and launch the transformation

![](https://user-images.githubusercontent.com/128547363/232910717-fd56452d-a6cd-4984-a0e5-41ef86282730.png)

Several minutes or even hours can be necessary, because this script checks if each page still exists. 

GLHF !
