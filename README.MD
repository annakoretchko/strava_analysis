

<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />

<p align="center">
  <a href="https://anna-koretchko.ue.r.appspot.com">
    <img src="images4ReadME/avg_speed_vs_distance.png" alt="Logo" width="800" height="500">
  </a>

  <h3 align="center">Strava Running Analysis</h3>

  <p align="center">
    Created this package as a way to implement the Strava API to automatically get my running data. Additionally, performed some Machine Learning Models are my data!
    <br />
    <a href="https://connect.garmin.com/"><strong>Strava »</strong></a>
    <br />
    <br />
    <a href="https://github.com/annakoretchko/strava_analysis/tree/master/dist/lastest_build">Latest Package</a>
    ·
    <a href="https://anna-koretchko.ue.r.appspot.com">Demo</a>
    ·
    <a href="https://developers.strava.com/">Strava API Documentation</a>
    ·
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
<p align="center">
<img src="images4ReadME/strava_logo.png" alt="Logo"> 
</p>
I have been using Strava since 2014, and for those of you unfamiliar with what Strava is, it's essentially 
a social media for runners, bikers and swimmers alike. A platform where equally obsessed athletes can gather and
ogle over their exercise data. 
<br />
I have been collecting running, swimming, lifting, and social media data surrounding my exercise efforts for the past  7 years, so I figured it was time to start doing some analytics ont he data. And sharing my methods and approach with you!
<br />
<br />

This project I will be going through the following:

  1. Provide a method to gather your most recent Strava data automatically, using python, via Strava's API
  2. Gather your historic Strava data through their site
  3. Clean and join the new and historic data 
  4. Start exploring my data and asking serious questions, like, can we predict the number of kudos I will receive on my next run by how many pictures I post? 
  5. But seriously, doing some cool Machine Learning, simple stats and other fun math to interpret our data!
<br />
<br />

* If you wanna try on your own but don't have a Strava account, feel free to use the demo-data in the data folder!

* If you wanna sign up for Strava and start collecting your own data, you can sign up [here](https://www.strava.com/register/free). It's **FREE**!

### Built With

This project is built using the following: 
* [Python](https://www.python.org/)
* [jupyter notebook](https://jupyter.org/)
* [Strava API](https://developers.strava.com/)



Also special thanks to Francis Polignano who provided some key [YouTube videos](https://www.youtube.com/watch?v=sgscChKfGyg) and [repos](https://github.com/franchyze923/Code_From_Tutorials/tree/master/Strava_Api) explaining how to work with Strava's API.

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

Python is the only requirement for this project (however, environment managers such as conda are greatly suggested as well)
* python
  ```sh
  sudo apt-get install python3.6
  ```

### Installation and Example Run

1. Create conda environment for garmin_analyis project ([install conda Here](https://conda.io/projects/conda/en/latest/user-guide/install/index.html))

2. Download the latest wheel (whl) from from the dist folder [here] (/dist/garmin_analysis-0.1-py3-none-any.whl)

3. cd to the downloaded wheel file
   ```sh
   (garmin_env) cd Downloads/garmin_analysis-0.X-py3-none-any.whl
   ```
4. pip install `garmin_analysis-0.X-py3-none-any.whl` to your newly created conda environment
   ```sh
   (garmin_env) pip install garmin_analysis-0.X-py3-none-any.whl
   ```
5. Now run the package which requires two inputs: -data and -output_path 
    ```sh
    (garmin_env) python -m garmin_analysis -data "<path to data file from Garmin Connect" -output_path "<path to where you want the output files to be saved"
    ```

<!-- USAGE EXAMPLES -->
## Usage

This packages allows Garmin Connect users to analyze their data in a pythonic manner, which can be extrapolated further into a myriad of projects! 
_To see a live demo of the graphs/outputs, please refer to the [Demo](https://anna-koretchko.ue.r.appspot.com/garmin)_



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

* Anna Koretchko - [Personal Website](https://anna-koretchko.ue.r.appspot.com/index)
* Email - annakoretchko@gmail.com







<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/annakoretchko/garmin_analysis/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/anna-koretchko-1b5b0211a/
[product-screenshot]: images/screenshot.png

