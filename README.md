# Welcome to the SmartBin Repository

Welcome to the SmartBin repository, where we aim to drive sustainable recycling behaviors using an interactive, IoT-based smart trash bin. This project leverages persuasive technology and participatory design methodologies to increase user engagement in recycling, with applications that are particularly impactful in educational and community settings.

---

## Project Overview

The SmartBin project integrates concepts from **Human-Computer Interaction (HCI)**, **Internet of Things (IoT)**, and **behavioral psychology** to promote environmentally conscious actions. Through smart technology and engaging feedback mechanisms, the SmartBin system encourages users to make sustainable choices by providing real-time feedback and educational content on recycling.

---

## Key Features

- **Interactive Feedback**: Equipped with sensors to detect waste disposal, the bin provides instant feedback using memes and animations, making the recycling experience engaging and rewarding.
- **Real-Time Monitoring**: The SmartBin uses an ultrasonic sensor to monitor its fill level, notifying waste collectors when it is ready for emptying, thus optimizing collection schedules.

---

## Installation and Setup

### Hardware Requirements:
- Raspberry Pi (Model 3 B+ or higher)
- Ultrasonic sensor for bin level detection
- Laser and LDR sensor for disposal detection
- Monitor for meme display
- WiFi connectivity for IoT functionalities

### Software Requirements:
- Python 3.x
- Required libraries listed in `requirements.txt`
- Telegram bot setup for real-time notifications to waste collection teams

### Setup:
1. Clone the repository and install the required libraries.
2. Configure the sensors and the Telegram bot for notifications.
3. Deploy the application on the Raspberry Pi and ensure all connections are secure.

---

## Usage

- **Disposal Detection**: As users dispose of items, the system detects the action and displays an educational or motivational meme to reinforce recycling behavior.
- **Monitoring and Notifications**: When the bin reaches capacity, the system notifies the waste collection team via Telegram for timely emptying.
- **Web Application**: Accessible from any device, the web app provides recycling tips, locations of collection centers, and interactive content on sustainability.

---

## Design and Methodology

SmartBin was developed using a **Participatory Action Design Research** approach, involving students and community members in design cycles to iteratively improve user engagement. Insights from these cycles have shaped the user-centric design and features, prioritizing accessibility and effectiveness in promoting recycling behaviors.

---

## Acknowledgments

This project is part of a research initiative at the **Federal University of Rio de Janeiro**, funded by **CAPES**, and supervised by **Claudio Miceli** and **Daniel Schneider**. The project extends gratitude to the students and faculty involved in the participatory design process.

---

Explore, contribute, and let’s make sustainable choices together with SmartBin!
