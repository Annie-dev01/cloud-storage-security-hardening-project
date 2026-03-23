# Cloud Storage Security Hardening Lab

## Overview

This project demonstrates a practical cloud security exercise focused on identifying and mitigating common risks associated with cloud storage services such as Amazon S3 and Azure Blob Storage.

The goal of this lab was to simulate how a security engineer would analyze potential threats to cloud storage and implement controls to reduce the risk of data exposure or unauthorized access.


## Threat Modeling

Several potential threats were identified during this exercise:

- Public data exposure due to misconfigured bucket permissions
- Privilege escalation through overly permissive IAM roles
- Unauthorized data access
- Ransomware targeting exposed storage
- Lack of audit visibility


## Security Controls Implemented

To mitigate these risks, the following security measures were implemented:

- Encryption at rest
- Encryption in transit (HTTPS)
- Restrictive bucket access policies
- Access logging enabled
- Monitoring access activity


## Key Security Concepts Practiced

- Cloud threat modeling
- Secure configuration of storage services
- Principle of least privilege
- Logging and monitoring for security visibility


## Tools Used

- Amazon S3 / Azure Blob Storage
- Cloud access policies
- Encryption configurations


## Lessons Learned

This exercise helped me reinforce the importance of properly configuring cloud storage resources to prevent data leaks and unauthorized access. It also highlighted how logging and monitoring play a crucial role in detecting suspicious access patterns.


## Future Improvements

- Automating security enforcement using Terraform
- Monitoring alerts for suspicious access
- Integrating cloud logs with a SIEM platform
