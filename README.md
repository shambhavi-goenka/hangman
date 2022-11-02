<!-- Project Head -->
<br />
<div align="center">
  <a href="https://github.com/po-the-panda-12/hangman">
    <img src="https://d338t8kmirgyke.cloudfront.net/icons/icon_pngs/000/001/955/original/hangman.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Hangman</h3>

  <p align="center">
    Hangman game using threading for user request for hints
    <br/>
  </p>
</div>

</br>

<!-- TABLE OF CONTENTS -->
<details>
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
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#references">References</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

<!-- Here's a blank template to get started: To avoid retyping too much info. Do a search and replace with your text editor for the following: `github_username`, `repo_name`, `twitter_handle`, `linkedin_username`, `email_client`, `email`, `project_title`, `project_description`

<p align="right">(<a href="#top">back to top</a>)</p> -->



### Built With

* [Python3](https://www.python.org/)
* Java (coming)
* C (coming)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

(For Python) <br/>
This is an example of how to list things you need to use the software and how to install them.
* wonderwords
  ```sh
  pip install wonderwords
  ```
* ez_setup (for PyDictionary)
  ```sh
  pip install ez_setup
  ```
* PyDictionary
  ```sh
  pip install PyDictionary
  ```

### Installation

<!-- 1. Get a free API Key at [https://example.com](https://example.com) -->
1. Clone the repo
   ```sh
   git clone https://github.com/po-the-panda-12/hangman 
   ```
  
2. Run program
   ```sh
   python3 hangman.py 
   ```
  
<!-- 3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ``` -->

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

The hangman game can be used to test your guessing abilities; but more importantly can be used as a compiled OOP (object oriented programming) example of list comprehension, threading (timer) and input validation.
Please do reach out if you have any suggestions on how to further develop this code

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- Create Hangman class containnig the following functions
  - secret()
  - change_error()
  - find_all()
  - display()
  - change_word()
  - set_choice()
  - check()
  - guess_check(guess_char)
  - hint_timer()
  - hint()
 
- Main function
  - Create object
  - Start timer
  - Get user input
  - Generate hint specific content user input / output (if timer elapsed)
  - Stop timer (used in case previous step of hint generation was not summoned)
  - Update guess and display stick figure


</br>

See the [open issues](https://github.com/po-the-panda-12/hangman/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [@shambhavi_goenka](https://t.me/shambhavi_goenka) - shambhavigoenka@gmail.com

Project Link: [https://github.com/po-the-panda-12/hangman](https://github.com/po-the-panda-12/hangman)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- REFERENCES -->
## References

* [Random Word Generation (wonderwords)](https://wonderwords.readthedocs.io/en/latest/index.html)
* [Word Definition (PyDictionary])(https://pypi.org/project/PyDictionary/)



<p align="right">(<a href="#top">back to top</a>)</p>


[product-screenshot]: images/screenshot.png
