# Introduction
Objective of this repo is to demonstrate condition execution of CI/CD pipline only when there is any change in relevant file

## How to test ?
* make any changes in `weather_package_1` lead to execution of pipline corresponding to that
* make any changes in `weather_package_2` lead to execution of pipline corresponding to that
* make any changes in `weather_package_1` and `weather_package_2`  in one PR will execute pipline for both
* make any changes outside of `weather_package_1` and `weather_package_2` will not execute any pipline.

## How to install packages ?
* Setup ssh in yout local and run pip command `pip install git+ssh://git@github.com/sudhanshuptl/weather_pkg_1/weather_pkg.git`
* Setup ssh in yout local and run pip command `pip install git+ssh://git@github.com/sudhanshuptl/weather_pkg_2/weather_pkg.git`