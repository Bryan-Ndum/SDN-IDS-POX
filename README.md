SDN IDS using POX
This project implements an Intrusion Detection System (IDS) for Software-Defined Networking (SDN) using the POX controller. It monitors network traffic, detects anomalies, and logs suspicious activities.

📌 Features
✔️ Monitors network flows in SDN
✔️ Detects anomalous traffic patterns based on predefined thresholds
✔️ Logs suspicious traffic flows for further analysis
✔️ Integrates with Mininet and POX for real-time monitoring
✔️ Customizable thresholds for packet and byte rate monitoring

⚡ Installation & Setup

Step 1: Clone the Repository

COPY THIS

git clone https://github.com/Bryan-Ndum/SDN-IDS-POX.git
cd SDN-IDS-POX

Step 2: Install Dependencies
Ensure Python 3 is installed, then install required dependencies.

COPY THIS

sudo apt update
sudo apt install python3-pip

Step 3: Install POX Controller

COPY THIS AND PASTE IN A SEPERATE TERMINAL

git clone https://github.com/noxrepo/pox.git
cd pox
./pox.py forwarding.l2_learning


Step 4: Run the IDS
Go back to your project folder:

COPY THIS

cd ../SDN-IDS-POX

Run the IDS:

COPY THIS

./pox.py ids_pox
🔧 Running with Mininet

To test your IDS, start a Mininet topology: (OPEN A NEW TERMINAL)

COPY THIS

sudo mn --topo single,3 --controller remote
This creates a simple 3-host topology and connects it to the remote POX controller.

🛠 How It Works

The IDS listens to PacketIn events from the POX controller.
It tracks the packet rate and byte rate per network flow.
If a flow exceeds predefined thresholds, the IDS logs a warning.
The IDS uses threading to continuously monitor and detect anomalies.

🚨 Example Log Output (Anomaly Detected)

COPY THIS
WARNING: Anomaly detected for flow (00:00:00:00:00:01, 00:00:00:00:00:02):
Packet Rate=150, Byte Rate=2000000
📝 Configuration
Modify the threshold values in ids_pox.py to suit your needs:

python

COPY THIS

THRESHOLD_PACKET_RATE = 100  # Packets per second
THRESHOLD_BYTE_RATE = 1000000  # Bytes per second
You can increase or decrease these values based on network activity.

💡 Future Improvements
🚀 Implement Machine Learning-based Anomaly Detection
🚀 Support for Signature-Based Attack Detection
🚀 Enhanced Logging & Reporting Mechanism

📜 License
This project is licensed under the MIT License.

🤝 Contributing
Want to improve this project? Feel free to fork it, open an issue, or submit a pull request! 🎯

📬 Contact
For any queries, reach out via GitHub Issues or email me

