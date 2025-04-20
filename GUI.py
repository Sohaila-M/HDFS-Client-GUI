import tkinter as tk
from tkinter import messagebox
import subprocess


def start_hdfs():
	try:
		cmd="start-dfs.sh"
		subprocess.run(cmd, shell=True, check=True)
		messagebox.showinfo("Success","HDFS started successfully")
	except subprocess.CalledProcessError as e:
        	messagebox.showerror("Command Failed", f"Error:\n{e}")
def start_yarn():
	try:
		cmd="start-yarn.sh"
		subprocess.run(cmd, shell=True, check=True)
		messagebox.showinfo("Success","YARN started successfully")
	except subprocess.CalledProcessError as e:
        	messagebox.showerror("Command Failed", f"Error:\n{e}")
def stop():
	try:
		cmd="stop-all.sh"
		subprocess.check_output(cmd, shell=True , text=True)
		messagebox.showinfo("Success","Services stopped successfully")
	except subprocess.CalledProcessError as e:
        	messagebox.showerror("Command Failed", f"Error:\n{e}")
def jps():

    try:
        cmd="jps"
        result = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, text=True)
        output_text.delete(1.0, tk.END)  # Clear previous output
        output_text.insert(tk.END, result)
    except subprocess.CalledProcessError as e:
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, f"Command failed:\n{e.output}")
def ls():
    hdfs_file = hdfs_entry.get().strip()

    try:
        cmd=f"hdfs dfs -ls {hdfs_file}"
        result = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, text=True)
        output_text.delete(1.0, tk.END)  # Clear previous output
        output_text.insert(tk.END, result)
    except subprocess.CalledProcessError as e:
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, f"Command failed:\n{e.output}")
def cat():
    hdfs_file = hdfs_entry.get().strip()

    try:
        cmd=f"hdfs dfs -cat {hdfs_file}"
        result = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, text=True)
        output_text.delete(1.0, tk.END)  # Clear previous output
        output_text.insert(tk.END, result)
    except subprocess.CalledProcessError as e:
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, f"Command failed:\n{e.output}")
def append_to_hdfs():
    local_file = local_entry.get().strip()
    hdfs_file = hdfs_entry.get().strip()

    if not local_file or not hdfs_file:
        messagebox.showerror("Error", "Please enter both local file path and HDFS file path.")
        return

    try:

        cmd = f"hdfs dfs -appendToFile {local_file} {hdfs_file}"
        subprocess.run(cmd, shell=True, check=True)
        messagebox.showinfo("Success", f"Appended '{local_file}' to '{hdfs_file}'")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Command Failed", f"Error:\n{e}")
def upload_to_hdfs():
    local_file = local_entry.get().strip()
    hdfs_file = hdfs_entry.get().strip()

    if not local_file or not hdfs_file:
        messagebox.showerror("Error", "Please enter both local file path and HDFS file path.")
        return

    try:

        cmd = f"hdfs dfs -put {local_file} {hdfs_file}"
        subprocess.run(cmd, shell=True, check=True)
        messagebox.showinfo("Success", f"Uploaded '{local_file}' to '{hdfs_file}'")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Command Failed", f"Error:\n{e}")
def download_to_local():
    local_file = local_entry.get().strip()
    hdfs_file = hdfs_entry.get().strip()

    if not local_file or not hdfs_file:
        messagebox.showerror("Error", "Please enter both local file path and HDFS file path.")
        return

    try:

        cmd = f"hdfs dfs -get {hdfs_file} {local_file}"
        subprocess.run(cmd, shell=True, check=True)
        messagebox.showinfo("Success", f"Downloaded '{local_file}' to '{hdfs_file}'")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Command Failed", f"Error:\n{e}")

# GUI 
root = tk.Tk()
root.title("HDFS Client GUI ")
root.configure(bg="#2b2b2b")

# Local file path input
tk.Label(root, bg="#2b2b2b", fg="white", font=("Arial", 16),text="Local File Path:").grid(row=0,column=0 ,pady=5)
local_entry = tk.Entry(root, width=60)
local_entry.grid(row=0,column=1 ,pady=5)

# HDFS file path input
tk.Label(root, bg="#2b2b2b", fg="white", font=("Arial", 16),text="HDFS File Path:").grid(row=1,column=0,pady=5)
hdfs_entry = tk.Entry(root, width=60)
hdfs_entry.grid(row=1,column=1,pady=5)


#Start HDFS
tk.Button(root, text="Start HDFS",  bg="#444444", fg="white", activebackground="#555555", activeforeground="white",font=("Arial", 16),command=start_hdfs).grid(row=2,column=0,pady=15,padx=15)
#Start YARN
tk.Button(root, text="Start YARN", bg="#444444", fg="white", activebackground="#555555", activeforeground="white", font=("Arial", 16),command=start_yarn).grid(row=2,column=1,pady=15)
#Stop all
tk.Button(root, text="Stop all", bg="#444444", fg="white", activebackground="#555555", activeforeground="white",font=("Arial", 16), command=stop).grid(row=2,column=2,pady=15,padx=15)
#jps
tk.Button(root, text="jps",  bg="#444444", fg="white", activebackground="#555555", activeforeground="white",font=("Arial", 16),command=jps).grid(row=3,column=1,pady=15,padx=15)
#List
tk.Button(root, text="List",  bg="#444444", fg="white", activebackground="#555555", activeforeground="white",font=("Arial", 16),command=ls).grid(row=3,column=0,pady=15,padx=15)
#cat
tk.Button(root, text="View file", bg="#444444", fg="white", activebackground="#555555", activeforeground="white",font=("Arial", 16), command=cat).grid(row=3,column=2,pady=15)
output_text = tk.Text(root, height=20, width=100)
output_text.grid(row=6,column=1,pady=10)
# Append button
tk.Button(root, text="Append to HDFS",  bg="#444444", fg="white", activebackground="#555555",font=("Arial", 16), activeforeground="white",command=append_to_hdfs).grid(row=4,column=0,pady=15,padx=15)
# Upload button
tk.Button(root, text="Upload to HDFS", bg="#444444", fg="white", activebackground="#555555", activeforeground="white",font=("Arial", 16), command=upload_to_hdfs).grid(row=4,column=1,pady=15,padx=15)
# Download button
tk.Button(root, text="Download to Local",  bg="#444444", fg="white", activebackground="#555555",font=("Arial", 16), activeforeground="white",command=download_to_local).grid(row=4,column=2,pady=15)

root.mainloop()
