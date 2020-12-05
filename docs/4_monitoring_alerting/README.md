# Session 4
How to monitor my service and receive alert if something goes wrong?

## Architecture

In this training session, we will use CloudWatch to monitor the number of mqtt messages published and use CloudWatch Alarm to detect if number of mqtt messages published is too high, and SNS to be notified by text message:
![](img/architecture.png)

## CloudWatch
In this section, we will use CloudWatch:
![](img/architecture_cloudwatch.png)

CloudWatch is a monitoring and observability service built for DevOps engineers, developers, site reliability engineers (SREs), and IT managers. CloudWatch provides you with data and actionable insights to monitor your applications, respond to system-wide performance changes, optimize resource utilization, and get a unified view of operational health

### Use CloudWatch to monitor MQTT published messages

1. Open the CloudWatch console.
![](img/cloudwatch_service.png)

1. Select __Metrics__ and __IoT__.
![](img/cloudwatch_metrics_iot.png)

1. Select __Protocol Metrics__.
![](img/cloudwatch_metrics_iot_mqtt_1.png)

1. Select __PublishIn.Success__.
![](img/cloudwatch_metrics_iot_mqtt_2.png)

1. Use __Sum__ as __static__.
![](img/cloudwatch_metrics_iot_mqtt_3.png)

1. Use __1 minute__ as __Period__.
![](img/cloudwatch_metrics_iot_mqtt_4.png)

1. You can see number of mqtt messages per minute.
![](img/cloudwatch_metrics_iot_mqtt_5.png)

### Set up CloudWatch Alarm to detect if number of mqtt messages per minute is too high

1. Open the CloudWatch console.
![](img/cloudwatch_service.png)

1. Select __Alarms__
![](img/cloudwatch_alarm.png)

1. __Create alarm__
![](img/cloudwatch_alarm_1.png)

1. __Select metric__
![](img/cloudwatch_alarm_2.png)

1. __IoT__
![](img/cloudwatch_alarm_3.png)

1. __Protocol Metrics__ > __PublishIn.Success__.
![](img/cloudwatch_alarm_4.png)

1. __Static__:`Sum` __Period__:`1 minute`.
![](img/cloudwatch_alarm_5.png)

1. Parameter threshold.
![](img/cloudwatch_alarm_6.png)

1. Create a SNS topic with your email.
![](img/cloudwatch_alarm_7.png)
![](img/cloudwatch_alarm_8.png)

1. Add alarm name. For example, `cxp_insa_tp_iot_mqtt_messages_too_many`
![](img/cloudwatch_alarm_9.png)

1. Create alarm.
![](img/cloudwatch_alarm_10.png)
![](img/cloudwatch_alarm_11.png)

## SNS
In this section, we will use SNS to send notification:
![](img/architecture_sns.png)

Amazon Simple Notification Service (Amazon SNS) is a fully managed messaging service for both application-to-application (A2A) and application-to-person (A2P) communication

### SNS topic subscription

1. Open the SNS console.
![](img/sns_service.png)

1. Click on SNS topic created in cloudwatch alarm section.
![](img/sns_1.png)

1. __Create subscription__
![](img/sns_2.png)

1. __Protocol__: `SMS`
![](img/sns_3.png)

1. Enter your phone number and __Create subscription__
![](img/sns_4.png)

### Trigger an alarm

Re publish all mqtt messages of session 1 to verify if you receive a sms notification

[session 1](../1_publish_mqtt/README.md)