# **SimCorp-Project**
***

## Project Scope:

Our primary concern centers around the security of SimCorp's cloud systems following a recent data exposure incident due to misconfigured instances. To address this, we've been tasked to support for a comprehensive adversary emulation engagement. This endeavor necessitates the formation of two vital teams - the **Red Team** and the **Blue Team**.

### Red Team's Role (our role):

The Red Team is tasked with the emulation of potential adversaries. Our expertise will be invaluable in identifying vulnerabilities within SimCorp's systems and simulating realistic attacks to uncover potential weaknesses. Through these efforts, we aim to proactively address vulnerabilities before they can be exploited maliciously.

### Blue Team's Role:

The Blue Team is entrusted with enhancing SimCorp's defensive systems. The team will play a pivotal role in elevating SimCorp's threat detection capabilities, constantly monitoring their network for any anomalies. The team's insights will be instrumental in fortifying SimCorp's security infrastructure.

## Red Team Objectives

We've been tasked with enumerating the target network from a "black boc" position (minimal knowledge of the target environment) starting with a foothold on a single endpoint.

One of our goals is discovering as many vulnerabilities as we can and documenting them in accordance with community resources such as CWE and CVSS.

We'll also get to apply TTPs we've learned throughout this course and perform exploits as the opportunities present themselves. Document how we went about executing TTPs and whether they were successful or not.

### Red Team Staging

We will be provided with a single compromised endpoint instance as well as VPN access to its LAN to facilitate tool execution.

For example, if we wanted to perform attacks from Kali Linux, we would activate an OpenVPN connection from Kali Linux to the target network.

### Red Team Objectives (RTOS)

**RTOS1.** Enumerate the target network, gleaning as much information as possible about the various hosts and their configurations. Document in detail what tools were used and how much you were able to reveal.

* **RTO1a.** Create a professional network topology of the target environment for inclusion in your final report.

**RTO2.** Discover vulnerabilities on targets hosts on the network. There will be at least one web application for you to discover and test against, in addition to several other instances running various operating systems with unknown configurations.

**RTO3.** Build/customize and utilize at least one custom Python tool to aid in your team's offensive efforts.

**RTO4.** Exploit and gain access to as many host instances as possible, and as deeply as possible.

> While hacking is great fun, it is important to be sure to take plenty of screeshots and document what worked and didn't work in order to produce a high quality report deliverable.

## Rules of Engagement

* Do not attack or damage the hypervisor software on instances
* Read and abide by the [AWS Pentesting Policy](https://aws.amazon.com/security/penetration-testing/)
* Do not alter the firewall or port configurations on the instances
* Do not attack tooling systems: OpenVPN server instance; SIEM instance; Threat hunter instance
* Do not damage the operability of the instances
* Do not delete data on the instances
* If you need a reboot on an instance, contact the white team

## Deliverables:

* [TeamAgreements](https://github.com/VascoLucas01/Cyber-Final-Project/tree/main/TeamAgreements)
* [Kali-Ma-PenTesting-Report](https://drive.google.com/file/d/1BOD2nTQUxHmKeSktVoJ5CLDfRYCDYCSc/view?usp=sharing)
* [TTPs attempted mapped 1:1 to MITRE ATT&CK](https://drive.google.com/file/d/1AYK3k1ejZ4gel-8MJtU4YXLC2W4eAZAy/view?usp=sharing)

## Team Contributors:

| [![Vasco Lucas](https://avatars.githubusercontent.com/u/110473841?v=4&s=144)](https://github.com/VascoLucas01) | [![Sérgio Charruadas](https://avatars.githubusercontent.com/u/20626461?v=4&s=144)](https://github.com/itzvenom) | [![José Serpa Pinto](https://avatars.githubusercontent.com/u/79847245?v=4&s=144)](https://github.com/jserpa-p) |
|---|---|---|
| [Vasco Lucas](https://github.com/VascoLucas01) | [Sérgio Charruadas](https://github.com/itzvenom) | [José Serpa Pinto](https://github.com/jserpa-p) |
