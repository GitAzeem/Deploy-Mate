# Deploy-Mate
Deploy-Mate is a user-friendly tool that simplifies the installation and configuration of essential software using Ansible on your cloud instances. With a sleek interface, it streamlines the process, making DevOps tasks effortless and efficient.

## Features

- **Ansible Playbooks**: Supports installation of common tools like Nginx, Redis, Apache, OpenSSH, Node.js, different versions of Java, Python, and PostgreSQL.
- **User-Friendly GUI**: Built with Python's Tkinter module, allowing users to easily select tools and provide necessary details.
- **Automated Inventory File Creation**: Generates an Ansible inventory file based on the user's input.

## Prerequisites

Before running this application, ensure you have the following:

- **Python 3.x**
- **Ansible** installed on your local machine.
- **.pem file** to access your EC2 instance.
- **Ansible Playbooks** for each supported tool/service.

## Supported Tools

- **Nginx**
- **Redis**
- **Apache**
- **OpenSSH**
- **Node.js**
- **Java 21**
- **Java 17**
- **Python**
- **PostgreSQL**

## Project Structure

```
.
├── ansible-playbooks/
│   ├── install_nginx.yml
│   ├── install_redis.yml
│   ├── install_apache.yml
│   ├── install_openssh.yml
│   ├── install_nodejs.yml
│   ├── install_java21.yml
│   ├── install_java17.yml
│   ├── install_python.yml
│   └── install_postgresql.yml
├── inventory.ini          # Generated automatically based on user input
├── ansible_tool_installer.py  # Main Python script containing the GUI
└── README.md              # Project documentation
```

## How to Run

1. **Clone or download the repository** to your local machine.
2. **Install the necessary Python packages**:
   ```bash
   pip install tkinter
   ```
3. **Run the Python script**:
   ```bash
   python ansible_tool_installer.py
   ```
4. **Fill in the required fields** in the GUI:
   - Select your Operating System (e.g., Ubuntu, Fedora, CentOS).
   - Select the tools you want to install.
   - Provide the path to your `.pem` file.
   - Enter the public IP address of your EC2 instance.
   - Provide the Ansible username (e.g., `ec2-user` for Amazon Linux or `ubuntu` for Ubuntu).

5. **Click on the "Install" button** to run the Ansible playbooks.

## How It Works

1. The **GUI** collects user input and generates an Ansible inventory file named `inventory.ini`.
2. The selected tools are mapped to their corresponding playbooks in the `ansible-playbooks` folder.
3. The **Ansible playbook commands** are constructed dynamically and executed using Python's `subprocess` module.
4. Output and error messages are displayed to the user to help identify installation success or failure.

## Ansible Playbooks

Ensure that you have all necessary Ansible playbooks in the `ansible-playbooks` directory. Each playbook should handle the installation of a specific service. Below is an example structure for an Ansible playbook (`install_nginx.yml`):

```yaml
---
- hosts: ec2
  become: true
  tasks:
    - name: Install Nginx
      apt:
        name: nginx
        state: present
```

## Contributing

If you'd like to contribute or improve this project, feel free to fork the repository and create a pull request with your changes.

