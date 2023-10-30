## Table of Contents
- [Overview](#overview)
- [Purpose](#purpose)
- [Configuration](#configuration)
  - [Prerequisites](#prerequisites)
  - [Configuration Steps](#configuration-steps)

## Overview

This project is an AWS Lambda function that automatically starts or stops Amazon Elastic Compute Cloud (EC2) instances based on their configured tags. The function is designed to be triggered periodically, such as every hour, to check the tags of EC2 instances and determine if they should be started or stopped. It helps you save costs by ensuring that your EC2 instances are only running when needed.

## Purpose

The purpose of this AWS Lambda function is to automate the management of your EC2 instances by examining their tags. You can use specific tags to control when an instance should be started or stopped. For example, you can set tags to specify the days and times when an instance should be active, and the function will perform the corresponding actions.

## Configuration

![image](https://github.com/Jindding/awsLambda-ec2-auto-stop-start/assets/49447802/74b77c88-71e4-47b1-89a0-b62ef5a09b9e)

<hr/>

![image](https://github.com/Jindding/awsLambda-ec2-auto-stop-start/assets/49447802/05219412-57bd-4f06-96d2-2d098d6ed1c0)

<hr/>

![image](https://github.com/Jindding/awsLambda-ec2-auto-stop-start/assets/49447802/1f2c2221-c0a6-4aec-b4fe-5fab137a16c1)

### Prerequisites

Before you can use this Lambda function, you need to configure it with your AWS credentials and specify the rules for starting and stopping instances based on their tags. Here's what you need to do:
- You should have an AWS account and access to the AWS Management Console.
- You need to set up an IAM user with the necessary permissions to interact with EC2 instances.

### Configuration Steps

1. **Access Key and Secret Key**: Replace the placeholders in the code with your AWS Access Key and Secret Key. It's recommended to use IAM roles and avoid hardcoding credentials for better security.

2. **Region**: Make sure the `region` variable is set to your desired AWS region, e.g., 'ap-northeast-2' for the Seoul region.

3. **Tag Configuration**: Tag your EC2 instances with the following tags:

   - `AUTO_STOP_ENABLE`: Set this tag to "true" to indicate that the auto stop/start feature should be applied to the instance.

   - `AUTO_STOP_DAY`: Specify the days of the week when the instance should be active, separated by commas (e.g., "월, 화, 수"). The code will check the current day against this tag.

   - `AUTO_STOP_TIME`: Specify the time range when the instance should be active, using the format "start_time~end_time" (e.g., "9~17"). The code will check the current hour against this tag.
