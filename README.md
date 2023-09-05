<div align="center">
<h1 align="center">
<img src="https://cdn-icons-png.flaticon.com/512/6133/6133884.png" width="100" />
<br>ChatCSV
</h1>
<h3>◦ Connect. Collaborate. Convert. ChatCSV.</h3>
<h3>◦ Developed with the software and tools listed below.</h3>
<br/>
<p align="center">
<img src="https://img.shields.io/badge/Streamlit-FF4B4B.svg?style&logo=Streamlit&logoColor=white" alt="Streamlit" />
<img src="https://img.shields.io/badge/OpenAI-412991.svg?style&logo=OpenAI&logoColor=white" alt="OpenAI" />
<img src="https://img.shields.io/badge/Python-3776AB.svg?style&logo=Python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/pandas-150458.svg?style&logo=pandas&logoColor=white" alt="pandas" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style&logo=Markdown&logoColor=white" alt="Markdown" />
 &nbsp; <span> <b>🦜️🔗 LangChain</b></span>
</p>
<br/>
</div>

---

## 📒 Table of Contents
- [📒 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [⚙️ Features](#️-features)
- [🧩 Modules](#-modules)
- [🚀 Getting Started](#-getting-started)
  - [✔️ Prerequisites](#️-prerequisites)
  - [📦 Installation](#-installation)
  - [🎮 Using ChatCSV](#-using-chatcsv)
- [🤝 Contributing](#-contributing)

---


## 📍 Overview

The ChatCSV project is a Streamlit application that enables users to upload a CSV file and ask statistical questions about its contents. It leverages the ChatOpenAI model to interpret and answer user queries. The purpose of this project is to provide an intuitive interface for data analysis, allowing users to gain insights from their datasets without the need for complex coding or data manipulation. Its value proposition lies in its simplicity and effectiveness in transforming raw data into actionable insights through natural language queries.

---

## ⚙️ Features

| Feature                | Description                           |
| ---------------------- | ------------------------------------- |
| **⚙️ Architecture**     | The system follows a client-server architecture where the Streamlit application interacts with the langchain library's ChatOpenAI model. The codebase is designed as a single-file application, with the main functionality implemented in the `app.py` script. |
| **🔗 Dependencies**    | The codebase relies on external dependencies such as the langchain library, Streamlit, Pandas, and Requests. These libraries are crucial for the functionality of the application and handling CSV operations. |
| **🧩 Modularity**      | The codebase is organized into a simple modular structure.|
| **⚡️ Performance**      | Performance depends largely on the langchain library and the underlying models it uses. No specific performance optimizations or benchmarks are implemented in the codebase. Performance can be improved by optimizing code, managing resources efficiently, and caching/query optimization in the underlying libraries. |
| **🔀 Version Control** | Version control for the project is managed using Git, as evident from the GitHub repository. Proper commit messages and descriptive branches facilitate collaboration and code maintenance.  |
| **🔌 Integrations**    | The system primarily interacts with the Streamlit framework for providing the web-based user interface. The system integrates with the OpenAI ChatOpenAI model from the langchain library to provide interpretive and answering capabilities. |

---

## 🧩 Modules

<details closed><summary>Root</summary>

| File                                                             | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ---                                                              | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [app.py](https://github.com/rahul2002m/ChatCSV/blob/main/app.py) | The code is a Streamlit application called ChatCSV. It allows users to upload a CSV file and ask statistical questions about its content. The application uses the ChatOpenAI model from the langchain library to interpret and answer user queries. The main function configures the Streamlit page, accepts CSV file uploads, takes user input for questions, processes the questions using the ChatOpenAI model, and displays the model's response. To run the application, execute the script after installing the required dependencies and setting the OpenAI API key. |

</details>

---

## 🚀 Getting Started

### ✔️ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> - `pip install langchain`
> - `pip install openai`
> - `pip install pandas`
> - `pip install streamlit`

### 📦 Installation

1. Clone the ChatCSV repository:
```sh
git clone https://github.com/rahul2002m/ChatCSV
```

2. Change to the project directory:
```sh
cd ChatCSV
```

3. Install the dependencies:
```sh
pip install -r requirements.txt
```

### 🎮 Using ChatCSV

```sh
streamlit run app.py
```
---

## 🤝 Contributing

Contributions are always welcome! Please follow these steps:
1. Fork the project repository. This creates a copy of the project on your account that you can modify without affecting the original project.
2. Clone the forked repository to your local machine using a Git client like Git or GitHub Desktop.
3. Create a new branch with a descriptive name (e.g., `new-feature-branch` or `bugfix-issue-123`).
```sh
git checkout -b new-feature-branch
```
4. Make changes to the project's codebase.
5. Commit your changes to your local branch with a clear commit message that explains the changes you've made.
```sh
git commit -m 'Implemented new feature.'
```
6. Push your changes to your forked repository on GitHub using the following command
```sh
git push origin new-feature-branch
```
7. Create a new pull request to the original project repository. In the pull request, describe the changes you've made and why they're necessary.
The project maintainers will review your changes and provide feedback or merge them into the main branch.

---
