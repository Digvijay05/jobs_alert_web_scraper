<div id="top">

<!-- HEADER STYLE: COMPACT -->

# JOBS_ALERT_WEB_SCRAPER.GIT
<em>Automate job alerts. Never miss the perfect opportunity again.</em>

<em>Built with the tools and technologies:</em>

<img src="https://img.shields.io/badge/Selenium-43B02A.svg?style=flat-square&logo=Selenium&logoColor=white" alt="Selenium">
<img src="https://img.shields.io/badge/Gunicorn-499848.svg?style=flat-square&logo=Gunicorn&logoColor=white" alt="Gunicorn">
<img src="https://img.shields.io/badge/Celery-37814A.svg?style=flat-square&logo=Celery&logoColor=white" alt="Celery">
<img src="https://img.shields.io/badge/Django-092E20.svg?style=flat-square&logo=Django&logoColor=white" alt="Django">
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat-square&logo=Python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/GitHub%20Actions-2088FF.svg?style=flat-square&logo=GitHub-Actions&logoColor=white" alt="GitHub%20Actions">

<br clear="left"/>

## ☀️ Table of Contents

<details>
<summary>Table of Contents</summary>

- [☀ ️ Table of Contents](#-table-of-contents)
- [🌞 Overview](#-overview)
- [🔥 Features](#-features)
- [🌅 Project Structure](#-project-structure)
    - [🌄 Project Index](#-project-index)
- [🚀 Getting Started](#-getting-started)
    - [🌟 Prerequisites](#-prerequisites)
    - [⚡ Installation](#-installation)
    - [🔆 Usage](#-usage)
    - [🌠 Testing](#-testing)
- [🌻 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [📜 License](#-license)
- [✨ Acknowledgments](#-acknowledgments)

</details>

---

## 🌞 Overview

Jobs Alert Web Scraper is a Django-based automation tool that programmatically scrapes job-related content from external websites and transforms it into structured posts for your platform. It provides a complete backend system for managing recruitment announcements through a REST API and admin interface.

**Why jobs_alert_web_scraper?**

This project eliminates manual content creation by automating job posting ingestion while maintaining data integrity and uniqueness. The core features include:

- **🔵 Automated Content Scraping:** Programmatically extracts job details like qualifications, deadlines, and fees from external sources
- **🟢 REST API Management:** Exposes comprehensive endpoints for listing, retrieving, and managing posts with serialized JSON data
- **🟡 Django Admin Interface:** Provides centralized oversight for posts, vacancies, qualifications, and related metadata
- **🟠 Push Notification System:** Integrates with APNs and FCM to deliver alerts, badges, and sounds across platforms
- **🟣 Production-Ready Deployment:** Configured for Heroku with Gunicorn WSGI server and ASGI compatibility
- **🔴 Continuous Integration:** Automated testing workflow with PostgreSQL ensures code reliability throughout development

---

## 🔥 Features

|      | Component       | Details                                                                                                |
| :--- | :-------------- | :----------------------------------------------------------------------------------------------------- |
| ⚙️  | **Architecture**  | <ul><li>Django-based web application</li><li>Uses Celery for async task processing</li><li>Heroku deployment via Procfile</li></ul> |
| 🔩 | **Code Quality**  | <ul><li>Uses `python-decouple` for config management</li><li>Contains `.github/workflows/django.yml` for CI/CD</li><li>Requires linting/tests (none evident)</li></ul> |
| 📄 | **Documentation** | <ul><li>No visible docs/README</li><li>Relies on requirements.txt for dependency specs</li></ul> |
| 🔌 | **Integrations**  | <ul><li>**Web scraping**: `selenium`, `beautifulsoup4`, `requests`, `lxml`</li><li>**Database**: `psycopg2`, `dj-database-url`</li><li>**APIs**: `djangorestframework`</li><li>**Message Broker**: `kombu`, `amqp` (Celery)</li></ul> |
| 🧩 | **Modularity**    | <ul><li>Django app structure implied</li><li>Uses `django-crontab` & `APScheduler` for job scheduling</li><li>Separate scraping logic via dedicated libraries</li></ul> |
| 🧪 | **Testing**       | <ul><li>No testing frameworks listed in dependencies</li><li>GitHub Actions CI configured (`django.yml`)</li></ul> |
| ⚡️  | **Performance**   | <ul><li>**Caching**: `whitenoise` for static files</li><li>**Async**: Celery for background scraping jobs</li><li>**DB pooling**: `dj-database-url` for PostgreSQL</li></ul> |
| 🛡️ | **Security**      | <ul><li>`certifi` for SSL certs</li><li>`django-cors-headers` for CORS management</li><li>Uses `python-decouple` to keep secrets out of code</li></ul> |
| 📦 | **Dependencies**  | <ul><li>**Scraping**: `selenium`, `beautifulsoup4`, `lxml`</li><li>**Backend**: `Django`, `gunicorn`, `djangorestframework`</li><li>**Async**: `celery`, `kombu`, `billiard`</li><li>**DB**: `psycopg2`, `sqlparse`</li></ul> |

---

## 🌅 Project Structure

```sh
└── jobs_alert_web_scraper.git/
    ├── .github
    │   └── workflows
    ├── Posts
    │   ├── __init__.py
    │   ├── __pycache__
    │   ├── admin.py
    │   ├── apps.py
    │   ├── migrations
    │   ├── models.py
    │   ├── serializers.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── Procfile
    ├── jadavjobs_admin
    │   ├── __init__.py
    │   ├── __pycache__
    │   ├── asgi.py
    │   ├── classes.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── manage.py
    ├── pgpush
    └── requirements.txt
```

### 🌄 Project Index

<details open>
	<summary><b><code>JOBS_ALERT_WEB_SCRAPER.GIT/</code></b></summary>
	<!-- __root__ Submodule -->
	<details>
		<summary><b>__root__</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ __root__</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Digvijay05/jobs_alert_web_scraper.git/blob/master/requirements.txt'>requirements.txt</a></b></td>
					<td style='padding: 8px;'>- Lists third-party dependencies required to build and operate the web application, ensuring consistent environment setup across development and production<br>- It defines the foundational libraries for backend services, task scheduling, database management, and external API interactions, supporting core functionalities like asynchronous processing, web scraping, and REST API delivery<br>- The constraints enable reliable deployment and collaboration by pinning specific package versions.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Digvijay05/jobs_alert_web_scraper.git/blob/master/pgpush'>pgpush</a></b></td>
					<td style='padding: 8px;'>- Handles asynchronous push notification delivery to users across platforms like iOS, Android, and web<br>- Integrates with providers like APNs and FCM to send alerts, badges, and sounds<br>- Schedules and retries failed notifications while ensuring reliable delivery<br>- Supports batching, priority settings, and logging for monitoring<br>- Fits into the broader messaging workflow to enhance user engagement.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Digvijay05/jobs_alert_web_scraper.git/blob/master/manage.py'>manage.py</a></b></td>
					<td style='padding: 8px;'>- Manages administrative tasks for the Django-based web application by serving as the primary command-line entry point<br>- It initializes the required environment and dispatches commands to the appropriate Django management modules, enabling essential operations such as running the development server, handling database migrations, and interacting with the application’s core functionality without directly modifying business logic or application data.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Digvijay05/jobs_alert_web_scraper.git/blob/master/Procfile'>Procfile</a></b></td>
					<td style='padding: 8px;'>- Defines the web process command for running the Django application in a production environment on a PaaS platform like Heroku<br>- It specifies using Gunicorn as the WSGI HTTP server to serve the <code>jadavjobs_admin</code> project, configuring a request timeout and keep-alive duration to ensure stable and responsive handling of incoming web traffic<br>- This entrypoint is essential for deployment and scalability.</td>
				</tr>
			</table>
		</blockquote>
	</details>
	<!-- jadavjobs_admin Submodule -->
	<details>
		<summary><b>jadavjobs_admin</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ jadavjobs_admin</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Digvijay05/jobs_alert_web_scraper.git/blob/master/jadavjobs_admin/wsgi.py'>wsgi.py</a></b></td>
					<td style='padding: 8px;'>- Facilitates deployment of the Jadav Jobs admin application by providing a standard interface for production web servers<br>- Sets the necessary Django settings and initializes the WSGI callable, enabling smooth traffic handling between the server and the Django framework<br>- This is essential for running the platform in a live environment.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Digvijay05/jobs_alert_web_scraper.git/blob/master/jadavjobs_admin/urls.py'>urls.py</a></b></td>
					<td style='padding: 8px;'>- Serves as the central routing configuration for the Django-based jadavjobs_admin application, directing web requests to appropriate endpoints<br>- It maps URLs to the Django admin interface, REST framework admin, and the core API handled by the Posts app<br>- This setup organizes and exposes administrative and API functionalities, forming the primary entry point for managing the applications backend services and static file handling.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Digvijay05/jobs_alert_web_scraper.git/blob/master/jadavjobs_admin/settings.py'>settings.py</a></b></td>
					<td style='padding: 8px;'>- Configures the Django project for the JadavJobs admin platform, establishing core behaviors across the entire application<br>- It manages database connections, integrates necessary components for a REST API, and enables CORS for frontend communication<br>- The settings also prepare static files for production deployment and initialize Heroku-specific configurations to support the hosting environment.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Digvijay05/jobs_alert_web_scraper.git/blob/master/jadavjobs_admin/classes.py'>classes.py</a></b></td>
					<td style='padding: 8px;'>- Based on the project structure and code provided, the <code>Worker</code> class in <code>classes.py</code> serves as the core automation engine within the <code>jadavjobs_admin</code> module<br>- It is responsible for programmatically scraping job-related content (such as announcements, qualifications, deadlines, and fees) from external websites and transforming that data into structured, original posts for the platform, thereby streamlining content creation while maintaining uniqueness<br>- This class bridges external data sources with the platforms internal models, enabling rapid, scalable content generation.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Digvijay05/jobs_alert_web_scraper.git/blob/master/jadavjobs_admin/asgi.py'>asgi.py</a></b></td>
					<td style='padding: 8px;'>- Entry point for the Django projects ASGI server, enabling asynchronous web server compatibility<br>- It initializes the application using project settings, making the web service ready for deployment on ASGI-compliant servers<br>- This setup is essential for running the JadavJobs admin interface in modern asynchronous environments, bridging the core application with the hosting infrastructure.</td>
				</tr>
			</table>
		</blockquote>
	</details>
	<!-- Posts Submodule -->
	<details>
		<summary><b>Posts</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ Posts</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Digvijay05/jobs_alert_web_scraper.git/blob/master/Posts/views.py'>views.py</a></b></td>
					<td style='padding: 8px;'>- Serves as the primary API interface for the Posts application, defining endpoints that manage and expose post-related data<br>- Handles listing all available API routes, generating links to individual posts, and fetching both summarized and detailed post information<br>- It also supports administrative functions such as deleting all posts and triggering an external data ingestion worker, centralizing core data access and management operations for the system.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Digvijay05/jobs_alert_web_scraper.git/blob/master/Posts/urls.py'>urls.py</a></b></td>
					<td style='padding: 8px;'>- Defines the URL routing schema for the Posts API, mapping incoming HTTP requests to their corresponding view functions<br>- It establishes endpoints for general API information, retrieving posts and links, managing individual posts, deleting all data, fetching a random post, and initiating background worker processes<br>- This structure provides the public interface for interacting with the applications core data and services.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Digvijay05/jobs_alert_web_scraper.git/blob/master/Posts/tests.py'>tests.py</a></b></td>
					<td style='padding: 8px;'>- Tests the API endpoint responses within the Posts application, ensuring the primary API overview and links endpoints return successful HTTP status codes<br>- This validation confirms that key paths are accessible and responsive, supporting reliability across the application structure and contributing to overall system integrity by verifying core routes function correctly without delving into backend logic or data specifics.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Digvijay05/jobs_alert_web_scraper.git/blob/master/Posts/serializers.py'>serializers.py</a></b></td>
					<td style='padding: 8px;'>- Serializers define how model data structures convert to and from JSON format for API communication, specifically handling posts and related entities like fees, dates, qualifications, vacancies, comments, and links<br>- They ensure consistent data validation and presentation across all endpoints, enabling seamless frontend-backend interactions for managing detailed post information within the application.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Digvijay05/jobs_alert_web_scraper.git/blob/master/Posts/models.py'>models.py</a></b></td>
					<td style='padding: 8px;'>- Defines core data models for managing structured job or announcement posts within a Django application<br>- The primary Post model aggregates related information such as application fees, important dates, qualification requirements, vacancy details, and important links through separate, reusable list models<br>- This architecture centralizes post-related content management, enabling consistent organization and presentation of complex, multi-faceted information<br>- A Comment model supports user feedback on published posts.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Digvijay05/jobs_alert_web_scraper.git/blob/master/Posts/apps.py'>apps.py</a></b></td>
					<td style='padding: 8px;'>- PostsConfig is a Django application configuration class that governs the Posts module within the larger project<br>- It establishes the primary identifier for database models and officially registers the app, enabling its integration with Django’s core systems<br>- This setup ensures seamless operation alongside other project components, contributing to the overall modularity and organization of the codebase.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/Digvijay05/jobs_alert_web_scraper.git/blob/master/Posts/admin.py'>admin.py</a></b></td>
					<td style='padding: 8px;'>- Registers Post-related models with the Django admin interface, enabling administrative management of critical data such as fees, important dates, age limits, vacancies, qualifications, and associated links or comments<br>- This integration supports centralized oversight for content and metadata tied to recruitment or informational posts, facilitating streamlined backend operations.</td>
				</tr>
			</table>
			<!-- migrations Submodule -->
			<details>
				<summary><b>migrations</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ Posts.migrations</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/Digvijay05/jobs_alert_web_scraper.git/blob/master/Posts/migrations/0003_vacancy_list_row_number.py'>0003_vacancy_list_row_number.py</a></b></td>
							<td style='padding: 8px;'>- Introduces a row number field to the vacancy list model within the Posts app, supporting optional identification or ordering of entries<br>- This database schema change enhances data organization by allowing each vacancy record to store a custom row identifier<br>- The migration builds on prior modifications, ensuring incremental and orderly evolution of the applications data structure without disrupting existing functionality.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/Digvijay05/jobs_alert_web_scraper.git/blob/master/Posts/migrations/0002_alter_links_list_download_file.py'>0002_alter_links_list_download_file.py</a></b></td>
							<td style='padding: 8px;'>- Adjusts an existing database schema for storing file uploads in the Posts app by modifying the download_file field to allow optional values and specifying a structured storage path<br>- This migration ensures flexibility for posts with downloadable content while maintaining organized file storage within the project’s static assets directory.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/Digvijay05/jobs_alert_web_scraper.git/blob/master/Posts/migrations/0001_initial.py'>0001_initial.py</a></b></td>
							<td style='padding: 8px;'>- Initializes core database schema for a posts system, defining models to store recruitment-related details like vacancies, qualifications, age limits, and fees<br>- Links supporting data such as important dates, downloadable links, and comments to each post<br>- Establishes structural relationships to organize hierarchical content, enabling the application to manage job postings comprehensively and maintain relational data integrity across interconnected tables.</td>
						</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
	<!-- .github Submodule -->
	<details>
		<summary><b>.github</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ .github</b></code>
			<!-- workflows Submodule -->
			<details>
				<summary><b>workflows</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ .github.workflows</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/Digvijay05/jobs_alert_web_scraper.git/blob/master/.github/workflows/django.yml'>django.yml</a></b></td>
							<td style='padding: 8px;'>- A GitHub Actions workflow automating continuous integration for the Django project<br>- It orchestrates the execution of automated tests within a controlled environment featuring a PostgreSQL database<br>- This ensures code reliability by validating changes against a defined test suite upon each push, maintaining project stability and preventing regressions throughout the development lifecycle<br>- The process is a core component of the codebases quality assurance strategy.</td>
						</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
</details>

---

## 🚀 Getting Started

### 🌟 Prerequisites

This project requires the following dependencies:

- **Programming Language:** Python
- **Package Manager:** Pip

### ⚡ Installation

Build jobs_alert_web_scraper.git from the source and intsall dependencies:

1. **Clone the repository:**

    ```sh
    ❯ git clone https://github.com/Digvijay05/jobs_alert_web_scraper.git
    ```

2. **Navigate to the project directory:**

    ```sh
    ❯ cd jobs_alert_web_scraper.git
    ```

3. **Install the dependencies:**

<!-- SHIELDS BADGE CURRENTLY DISABLED -->
	<!-- [![pip][pip-shield]][pip-link] -->
	<!-- REFERENCE LINKS -->
	<!-- [pip-shield]: https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white -->
	<!-- [pip-link]: https://pypi.org/project/pip/ -->

	**Using [pip](https://pypi.org/project/pip/):**

	```sh
	❯ pip install -r requirements.txt
	```

### 🔆 Usage

Run the project with:

**Using [pip](https://pypi.org/project/pip/):**
```sh
python {entrypoint}
```

### 🌠 Testing

Jobs_alert_web_scraper.git uses the {__test_framework__} test framework. Run the test suite with:

**Using [pip](https://pypi.org/project/pip/):**
```sh
pytest
```

---

## 🌻 Roadmap

- [X] **`Task 1`**: <strike>Implement feature one.</strike>
- [ ] **`Task 2`**: Implement feature two.
- [ ] **`Task 3`**: Implement feature three.

---

## 🤝 Contributing

- **💬 [Join the Discussions](https://github.com/Digvijay05/jobs_alert_web_scraper.git/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/Digvijay05/jobs_alert_web_scraper.git/issues)**: Submit bugs found or log feature requests for the `jobs_alert_web_scraper.git` project.
- **💡 [Submit Pull Requests](https://github.com/Digvijay05/jobs_alert_web_scraper.git/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/Digvijay05/jobs_alert_web_scraper.git
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/Digvijay05/jobs_alert_web_scraper.git/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=Digvijay05/jobs_alert_web_scraper.git">
   </a>
</p>
</details>

---

## 📜 License

Jobs_alert_web_scraper.git is protected under the [LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## ✨ Acknowledgments

- Credit `contributors`, `inspiration`, `references`, etc.

<div align="right">

[![][back-to-top]](#top)

</div>


[back-to-top]: https://img.shields.io/badge/-BACK_TO_TOP-151515?style=flat-square


---
