# Assignment8-IST105-0313

```bash
sudo dnf update -y
sudo dnf install -y httpd
sudo dnf install python3 -y
sudo dnf install -y php
sudo dnf -y install git
cd /var/www/html
sudo git clone https://github.com/itouoti12/IST105-0404-DigitalPartyPlanner.git .
sudo chmod +x /var/www/html/party_planner.py
sudo systemctl start httpd

```
