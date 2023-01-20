<a name="readme-top"></a>

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/tuhinmallick/pyMorse">
    <img src="docs/images/security.svg" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">pyMorse</h3>

  <p align="center">
    pyMorse is a python package that incorporating RSA into your email for added privacy.
    <br />
    <a href="https://github.com/tuhinmallick/pyMorse"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/tuhinmallick/pyMorse/blob/main/notebooks/Insider_trading_analysis.ipynb">View Demo</a>
    ·
    <a href="https://github.com/tuhinmallick/pyMorse/issues">Report Bug</a>
    ·
    <a href="https://github.com/tuhinmallick/pyMorse/issues">Request Feature</a>
  </p>
</div>

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
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

This is a Python package for implementing confidentiality techniques such as data masking and data encryption for sensitive data in your applications.

The package includes the following features:

Masking of sensitive data such as personal identification numbers, credit card numbers, and email addresses
Encryption of sensitive data using industry-standard algorithms such as AES and RSA
Support for masking and encryption of various data types including strings, integers, and dates
Easy to use and integrate with existing applications

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!--
### Built With

* [![Next][Next.js]][Next-url]
* [![React][React.js]][React-url]
* [![Vue][Vue.js]][Vue-url]
* [![Angular][Angular.io]][Angular-url]
* [![Svelte][Svelte.dev]][Svelte-url]
* [![Laravel][Laravel.com]][Laravel-url]
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]
* [![JQuery][JQuery.com]][JQuery-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p> -->

<!-- GETTING STARTED -->

## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the package and how to install them.

### Installation


```python
pip install pyconfidentiality
```

<h3 align="center"><b>Usage</b></h3>

## 1. Generate the Public and Private Keys

```python
from pyconfidentiality import generate_keypair

bit_length = int(input("Enter bit length: "))

public_key, private_key = generate_keypair(2**bit_length)
```

## 2. Generate Cipher Text

```python
from pyconfidentiality import encrypt_message
plain_text = input("Enter a message: ")
cipher_text, cipher_obj = encrypt_message(plain_text, public_key)
print("Encrypted message: {}".format(cipher_text))
```

## 3. Send the message

- Note we are intially using GMAIL for this
- Make sure your Google Account has [Allow Less Secure App Access](https://myaccount.google.com/lesssecureapps) enabled
- It is always recommeded to store the credentials of your GMAIL account using environment variables in your system

```python
from pyconfidentiality import send_message
your_email = os.environ.get('EMAIL_ID')
your_password = os.environ.get('EMAIL_PASSWORD')
receiver_email = input("Enter Reciever Email")
subject = input("Enter subject of the Email")

send_message(your_email,your_password,reciever_email,subject,cipher_text)
```

## 4. Get back our plain text

```python
from pyconfidentiality import decrypt_message
print("Decrypted message: {}".format(decrypt(cipher_obj, private_key)))
```

<h2 align= "center"><b> Project Maintainers</b></h2>
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->

## Usage

_For more examples, please refer to the [Notebook](https://github.com/tuhinmallick/pyMorse/blob/main/notebooks/Insider_trading_analysis.ipynb)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->

## Roadmap

- [x] Feature 1
- [x]  Feature 2
- [ ] Feature 3
  - [ ] Nested Feature

See the [open issues](https://github.com/tuhinmallick/pyMorse/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

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

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->

## 🛡 License

[![License](https://img.shields.io/github/license/tuhinmallick/pyMorse)](https://github.com/tuhinmallick/pyMorse/blob/master/LICENSE)

This project is licensed under the terms of the `MIT` license. See [LICENSE](https://github.com/tuhinmallick/pyMorse/blob/master/LICENSE) for more details.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Authors

- [@tuhinmallick](https://www.github.com/tuhinmallick)

<!-- CONTACT -->

## Contact

Your Name - [@tuhinmallick](https://twitter.com/tuhinmallick) - tuhin.mllk@gmail.com

Project Link: [https://github.com/tuhinmallick/pyMorse](https://github.com/tuhinmallick/pyMorse)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->

## Acknowledgments

- [ilyaryabov](https://www.kaggle.com/datasets/ilyaryabov/insider-trading-sp500-inside-info)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/tuhinmallick/pyMorse.svg?style=for-the-badge
[contributors-url]: https://github.com/tuhinmallick/pyMorse/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/tuhinmallick/pyMorse.svg?style=for-the-badge
[forks-url]: https://github.com/tuhinmallick/pyMorse/network/members
[stars-shield]: https://img.shields.io/github/stars/tuhinmallick/pyMorse.svg?style=for-the-badge
[stars-url]: https://github.com/tuhinmallick/pyMorse/stargazers
[issues-shield]: https://img.shields.io/github/issues/tuhinmallick/pyMorse.svg?style=for-the-badge
[issues-url]: https://github.com/tuhinmallick/pyMorse/issues
[license-shield]: https://img.shields.io/github/license/tuhinmallick/pyMorse.svg?style=for-the-badge
[license-url]: https://github.com/tuhinmallick/pyMorse/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/tuhinmallick
