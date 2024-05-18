# Distributed Image Processing System using Cloud Computing

## Table of Contents
- [Introduction](#introduction)
- [Features and Specifications](#features-and-specifications)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [System Architecture](#system-architecture)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction
This project aims to develop a distributed image processing system using cloud computing technologies. The system is implemented in Python, leveraging cloud-based virtual machines for distributed computing. The application utilizes OpenCL or MPI for parallel processing of image data. This project is designed to be completed by teams of 3 to 4 students.

## Features and Specifications
- **Distributed Processing**: The system distributes image processing tasks across multiple virtual machines in the cloud.
- **Image Processing Algorithms**: Implements various image processing algorithms such as filtering, edge detection, and color manipulation.
- **Scalability**: The system is scalable, allowing for the addition of more virtual machines as the workload increases.
- **Fault Tolerance**: The system is resilient to failures, with the ability to reassign tasks from failed nodes to operational ones.

## Setup and Installation
### Prerequisites
- Python 3.x
- Virtual Machines (VMs) on a cloud platform (e.g., AWS in our Case)
- OpenCL or MPI libraries installed on each VM

### Installation Steps
1. **Clone the Repository**
   ```bash
   git clone https://github.com/adham137/cloud_image_processing.git
   cd distributed-image-processing
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Cloud VMs**
   - Set up the virtual machines on your chosen cloud platform.
   - Ensure all VMs have Python and the necessary libraries (OpenCL or MPI) installed.
   - Configure SSH access between VMs for seamless communication.

4. **Deploy the Application**
   - Copy the application code to each VM.
   - Use a configuration management tool for setting up the environment and deploying the application on all VMs.

## Usage
### Running the Application
1. **Start the Master Node**
   ```bash
   python3 master.py
   ```

2. **Start Worker Nodes on Each VM**
   ```bash
   python worker.py
   ```

3. **Submit Image Processing Tasks**
   - Use the provided client interface to submit image processing tasks to the master node.
   - The master node will distribute tasks to available worker nodes.

### Example Commands
```bash
# Submit a task for edge detection on an image
python client.py --task edge_detection --image_path /path/to/image.jpg
```

## System Architecture
### Components
- **Master Node**: Manages task distribution and fault tolerance.
- **Worker Nodes**: Perform the actual image processing tasks.
- **Client Interface**: Submits tasks to the master node.

### Data Flow
1. The client submits a task to the master node.
2. The master node divides the task into subtasks and distributes them to worker nodes.
3. Worker nodes process the subtasks and return the results to the master node.
4. The master node aggregates the results and sends the final output back to the client.

## Contributing
### Team Members
- [Member 1](mailto:20P2084@eng.asu.edu.eg)
- [Member 2](mailto:20P1005@eng.asu.edu.eg)
- [Member 3](mailto:20P9705@eng.asu.edu.eg)


### Guidelines
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push to your branch.
4. Create a pull request with a detailed description of your changes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact
For questions or further information, please contact the project team
