
# Network Scanner for Raspberry Pi Devices

## Overview

This Network Scanner is a powerful, user-friendly tool designed to help users easily find Raspberry Pi devices within their local network. Built with PyQt5 and leveraging the capabilities of the nmap library, it provides a graphical user interface (GUI) for scanning and identifying devices. Whether you're managing multiple Raspberry Pis in a network or just trying to locate your device, this tool streamlines the process by displaying the devices' IP and MAC addresses, highlighting Raspberry Pis for easy identification.

## Features

- **Simple Interface**: A clean, intuitive GUI makes scanning your network as easy as clicking a button.
- **Auto-Detect Network Range**: Automatically detects and fills in your network range based on your current IP address.
- **Raspberry Pi Highlighting**: Raspberry Pi devices are highlighted, making them easy to spot among other networked devices.
- **Customizable Scanning**: Offers the option to display only Raspberry Pi devices or all devices found in the scan.
- **Error Handling**: Provides feedback in case of scanning errors or issues.

## Installation

### Prerequisites

Before you can run the Network Scanner, you must have Python installed on your system (Python 3.6 or newer is recommended). Additionally, ensure you have PyQt5 and nmap Python library installed.

### Installing Dependencies

1. Install PyQt5:

    ```bash
    pip install PyQt5
    ```

2. Install python-nmap:

    ```bash
    pip install python-nmap
    ```

### Running the Application

To run the Network Scanner, clone this repository or download the source code. Navigate to the directory containing the code and run the following command:

```bash
python network_scanner.py
```

## Usage

Upon launching the Network Scanner, the application will display your network range. You can adjust this range if necessary. Click the "Scan" button to start scanning your network. Results will appear in the main window, with Raspberry Pi devices highlighted for easy identification. You can choose to display only Raspberry Pi devices by checking the "Only display Raspberry Pi devices" option.

## Contributing

Contributions to the Network Scanner are welcome! Whether it's bug fixes, feature suggestions, or code contributions, feel free to fork the repository and submit a pull request. Please read [CONTRIBUTING.md](CONTRIBUTING.md) for more information on how to contribute.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the developers of PyQt5 and the python-nmap library for making network scanning accessible to Python applications.
- This project is inspired by the need to easily locate and manage Raspberry Pi devices in networked environments.
