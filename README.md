# SQL Injection Lab

![SQL Injection](https://img.shields.io/badge/SQL-Injection-red.svg)

## Table of Contents
- [Introduction](#introduction)
- [Major Requirement](#major-requirement)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

SQL injection is a prevalent security vulnerability in web applications. This CLI-based lab mimics actual login functionality, featuring both registration and login processes. Its primary goal is to emphasize the critical importance of using parameterized queries in developer's code. By interacting with this lab, users can gain practical insights into the risks associated with insecure coding practices and the potential impact of SQL injection attacks on web applications.

## Major Requirement

Make sure you have the latest versions of `Python` and `PostgreSQL` installed on your system.

(Optional) It's beneficial to install `pgAdmin` if it's not already installed, but it's not mandatory. Similar tasks can be performed using the command-line interface (CLI).

## Project Structure

The project is organized into two main folders:

1. **secure**: This directory contains the secure implementation of the web application, showcasing best practices to prevent SQL injection vulnerabilities.

2. **vulnerable**: This directory contains code with known SQL injection vulnerabilities, allowing users to experiment with SQL injection attacks safely.

Each directory contains a `config.json` file that needs to be configured with PostgreSQL database settings specific to your environment.

## Installation

To get started, clone this repository to your local machine:

```bash
git clone https://github.com/haaris272k/SQL-injection-lab.git
   ```

## Usage

To use the SQL Injection Lab, follow these steps:

1. **Prerequisites**

   (a) cd into the repo and install requirements:

     ```bash
     
     cd SQL-injection-lab
     
     pip install -r requirements.txt
     
     ```
   (b) Make sure you have PostgreSQL installed on your local system.

2. **Configuration**

   (a) Create a database of your choice using either the command-line interface or a tool like pgAdmin.

   (b) Modify the `config.json` file in the `secure` and `vulnerable` folders with your PostgreSQL database settings. You can specify the table name of your choice.
       Enter the exact name of the database you created.

   (c) Once the configurations are set, navigate to either the `secure` or `vulnerable` directory based on your needs.

4. **Running the script**

   Run the script using Python:

   - For the secure version (under the `secure` directory):

     ```bash
     python secure.py
     ```

   - For the vulnerable version (under the `vulnerable` directory):

     ```bash
     python vul.py
     ```

## Contributing

  Contributions to this project are welcome! Here's how you can contribute:

  - **Open Issues**: If you find a bug or have a feature request, please open an issue.
  
  - **Submit Pull Requests**: If you'd like to contribute code, please feel free to submit a pull request.
  
  - **Feedback**: Have suggestions or ideas on how to improve the lab environment? I'd love to hear from you! Provide your feedback.

  Your contributions are valuable and help make this project better for everyone.

## License

  ![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)
  
  This project is licensed under the [MIT License](LICENSE). You are free to use and distribute it as per the terms of the license.
