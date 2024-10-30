import os
import subprocess
import tkinter as tk
from tkinter import ttk, messagebox

def run_ansible_playbook(playbook_file, pem_path, inventory_file, ansible_user):
    # Prepare the ansible command
    command = [
        "ansible-playbook",
        playbook_file,
        "-i", inventory_file,
        "--extra-vars", f"ansible_ssh_private_key_file={pem_path} ansible_user={ansible_user}",
        "-vvv"  # Add verbosity for debugging
    ]

    # Execute the ansible-playbook command
    result = subprocess.run(command, capture_output=True, text=True)

    # Print the output for debugging
    print("STDOUT:", result.stdout)
    print("STDERR:", result.stderr)

    if result.returncode == 0:
        messagebox.showinfo("Success", "Tools installed successfully!")
    else:
        messagebox.showerror("Error", f"Ansible error: {result.stderr}")

def create_inventory_file(inventory_file, ec2_ip, pem_path, ansible_user):
    with open(inventory_file, 'w') as f:
        f.write(f"[ec2]\n{ec2_ip} ansible_ssh_private_key_file={pem_path} ansible_user={ansible_user}\n")

def on_submit():
    os_type = os_combobox.get()
    tools = tools_listbox.curselection()
    pem_path = pem_entry.get()
    ec2_ip = ec2_ip_entry.get()
    ansible_user = username_entry.get()

    if not os_type or not tools or not pem_path or not ec2_ip or not ansible_user:
        messagebox.showwarning("Warning", "Please fill all fields!")
        return

    # Convert selected tools to their names
    selected_tools = [tools_listbox.get(i) for i in tools]

    #Create Inventory File
    inventory_file = 'inventory.ini'
    create_inventory_file(inventory_file, ec2_ip, pem_path, ansible_user)

    # Map tools to their corresponding playbooks
    playbook_mapping = {
        "nginx": "ansible-playbooks/install_nginx.yml",
        "redis": "ansible-playbooks/install_redis.yml",
        "apache": "ansible-playbooks/install_apache.yml",
        "openssh": "ansible-playbooks/install_openssh.yml",
        "nodejs": "ansible-playbooks/install_nodejs.yml",
        "java21": "ansible-playbooks/install_java21.yml",
        "java17": "ansible-playbooks/install_java17.yml",
        "python": "ansible-playbooks/install_python.yml",
        "postgresql": "ansible-playbooks/install_postgresql.yml",
    }

    # Run Ansible playbooks for selected tools
    for tool in selected_tools:
        playbook_file = playbook_mapping.get(tool)
        if playbook_file:
            run_ansible_playbook(playbook_file, pem_path, inventory_file, ansible_user)
        else:
            messagebox.showwarning("Warning", f"No playbook found for {tool}")

# Create the main window
root = tk.Tk()
root.title("Ansible Tool Installer")

# OS Selection
os_label = tk.Label(root, text="Select OS:")
os_label.pack()

os_combobox = ttk.Combobox(root, values=["ubuntu", "fedora", "centos", "redhat", "almalinux", "rhel"])
os_combobox.pack()

# Tools Selection
tools_label = tk.Label(root, text="Select Tools:")
tools_label.pack()

tools_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
tools_list = ["nginx", "redis", "apache", "openssh", "nodejs", "java21", "java17", "python", "postgresql"]
for tool in tools_list:
    tools_listbox.insert(tk.END, tool)
tools_listbox.pack()

# PEM File Entry
pem_label = tk.Label(root, text="Path to .pem file:")
pem_label.pack()

pem_entry = tk.Entry(root)
pem_entry.pack()

# EC2 IP Entry
ec2_ip_label = tk.Label(root, text="EC2 Instance Public IP:")
ec2_ip_label.pack()

ec2_ip_entry = tk.Entry(root)
ec2_ip_entry.pack()

# Username Entry
username_label = tk.Label(root, text="Ansible Username:")
username_label.pack()

username_entry = tk.Entry(root)
username_entry.pack()

# Submit Button
submit_button = tk.Button(root, text="Install", command=on_submit)
submit_button.pack()

# Run the application
root.mainloop()
