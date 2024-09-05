# Twilio Takeaway Project

## Overview

The Twilio Takeaway Project is a food ordering application developed in Python, designed to provide an intuitive interface for customers to place orders. This project is part of the learning process for Object-Oriented Programming (OOP) principles and API integration. It leverages the Twilio API to send SMS notifications to customers, summarising their order and providing the total amount due. 

## Project Description

This repository contains the complete implementation of the Twilio Takeaway application. Key components include:

- **Interface**: A user-friendly interface that displays available food items along with their prices. The interface allows users to modify and add food items as needed.
- **Order Processing**: The application processes customer orders and calculates the total amount due.
- **SMS Notifications**: Utilises the Twilio API to send an SMS to the customer’s phone number, including an order recap and the total amount due.
- **Logfile Method**: The `SMS` class includes a `logfile` method that creates a text file in the project's directory to log SMS activities.

## Usage

1. **Run the Interface**: To start the application, execute the `interface.py` file located in the `interface` directory.
2. **Modify Food Items**: Adjust the customer instance, food items, and their details within the `interface.py` file as needed.
3. **SMS Functionality**: The application will send an SMS recap of the order to the customer, leveraging Twilio’s API for communication.

## Features

- **Dynamic Food Item Management**: Easily modify and manage food items and their prices through the interface.
- **Order Recap**: Automatic SMS notifications summarising the customer’s order.
- **Activity Logging**: Detailed logs of SMS activities stored in a text file for reference.

## Key Learnings

- **Object-Oriented Programming (OOP)**: Applied OOP principles to design and structure the application, enhancing modularity and maintainability.
- **API Integration**: Gained experience in integrating third-party APIs, such as Twilio, into a Python application.
- **User Interface Design**: Developed skills in creating user interfaces that facilitate seamless customer interactions.
- **Order Processing**: Implemented functionality for managing and processing customer orders effectively.

## Challenges

- **API Integration**: Configuring and integrating the Twilio API required thorough testing and adjustments.
- **Interface Usability**: Ensuring the interface was user-friendly and met all project requirements was a key challenge.

This repository showcases the implementation of a takeaway ordering system with SMS notification capabilities, reflecting the integration of various technologies to enhance user experience and functionality.

