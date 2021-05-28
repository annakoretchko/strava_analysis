

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
  <a href="https://anna-koretchko.ue.r.appspot.com/garmi">
    <img src="images_RM/avg_speed_vs_distance.png" alt="Logo" width="800" height="500">
  </a>

  <h3 align="center">Garmin Running Analysis</h3>

  <p align="center">
    Quick package created to analyze data from Garmin Connect
    <br />
    <a href="https://connect.garmin.com/"><strong>Garmin Connect »</strong></a>
    <br />
    <br />
    <a href="/dist/garmin_analysis-0.1-py3-none-any.whl">Latest Package</a>
    ·
    <a href="https://anna-koretchko.ue.r.appspot.com/garmin">Demo</a>

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
<img src="images/Garmin-logo2.jpeg" alt="Logo"> 
</p>
I am an avid running and love using my Garmin Forerunner 945 to collect all the data available while I run. Over the past 8 years, I have accumulated quite a large amount of data. I created this python package for anyone to analyse their Garmin Data from the Garmin Connect site and gain deeper understanding about their running analytics!


* If you wanna try on your own but don't have a Garmin account, feel free to use the data in the demo-data folder!



### Built With

This section should list any major frameworks that you built your project using. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.
* [Python](https://www.python.org/)




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

